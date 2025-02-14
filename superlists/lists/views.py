from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import List
from .list_form import ListForm

# Create your views here.
# lists = [
#     {'id': 1, 'name': 'Workout'},
#     {'id': 2, 'name': 'Groceries'},
#     {'id': 3, 'name': 'Study'},
# ]

def home(request):
    # Now we add directly the lists to the context
    lists = List.objects.all()
    context = {'lists': lists}
    return render(request, 'home.html',context)

def view_list(request):
    new_list = ListForm()
    context = {'form': new_list}
    return render(request, 'list.html',context)