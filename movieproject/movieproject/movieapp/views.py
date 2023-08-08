from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import FormMovie
from .models import movies


# Create your views here.
def index(request):
    obj=movies.objects.all()
    return render(request,"movie.html",{'result':obj})
def detail(request, id):
    movie = movies.objects.get(id=id)
    return render(request,"details.html",{'movies':movie})
def addmovies(request):
    if request.method=="POST":
        name = request.POST.get('name')
        year = request.POST.get('year')
        desc = request.POST.get('desc')
        img = request.FILES['img']
        user=movies(name=name,year=year,desc=desc,img=img)
        user.save()
    return render(request,"add.html")
def update(request,id):
    movie = movies.objects.get(id=id)
    form = FormMovie(request.POST or None,request.FILES,instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'movie':movie})
def delete(request,id):
    if request.method == "POST":
        movie=movies.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request, 'delete.html')