from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, Author, BookInstance, Genre
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import *
from .forms import AuthorsForm, Form_add_author 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy 
from django.urls import reverse
from .models import Book
from .models import Author 
from django import forms
from django.views.generic import ListView, DetailView

# Create your views here.



def index(request): 
    text_head = 'На нашем сайте вы можете получить книги в электронном виде' 
    # Данные о книгах и их количестве 
    books = Book.objects.all() 
    num_books = Book.objects.all().count() 

    # Данные об экземплярах книг в БД 
    num_instances = BookInstance.objects.all().count() 
    # Доступные книги (статус = 'На складе') 
    num_instances_available = BookInstance.objects.filter( 
        status__exact=2).count() 

    # Данные об авторах книг 
    authors = Author.objects 
    num_authors = Author.objects.count() 



    # Количество посещений этого view, подсчитанное в переменной session 
    num_visits = request.session.get('num_visits', 0) 
    request.session['num_visits'] = num_visits + 1 

    # Словарь для передачи данных в шаблон index.html 
    context = {'text_head': text_head, 
        'books': books, 'num_books': num_books, 
        'num_instances': num_instances, 
        'num_instances_available': num_instances_available, 
        'authors': authors, 'num_authors': num_authors,
        'num_visits': num_visits
    }
    # передача словаря context с данными в шаблон 
    return render(request, 'catalog/index.html', context)

def about(request):
    text_head = 'Сведения о компании'
    name = 'ООО "Интеллектуальные информационные системы"'
    rab1 = 'Разработка приложений на основе' \
    ' систем искусственного интеллекта'
    rab2 = 'Распознавание объектов дорожной инфраструктуры'
    rab3 = 'Создание графических АРТ-объектов на основе' \
    ' систем искусственного интеллекта'
    rab4 = 'Создание цифровых интерактивных книг, учебных пособий' \
    ' автоматизированных обучающих систем'
    context = {'text_head': text_head, 'name': name,
    'rab1': rab1, 'rab2': rab2,
    'rab3': rab3, 'rab4': rab4}
    # передача словаря context с данными в шаблон
    return render(request, 'catalog/about.html', context)
def contact(request):
    text_head = 'Контакты'
    name = 'ООО "Интеллектуальные информационные системы"'
    address = 'Москва, ул. Планерная, д.20, к.1'
    tel = '495-345-45-45'
    email = 'iis_info@mail.ru'
    # Словарь для передачи данных в шаблон index.html
    context = {'text_head': text_head,
    'name': name, 'address': address,
    'tel': tel,
    'email': email}
    # передача словаря context с данными в шаблон
    return render(request, 'catalog/contact.html', context)


class BookListView(ListView): 
    model = Book 
    context_object_name = 'books' 

class BookCreate(CreateView): 
    model = Book 
    fields = '__all__' 
    success_url = reverse_lazy('edit_books') 

class BookDelete(DeleteView): 
    model = Book 
    success_url = reverse_lazy('edit_books')    

class BookUpdate(UpdateView): 
    model = Book 
    fields = '__all__' 
    success_url = reverse_lazy('edit_books') 

class BookDetailView(DetailView): 
    model = Book 
    context_object_name = 'book' 

class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 4

class Form_edit_author(forms.ModelForm): 
    class Meta: 
        model = Author 
        fields = '__all__' 

def edit_author(request, id): 
    author = Author.objects.get(id=id) 
    # author = get_object_or_404(Author, pk=id) 
    if request.method == "POST": 
        instance = Author.objects.get(pk=id) 
        form = Form_edit_author(request.POST, request.FILES, instance=instance) 
        if form.is_valid(): 
            form.save() 
        return HttpResponseRedirect("/edit_authors/") 
    else: 
        form = Form_edit_author(instance=author) 
        content = {"form": form} 
        return render(request, "catalog/edit_author.html", content) 



class LoanedBooksByUserListView(LoginRequiredMixin, generic.ListView):

    model = BookInstance
    template_name = 'catalog/Bookinstance_list_Borrowed_user.html'
    paginate_by = 10
    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='2').order_by('due_back')
    
def authors_add(request):
    author = Author.objects.all()
    authorsform = AuthorsForm()
    return render(request, "catalog/authors_add.html",
        {"form": authorsform, "author": author})

def create(request):
    if request.method == "POST":
        author = Author()
        author.first_name = request.POST.get("first_name")
        author.last_name = request.POST.get("last_name")
        author.date_of_birth = request.POST.get("date_of_birth")
        author.date_of_death = request.POST.get("date_of_death")
        author.save()
        return HttpResponseRedirect("/authors_add/")
    
def edit_books(request): 
    book = Book.objects.all() 
    context = {'book': book} 
    return render(request, "catalog/edit_books.html", context) 

def delete(request, id):
    try:
        author = Author.objects.get(id=id)
        author.delete()
        return HttpResponseRedirect("/authors_add/")
    except Author.DoesNotExist:
        return HttpResponseNotFound("<h2>Автор не найден</h2>")

def edit1(request, id):
    author = Author.objects.get(id=id)
    if request.method == "POST":
        author.first_name = request.POST.get("first_name")
        author.last_name = request.POST.get("last_name")
        author.date_of_birth = request.POST.get("date_of_birth")
        author.date_of_death = request.POST.get("date_of_death")
        author.save()
        return HttpResponseRedirect("/authors_add/")
    else:
        return render(request, "edit1.html", {"author": author})
    
class BookCreate(CreateView):
    model = Book
    fields = '__all__'
    success_url = reverse_lazy('books')

class BookUpdate(UpdateView):
    model = Book
    fields = '__all__'
    success_url = reverse_lazy('books')


class BookDelete(DeleteView):
    model = Book
    success_url = reverse_lazy('books')

def start1(request):
    return render(request, "start1.html")

def color_bg(request):
    return render(request, "color_bg.html")

def colortext(request):
    return render(request, "color-text.html")

def color_text_bg(request):
    return render(request, "color_text_bg.html")

def space_1(request):
    return render(request, "space_1.html")

def space_2(request):
    return render(request, "space_2.html")

def space_3(request):
    return render(request, "space_3.html")

def aligment_1(request):
    return render(request, "aligment_1.html")

def aligment_2(request):
    return render(request, "aligment_2.html")

def border_1(request):
    return render(request, "border_1.html")

def border_2(request):
    return render(request, "border_2.html")

def border_color(request):
    return render(request, "border_color.html")

def border_radius_1(request):
    return render(request, "border_radius_1.html")

def border_radius_2(request):
    return render(request, "border_radius_2.html")

def start(request):
    return render(request, "start.html")

def table(request):
    return render(request, "table.html")

def table_1(request):
    return render(request, "table_1.html")

class BookListView(ListView):
 model = Book
 context_object_name = 'books'
 paginate_by = 3

class AuthorListView(ListView):
 model = Author
 paginate_by = 4

class AuthorDetailView(DetailView):
 model = Author

def edit_authors(request): 
  author = Author.objects.all() 
  context = {'author': author} 
  return render(request, "catalog/edit_authors.html", context) 

def add_author(request): 
  if request.method == 'POST': 
     form = Form_add_author(request.POST, request.FILES) 
     if form.is_valid(): 
        # получить данные из формы 
        first_name = form.cleaned_data.get("first_name") 
        last_name = form.cleaned_data.get("last_name") 
        date_of_birth = form.cleaned_data.get("date_of_birth") 
        about = form.cleaned_data.get("about") 
        photo = form.cleaned_data.get("photo") 
        # создать объект для записи в БД 
        obj = Author.objects.create( 
          first_name=first_name, 
          last_name=last_name, 
          date_of_birth=date_of_birth, 
          about=about, 
          photo=photo) 
        # сохранить полученные данные 
        obj.save() 
        # загрузить страницу со списком автором 
        return HttpResponseRedirect(reverse('authors-list')) 
     else: 
         form = Form_add_author() 
         context = {"form": form} 
         return render(request, "catalog/authors_add.html", context)

def delete(request, id): 
  try: 
     author = Author.objects.get(id=id) 
     author.delete() 
     return HttpResponseRedirect("/edit_authors/") 
  except: 
    return HttpResponseNotFound("<h2>Автор не найден</h2>")  