from django.shortcuts import render
from django.http import Http404
from django.views.generic import DetailView, ListView

from .models import Notes 

class NotesListView(ListView):
    model = Notes
    context_object_name = "notes"
    # template_name = "notes/notes_list.html" # only required while file name is not match with view class name


class NotesDetailView(DetailView):
    model = Notes
    context_object_name = 'note'
    # template_name = "notes/notes_details.html" # only required while file name is not match with view class name

# def list(request):
#     all_notes = Notes.objects.all()
#     return render(request, 'notes/notes_list.html', {'notes':all_notes})


# def detail(request, pk):
#     try:
#         note = Notes.objects.get(pk=pk)
#     except Notes.DoesNotExist:
#         raise Http404("Note does not exist")
#     return render(request, "notes/notes_detail.html", {'note':note})
