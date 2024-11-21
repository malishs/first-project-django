from django.contrib import admin
from.models import Author, Book, Genre, Language, Publisher, Status, BookInstance

# Register your models here.
# from django.utils.safestring import mark_safe
from django.utils.html import format_html
# Определение класса AuthorAdmin для авторов книг
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'photo', 'show_photo')
    fields = ('last_name', 'first_name', 'date_of_birth','photo')
    readaonly_fields = ["show_photo"]
    def show_photo(self, obj):
        return format_html(
            f'<img src="{obj.photo.url}" style = "max-height:100px">')
        # можно и с использованием функции mark_safe
        # return mark_safe
            # f'<img scr="{obj.photo.url}" style ="max-height:100px">')
    show_photo.short_description = 'Фото'

# admin.site.register(Author)
# Регестрируем класс AuthorAdmin для авторов кинг
admin.site.register(Author, AuthorAdmin)

class BooksInstanceInline(admin.TabularInline):
    model = BookInstance

# admin.site.register(Book)
# Регестрируем класс BookAadmin для кинг
@admin.register(Book)

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'language', 'display_author', 'show_photo')
    list_filter = ('genre', 'author')
    inlines = [BooksInstanceInline]
    readonly_fields = ["show_photo"]
    def show_photo(self, obj):
        return format_html(
            f'<img src="{obj.photo.url}" style ="max-hieght:100px">')
    show_photo.short_description = 'Обложка'

# admin.site.register(BookInstance)
# Регестрируем класс BookInstanceAdmin для экземпляра книг
@admin.register(BookInstance)

class BookiInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'borrower', 'due_back', 'id') 
    list_filter = ('book', 'status')
    fieldsets = (
        ('Экземпляр книги', {
            'fields': ('book', 'inv_nom')}),
        ('Статус и окончание его действия', {
            'fields': ('status', 'due_back')})
    )

admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(Publisher)
admin.site.register(Status)



# class BooksInstanceInline(admin.TabularInline):
#  model = BookInstance


# @admin.register(Book)
# class BookAdmin(admin.ModelAdmin):
#  list_display = ('title', 'genre', 'language', 'display_author')
#  list_filter = ('genre', 'author')
#  inlines = [BooksInstanceInline]

# @admin.register(BookInstance)
# class BookInstanceAdmin(admin.ModelAdmin):
#     list_display = ('book', 'status', 'borrower', 'due_back', 'id')
#     list_filter = ('status', 'due_back')
#     fieldsets = (
#         (None, {
#             'fields': ('book', 'imprint', 'inv_nom')
#         }),
#         ('Availability', {
#             'fields': ('status', 'due_back', 'borrower')
#         }),       
#         )
#     def borowwer(self):
#         BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='2').order_by('due_back')





