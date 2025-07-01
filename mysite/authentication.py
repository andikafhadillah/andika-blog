from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout


def login(request):
    template_name = "login.html"
    Pesan = ""
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        if not username or not password:
            Pesan = "username dan password wajib diisi"
        
        else:      
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                Pesan = "berhasil login"
                return redirect('/')
            else:
                Pesan = "username atau password salah"


    context = {
        'Pesan':Pesan
    }
    return render(request, template_name, context)


def registrasi(request):
    template_name = "registrasi.html"
    Pesan = ''
    if request.method == "POST":
        username = request.POST.get('username')
        nama_depan = request.POST.get('nama_depan')
        nama_belakang = request.POST.get('nama_belakang')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if not username or not nama_depan or not nama_belakang or not password1 or not password2:
            Pesan = "semua data wajib diisi yah"
        else:
            if password1 != password2:
                Pesan = "password 1 dan 2 tidak sama"
            else:
                user = User.objects.filter(username=username)
                if user.exists():
                    Pesan = "username sudah digunakan"
                else:
                    user = User.objects.create(
                        username = username,
                        first_name = nama_depan,
                        last_name = nama_belakang,
                    )
                    user.set_password(password1)
                    user.save()
                    return redirect("/")

    contex = {
        'Pesan':Pesan
    }
    return render(request, template_name, contex)

def logout(requust):
    auth_logout(requust)
    return redirect('/')