from django.shortcuts import render

# Create your views here.

def index_test(request):

    return render(request, "index.html")


def contact_test(request):

    return render(request, "contact.html")