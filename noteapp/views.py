from django.shortcuts import render, redirect
from . models import Note
from .forms import NoteForm
from django.contrib import messages

# Create your views here.


def index(request):
    notes = Note.objects.all()
    context = {"notes": notes}
    return render(request, "noteapp/index.html", context)


def new_note(request):
    form = NoteForm()
    if request.method == 'POST':
        form = NoteForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {"form": form}
    return render(request, "noteapp/new_note.html", context)


def update_note(request, pk):
    note = Note.objects.get(id=pk)
    form = NoteForm(instance=note)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {"note": note, "form": form}
    return render(request, "noteapp/new_note.html", context)


def delete_note(request, pk):
    note = Note.objects.get(id=pk)
    form = NoteForm(instance=note)
    if request.method == 'POST':
        note.delete()
        messages.info(request, "Note has been successfully deleted")
    context = {"note": note, "form": form}
    return render(request, "noteapp/delete_note.html", context)


# def search_note(request):
#     if request.method == 'POST':
#         search_text = request.POST['search']
#         notes = Note.objects.filter(title__icontains=search_text) | Note.objects.filter(
#             body__icontains=search_text)
#         return render(request, "search.html", {"notes": notes})
#     return redirect("index")
