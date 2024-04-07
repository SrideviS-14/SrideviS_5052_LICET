from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .forms import MusicForm
from .models import Music
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

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
    query = request.GET.get('q')
    if query:
        songs = Music.objects.filter(title__icontains=query)
    else:
        songs = Music.objects.all()
    listen_later_songs = request.user.listen_later_songs.all()
    return render(request, 'display.html', {'songs': songs, 'listen_later_songs': listen_later_songs})

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

@login_required
def add_to_listen_later(request, song_id):
    song = get_object_or_404(Music, id=song_id)
    request.user.listen_later_songs.add(song)
    return redirect('music:display')

