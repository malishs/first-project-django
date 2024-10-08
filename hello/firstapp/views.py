from django.http import *
from django.template.response import TemplateResponse
from .forms import UserForm
from .models import Person
from .models import Company, Product
from .models import Student, Cours
from .models import User, Account
from django.db.models import F 

alex = User.objects.create(name="Александр")
acc = Account(login = "1234", password="6565")
alex.account = acc
alex.account.save()
alex.account.login = "qwerty"
alex.account.password = "123456"
alex.account.save()

def index(request):
    people = Person.objects.all()
    return TemplateResponse(request, "index.html", {"people": people})

def create(request):
    if request.method == "POST":
        klient = Person()
        klient.name = request.POST.get("name")
        klient.age = request.POST.get("age")
        klient.save()
    return HttpResponseRedirect("/")

def edit(request, id):
    try:
        person = Person.objects.get(id=id)
        if request.method == "POST":
            person.name = request.POST.get("name")
            person.age = request.POST.get("age")
            person.save()
            return HttpReponseRedirect("/")
        else:
            return TemplateResponse(request, "edit.html", {"person": person})
    except Person.DoesNotExists:
        return HttpReponseNotFound("<h2>Клиент не найден</h2>")

def delete(request, id):
    try:
        person = Person.objects.get(id=id)
        person.delete()
        return HttpRepsonseRedirect("/")
    except Person.DoesNotExists:
        return HttpResponseRedirect("/about")

def personal(request):
    header = "Персональные данные"
    langs = ["Английский", "Немецкий", "Испанский"]
    user = {"name": "Максим,", "age": 30}
    addr = ("Виноградная", 23, 45)
    data = {"header": header, "langs": langs, "user": user, "address": addr}
    return TemplateResponse(request, "index.html", data)

def about(request):
    return HttpResponse("About")

def contact(request):
    return HttpResponseRedirect("/about")

def details(request):
    return HttpResponsePermanentRedirect("/")

def products(request, productid):
    category = request.GET.get("cat", "")
    output = "<h2>Продукт № {0} Категория: {1}</h2>".format(productid, category)
    return HttpResponse(output)

def users(request):
    id = request.GET.get("id", 1)
    name = request.GET.get("name", "Максим")
    output = "<h2>Пользователь</h2><h3>id: {0} Имя: {1} </h3>".format(id,name)
    return HttpResponse(output)

def chaihana(request):
    cat = ["Ноутбуки", "Принтеры", "Сканеры", "Диски", "Шнуры"]
    return TemplateResponse(request, "firstapp/chaihana.html", context={"cat": cat})

def nameage(request):
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        output = "<h2>Пользователь</h2><h3>Имя - {0}, Возраст - {1}</h3>".format(name, age)
        return HttpResponse(output)
    else:
        nameage = Nameage()
        return TemplateResponse(request, "firstapp/index.html", 
                                {"form": nameage})
def forma(request):
    userForm = UserForm()
    return TemplateResponse(request, "firstapp/formakak.html", 
                                {"form": Forma})