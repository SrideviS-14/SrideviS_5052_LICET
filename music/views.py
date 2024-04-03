from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .forms import MusicForm
from .models import Music
from django.http import HttpResponseRedirect
from django.urls import reverse


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('music:display')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('music:display')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})
    
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('music:login'))

def display(request):
    songs = Music.objects.all()
    return render(request, 'display.html', {'songs': songs})

from django.contrib.auth.decorators import login_required

@login_required
def add_song(request):
    if request.method == 'POST':
        form = MusicForm(request.POST, request.FILES)
        if form.is_valid():
            music = form.save(commit=False)  # Create Music object but don't save to database yet
            music.uploaded_by = request.user  # Associate the song with the logged-in user
            music.save()  # Save the Music object to database
            return redirect('music:display')
    else:
        form = MusicForm()
    return render(request, 'add_song.html', {'form': form})

