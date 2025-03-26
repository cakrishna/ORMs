from django.shortcuts import render, HttpResponse

# Create your views here.


def home(request):
    return render(request, 'home.html')
    # return HttpResponse("Hello worlds!")

def base(request):
    return render(request, 'about.html')
    # return HttpResponse("Hello worlds!")
