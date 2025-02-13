from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
lists = [
    {'id': 1, 'name': 'Workout'},
    {'id': 2, 'name': 'Groceries'},
    {'id': 3, 'name': 'Study'},
]

def home(request):
    return render(request, 'home.html')

def view_list(request):
    context = {'lists': lists}
    return render(request, 'list.html',context)