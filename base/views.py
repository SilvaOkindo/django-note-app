from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


from .forms import NoteForm
from .models import Notes


# Create your views here.


def register_page(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'A error occurred during registration')
    context = {'form': form}
    return render(request, 'base/register.html', context)


def login_page(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            username = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist.')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'username OR password does not exist.')

    return render(request, 'base/login.html', context)


def logout_page(request):
    logout(request)
    return redirect('welcome')


@login_required(login_url='login')
def home(request):
    notes = Notes.objects.filter(user=request.user)
    context = {"notes": notes}
    return render(request, 'base/home.html', context)


def note(request, pk):
    note = Notes.objects.get(id=pk)
    context = {'note': note}
    return render(request, 'base/note.html', context)


def welcome_page(request):
    return render(request, 'base/welcome_page.html')


@login_required(login_url='login')
def creat_note(request):
    form = NoteForm()
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'base/note_form.html', context)


@login_required(login_url='login')
def update_note(request, pk):
    note = Notes.objects.get(id=pk)
    form = NoteForm(instance=note)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'base/note_form.html', context)


@login_required(login_url='login')
def delete_note(request, pk):
    note = Notes.objects.get(id=pk)
    if request.method == 'POST':
        note.delete()
        return redirect('home')

    return render(request, 'base/delete_note.html', {'obj': note})
