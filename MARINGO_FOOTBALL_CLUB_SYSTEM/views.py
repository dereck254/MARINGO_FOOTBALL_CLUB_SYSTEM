from django.shortcuts import render, redirect
from .models import Player
from django.shortcuts import render
def displayindex(request):
    data = Player.objects.all()
    context = {"data" : data}
    return render(request, "index.html", context)

def players(request):
    return render(request, 'players.html')

def insertData(request):
    if request.method == "POST":
        idnumber = request.POST.get('idnumber')
        fullname = request.POST.get('fullname')
        gender = request.POST.get('gender')
        age = request.POST.get('age')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        county = request.POST.get('county')
        school = request.POST.get('school')
        team = request.POST.get('team')
        photo = request.POST.get('photo')

        query = Player(idnumber=idnumber, fullname=fullname, gender=gender, age=age, email=email, contact=contact, county=county, school=school, team=team, photo=photo)
        query.save()
        return redirect("/")
    return render(request, "index.html")

def deleteData(request, id):
    d = Player.objects.get(id=id)
    d.delete()
    return redirect("/")
    return render(request, "players.html")

def updateData(request, id):
    if request.method == "POST":
        idnumber = request.POST.get('idnumber')
        fullname = request.POST.get('fullname')
        gender = request.POST.get('gender')
        age = request.POST.get('age')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        county = request.POST.get('county')
        school = request.POST.get('school')
        team = request.POST.get('team')
        photo = request.POST.get('photo')

        edit = Player.objects.get(id=id)
        edit.idnumber = idnumber
        edit.fullname = fullname
        edit.gender = gender
        edit.age = age
        edit.email = email
        edit.contact = contact
        edit.county = county
        edit.school = school
        edit.team = team
        edit.photo = photo
        edit.save()
        return redirect("/")
    d = Player.objects.get(id=id)
    context = {"d" : d}
    return render(request, "edit.html", context)

def contact(request):
    return render(request, 'contact.html')

def matches(request):
    return render(request, 'matches.html')

def blog(request):
    return render(request, 'blog.html')