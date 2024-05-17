import boto3
from django.shortcuts import render, redirect, get_object_or_404
from django.core.files.storage import FileSystemStorage
from .forms import MyFileForm, MyFileUpdateForm
from django.conf import settings
from .models import MyFile


def index(request):
    return render(request, 'index.html')


def home(request):
    return render(request, 'home.html')


def form(request):
    return render(request, 'form.html')


def submitted(request):
    return render(request, 'submitted.html')


def contact(request):
    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')


def honor(request):
    return render(request, 'honor.html')


def adminpanel(request):
    files = MyFile.objects.all().order_by('-uploaded_at')

    # Pass the files to the template
    return render(request, 'adminpanel.html', {'files': files})


def myReports(request):
    files = MyFile.objects.all().order_by('-uploaded_at')
    return render(request, 'myReports.html', {'files': files})


def my_report(request, pk):
    file = get_object_or_404(MyFile, pk=pk)
    return render(request, 'my_report.html', {'file': file})


def admin_report(request, pk):
    file = get_object_or_404(MyFile, pk=pk)
    return render(request, 'admin_report.html', {'file': file})


def upload_file(request):
    if request.method == 'POST':
        form = MyFileForm(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            # report = form.save(commit=False)
            # report.save()
            my_file = form.save(commit=False)
            if request.user.is_authenticated:
                my_file.user = request.user
            else:
                my_file.user = None
            my_file.save()
            form.save()
            return redirect('oauth_app:submitted')  # Redirect to 'submitted' named URL
    else:
        form = MyFileForm()  # Create an instance of the form
    return render(request, 'form.html', {'form': form})


def update_file(request, pk):
    my_file = get_object_or_404(MyFile, pk=pk)

    if request.method == 'POST':
        form = MyFileUpdateForm(request.POST, instance=my_file)
        if form.is_valid():
            form.save()
            return redirect('adminpanel')  # Redirect to a success page or any other URL
    else:
        form = MyFileUpdateForm(instance=my_file)

    return render(request, 'admin_report.html', {'form': form})


def delete_report(request, pk):
    my_file = get_object_or_404(MyFile, pk=pk)

    if request.user == my_file.user:
        my_file.delete()

    return redirect('myReports')  # replace with your view name


def delete_admin_report(request, pk):
    my_file = get_object_or_404(MyFile, pk=pk)

    my_file.delete()

    return redirect('adminpanel')  # replace with your view name
