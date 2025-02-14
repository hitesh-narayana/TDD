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
    if request.method == 'POST':
        new_list = ListForm(request.POST)
    if new_list.is_valid():
        
        list_name = new_list.cleaned_data['name']
        if not List.objects.filter(name=list_name).exists():
            # Creates an instance and uncouples the dictionary
            created_list = List.objects.create(**new_list.cleaned_data)
            # trys to save the instance to the database( works incrementally)
            context['created_list_id'] = created_list.id
            return redirect('/')
        
    return render(request, 'list.html',context)