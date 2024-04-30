from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.views import logout_then_login
from .forms import UploadForm, QueryForm, UserModelForm
from .models import UploadedData, CompanyDataModel, UserModel
import csv
from django.http import JsonResponse
from chunked_upload.views import ChunkedUploadCompleteView

class CustomChunkedUploadView(ChunkedUploadCompleteView):
    model = UploadedData

    def on_completion(self, uploaded_file, request):
       # Process the uploaded file and insert contents to the database
        with uploaded_file.file.open(mode='r') as file:
            csv_file = file.read().decode('utf-8')
            csv_reader = csv.DictReader(csv_file.splitlines())
            for row in csv_reader:
                data = {
                    'name': row['name'],
                    'domain': row['domain'],
                    'industry': row['industry'],
                    'year_founded': row['year founded'],
                    'size_range': row['size range'],
                    'locality': row['locality'],
                    'country': row['country'],
                    'linkedin_url': row['linkedin url'],
                    'current_employee_estimate': row['current employee estimate'],
                    'total_employee_estimate': row['total employee estimate']
                }
                CompanyDataModel.objects.create(**data)        
        # return super().on_completion(uploaded_file, request)

# Create your views here.
def login(request: HttpRequest) -> HttpResponse:
    return render(request, 'login.html')

@login_required
def upload(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = form.cleaned_data['file']
            uploaded_data = UploadedData.objects.create(user=request.user, file=uploaded_file)

            # Process the uploaded file and insert contents to the database
            with uploaded_data.file.open(mode='r') as file:
                csv_file = file.read().decode('utf-8')
                csv_reader = csv.DictReader(csv_file.splitlines())
                for row in csv_reader:
                    data = {
                        'name': row['name'],
                        'domain': row['domain'],
                        'industry': row['industry'],
                        'year_founded': row['year founded'],
                        'industry': row['industry'],
                        'size_range': row['size range'],
                        'locality': row['locality'],
                        'country': row['country'],
                        'linkedin_url': row['linkedin url'],
                        'current_employee_estimate': row['current employee estimate'],
                        'total_employee_estimate': row['total employee estimate']
                    }
                    print(data['name'], data['domain'], data['company'], sep='-')
                    CompanyDataModel.objects.create(**data)
            return redirect('upload-url')
    else:
        form = UploadForm()
    return render(request, 'upload.html', {'form': form})

def query_builder(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = QueryForm(request.POST)
        if form.is_valid():
            user_query = form.save(commit=False)
            user_query.user = request.user
            user_query.save()
            # Perform the query and display results
    else:
        form = QueryForm()
    return render(request, 'query.html', {'form': form})

@login_required
def logout_user(request: HttpRequest):
    logout_then_login(request)
    return redirect('login-url')

# User Management
def get_all_users(request: HttpRequest) -> HttpResponse:
    return render(request, 'Users.html', context={'Users': UserModel.objects.all().reverse()})

def get_user_detail(request: HttpRequest, pk: int) -> HttpResponse:
    user = get_object_or_404(UserModel, pk=pk)
    return render(request, 'user_detail.html', {'user': user})

def create_new_user(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = UserModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user-list')
    else:
        form = UserModelForm()
    return render(request, 'user-form.html', {'form': form})

def edit_user(request: HttpRequest, pk: int) -> HttpResponse:
    user = get_object_or_404(UserModel, pk=pk)
    if request.method == 'POST':
        form = UserModelForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user-list')
    else:
        form = UserModelForm(instance=user)
    return render(request, 'user-form.html', {'form': form})

def delete_user(request: HttpRequest, pk: int) -> HttpResponse:
    user = get_object_or_404(UserModel, pk=pk)
    if request.method == 'POST':
        user.delete()
        return redirect('user-list')
    return render(request, 'user_confirm_delete.html', {'user': user})