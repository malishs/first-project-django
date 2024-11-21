"""
URL configuration for WebBooks project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from catalog import views
# from .import views
from django.urls import re_path
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', views.index, name='index'),
    # path('', include('catalog.urls')),
    path('admin/', admin.site.urls),
    path('books/', views.BookListView.as_view(), name='books'),
    path('books/', views.BookListView.as_view(), name='books-list'),
    path('books/<int:pk>/', views.BookDetailView.as_view(), name='book-detail'),
    # path('books/', views.BookListView.as_view(), name='books'),
    # re_path(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
    re_path(r'^authors/$', views.AuthorListView.as_view(), name='authors'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    path('authors_add/', views.authors_add, name='authors_add'),
    path('edit1/<int:id>/', views.edit1, name='edit1'),
    path('create/', views.create, name='create'),
    path('delete/<int:id>/', views.delete, name='delete'),
    re_path(r'^book/create/$', views.BookCreate.as_view(), name='book_create'),
    re_path(r'^book/update/(?P<pk>\d+)$', views.BookUpdate.as_view(), name='book_update'),
    re_path(r'^book/delete/(?P<pk>\d+)$', views.BookDelete.as_view(), name='book_delete'),
    path('authors/', views.AuthorListView.as_view(), name='authors-list'),
    path('authors/<int:pk>/', views.AuthorDetailView.as_view(), name='authors-detail'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('edit_authors/', views.edit_authors, name='edit_authors'),
    path('edit_author/<int:id>/', views.edit_author, name='edit_author'),
    path('authors_add/', views.add_author, name='authors_add'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('edit_books/', views.edit_books, name='edit_books'), 
    path('book/create/', views.BookCreate.as_view(), name='book_create'), 
    path('book/update/<int:pk>/', views.BookUpdate.as_view(), name='book_update'), 
    path('book/delete/<int:pk>/', views.BookDelete.as_view(), name='book_delete'), 
    # path ('start1/', views.start1, name='start1'),
    # path ('color_bg/', views.color_bg, name='color_bg'),
    # path ('color-text/', views.colortext, name='color-text'),
    # path ('color_text_bg/', views.color_text_bg, name='color_text_bg'),
    # path ('space_1/', views.space_1, name='space_1'),
    # path ('space_2/', views.space_2, name='space_2'),
    # path ('space_3/', views.space_3, name='space_3'),
    # path ('aligment_2', views.aligment_2, name='aligment_2'),
    # path ('border_1', views.border_1, name='border_1'),
    # path ('border_2', views.border_2, name='border_2'),
    # path ('border_color', views.border_color, name='border_color'),
    # path ('border_radius_1', views.border_radius_1, name='border_radius_1'),
    # path ('border_radius_2', views.border_radius_2, name='border_radius_2'),
    # path ('start', views.start, name='start'),
    # path ('table', views.table, name='table'),
    # path ('table_1', views.table_1, name='table_1'),
]
if settings.DEBUG:
    # if settings.DEBUG:
        urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
