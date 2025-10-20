from django.shortcuts import render,redirect
from app1.models import Stundents
from app1.forms import StudentsForm
# Create your views here.
def list_students_view(request):
    stundets_list=Stundents.objects.all()
    return render(request,'app1/index.html',{'students_list':stundets_list})

def add_student_view(request):
    form=StudentsForm()
    if request.method=="POST":
        form=StudentsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request,'app1/insert.html',{'form':form})

def update_student_view(request,id):
    Stundent=Stundents.objects.get(id=id)
    form=StudentsForm(instance=Stundent)
    if request.method=="POST":
        form=StudentsForm(request.POST,instance=Stundent)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request,'app1/update.html',{'form':form})

def delete_student_view(request,id):
    Stundent=Stundents.objects.get(id=id)
    Stundent.delete()
    return redirect('/')
    