from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from whashudit.models import MemberInfo, Review
from whashudit.forms import UserForm

# Create your views here.


def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)  # 사용자 인증
            login(request, user)  # 로그인

            return redirect('/home/')
    else:
        form = UserForm()

    return render(request, 'whashudit/signup.html', {'form': form})


def home(request):

    page = Review.objects.all()
    return render(request,'whashudit/home.html',{
        'page' : page
    })


def search(request):

    page = Review.objects.all()
    return render(request,'whashudit/search.html',{
        'page' : page
    })
