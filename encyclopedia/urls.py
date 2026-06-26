from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki", views.index, name="wiki_index"),
    path("wiki/", views.index, name="wiki_index_slash"),
    
    path("search", views.search, name="search"),
    path("search/", views.search, name="search_slash"),
    
    path("new", views.new_page, name="new_page"),
    path("new/", views.new_page, name="new_page_slash"),
    path("wiki/new", views.new_page, name="wiki_new_page"),
    path("wiki/new/", views.new_page, name="wiki_new_page_slash"),
    
    path("random", views.random_page, name="random_page"),

    path("wiki/<str:title>", views.entry, name="wiki_entry"),
    path("<str:title>", views.entry, name="entry"),
    path("edit/<str:title>", views.edit, name="edit"),
    
]
