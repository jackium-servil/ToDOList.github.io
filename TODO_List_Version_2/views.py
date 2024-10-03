from django.shortcuts import render, redirect
from .forms import Form
from .models import Tasks
# Create your views here.

def home(request):
    form = Form()
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid:
            form.save()
            return redirect('home')
    form1 = Tasks.objects.all()    
    context = {"Task":form1, "form":form}
    return render(request, "home.html", context=context)


def edit(request, pk):
    task = Tasks.objects.get(id=pk)
    form = Form(instance=task)   
    if request.method == "POST":
        form = Form(request.POST, instance=task)
        if form.is_valid:
            form.save()
            return redirect('home')        
    context = {'form':form}
    return render(request, "edit.html", context=context)


def deleting(request, pk):
    task = Tasks.objects.get(id=pk)
    task.delete()
    return redirect('home')
    
def viewing(request, pk):
    task = Tasks.objects.get(id=pk)
    context = {'task':task}
    return render(request, "view.html", context=context)
