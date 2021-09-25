from django.shortcuts import render
from . models import Task
# Create your views here.
def add(request):
    task1=Task.objects.all()
    if request.method=='POST':
        name=request.POST.get('task','')
        priority = request.POST.get('priority','')
        date = request.POST.get('date', '')
        task=Task(name=name,priority=priority,date=date)
        task.save()
    return render(request,"home.html",{'task1':task1})