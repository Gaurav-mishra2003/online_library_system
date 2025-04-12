"""
URL configuration for online_library_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from testapp import views

urlpatterns = [
    
    path('',views.home,name='home'),
    path('authors/add/', views.add_author, name='add_author'),
    path('books/add/', views.add_book, name='add_book'),
    path('borrow/add/', views.add_borrow_record, name='add_borrow_record'),

    path('authors/', views.list_authors, name='list_authors'),
    path('books/', views.list_books, name='list_books'),
    path('borrow/', views.list_borrow_records, name='list_borrow_records'),

    # path('export/', views.export_to_excel, name='export_to_excel'),
]

