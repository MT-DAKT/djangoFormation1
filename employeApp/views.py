from django.shortcuts import render, redirect

from employeApp.models import Member


def index(request):
    employe=Member.objects.all()
    return render(request, 'index.html', {'employe':employe})

def add(request):
    return render(request, 'add.html')

def addrec(request):
    x = request.POST['first']
    y = request.POST['last']
    z = request.POST['country']
    member=Member(firstname=x,lastname=y,country=z)
    member.save()
    return redirect("/")

def delete(request, id):
    member=Member.objects.get(id=id)
    member.delete()
    return redirect("/")

def update(request, id):
    member=Member.objects.get(id=id)
    return render(request, 'update.html',{'member':member})

def uprec(request, id):
    x = request.POST['first']
    y = request.POST['last']
    z = request.POST['country']
    member=Member.objects.get(id=id)
    member.firstname=x
    member.lastname=y
    member.country=z
    member.save()
    return redirect("/")


