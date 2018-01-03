from django.shortcuts import render
from blog.models import *

def index(request):
    return render(request,'personal/home.html')

def contact(request):
    return render(request,'personal/contact.html',{'content':['if you like to contact me,please click on social media below','Thank you']})

def login(request):
    return render(request,'personal/login.html')

def btekno(request):
    berita = Post.objects.all()
    konten = {'all_berita':berita}
    return render(request,'personal/btekno.html', konten)

def bpolitik(request):
    return render(request,'personal/bpolitik.html')

def bsosi(request):
    return render(request,'personal/bsosi.html')

def bentertain(request):
    return render(request,'personal/bentertain.html')

def bsains(request):
    berita = Bsains.objects.all()
    konten = {'all_berita':berita}
    return render(request,'personal/bsains.html',konten)

def bekonomi(request):
    berita = Bekonomi.objects.all()
    konten = {'all_berita':berita}
    return render(request,'personal/bekonomi.html',konten)

def login(request):
    return render(request,'personal/login.html')

def signup(request):
    return render(request,'personal/signup.html')

def berita(request):
    return render(request,'personal/berita.html')
