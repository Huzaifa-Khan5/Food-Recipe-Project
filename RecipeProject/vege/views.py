from django.shortcuts import render,redirect
from .models import *

# Create your views here.

def receipes(request):
    if request.method=="POST":
        data=request.POST
        receipe_name=data.get("receipe_name")
        receipe_description=data.get("receipe_description")
        receipe_img=request.FILES.get("receipe_img")

        Receipe.objects.create(
            receipe_name=receipe_name,
            receipe_description=receipe_description,
            receipe_img=receipe_img
        )
        return redirect("/")
    queryset=Receipe.objects.all()

    if request.GET.get("Search"):
        queryset=queryset.filter(receipe_name__icontains=request.GET.get("Search"))

    return render(request,'receipes.html',{'receipes':queryset})

def delete_receipe(request,id):
    queryset=Receipe.objects.get(id=id)
    queryset.delete()
    return redirect("/")

def update_receipe(request,id):
    queryset=Receipe.objects.get(id=id)
    if request.method=="POST":
        data=request.POST
        receipe_name=data.get("receipe_name")
        receipe_description=data.get("receipe_description")
        receipe_img=request.FILES.get("receipe_img")
        queryset.receipe_name=receipe_name
        queryset.receipe_description=receipe_description

        if receipe_img:
            queryset.receipe_img=receipe_img
        
        queryset.save()
        return redirect("/") 

    return render(request,'update_receipe.html',{'receipe':queryset})


