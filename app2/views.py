from django.shortcuts import render,redirect
from .models import Details

# Create your views here.
def home(request):
    a=Details.objects.all()
    if request.method=='POST':
        name=request.POST.get('name')
        age=request.POST.get('age')
        Details.objects.create(name=name,age=age)
        return redirect('home')

    return render(request, 'index.html',{'a':a})

def delete_task(request,id):
    a=Details.objects.filter(id=id)
    a.delete()
    return redirect('home')
    
def update_task(request,id):
    a=Details.objects.get(id=id)
    if request.method=='POST':
        a.name=request.POST.get('name')
        a.age=request.POST.get('age')
        a.save()
        return redirect('home')
    return render(request,'update.html',{'a':a})

