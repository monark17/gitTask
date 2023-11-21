# yourappname/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .forms import NoteForm, Note

def index(request):
    return render(request, 'index.html')

def login_redirect(request):
    return redirect('add_note')  # Custom login view to redirect to add_note after signing up


@login_required
def user_profile(request):
    # Fetch the user's notes
    user_notes = Note.objects.filter(user=request.user)

    return render(request, 'user_profile.html', {'user_notes': user_notes})

def view_notes(request):
    notes = Note.objects.filter(user=request.user)
    return render(request, 'view_notes.html', {'notes': notes})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login_redirect')  # Redirect to custom login view after signup
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def add_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            return redirect('view_notes')  # Redirect to add_note after adding a note
    else:
        form = NoteForm()
    return render(request, 'add_note.html', {'form': form})
