from django.shortcuts import render,redirect
from .forms import ContactForm
from django.contrib.auth.decorators import login_required
from courses.models import Courses


def redirect_home(request):

    return redirect("home/")


def index_test(request):

    all_courses = Courses.objects.all()
    return render(request, "index.html", {"courses" : all_courses})


def contact_test(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home/')
    form = ContactForm()
    return render(request, "contact.html", {'form' : form})


def courses_test(request):
    return render(request, "courses.html")

def about_test(request):
    return render(request, "about.html")


def login(request):
    return render(request, "login.html")

def register(request):
    return render(request, "register.html")