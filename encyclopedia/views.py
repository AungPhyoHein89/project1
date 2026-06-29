from django.shortcuts import render, redirect
import markdown2
from . import util
from .forms import NewEntryForm
import random


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    markdown_content = util.get_entry(title)
    
    if markdown_content is None:
        return render(request, "encyclopedia/error.html", {
            "title": title,
            "message": f"The requested page with title: {title} was not found."
        })
    
    content = markdown2.markdown(markdown_content)
    return render(request, "encyclopedia/entry.html", {
        "title": title,
        "content": content
    })

def edit(request, title):
    if request.method == "POST":
        update_content = request.POST.get("content")
        util.save_entry(title, update_content)
        return redirect("entry", title=title)
    
    existing_content = util.get_entry(title)
    return render(request, "encyclopedia/edit.html", {
        "title": title,
        "content": existing_content
    })
    

def new_page(request):
    if request.method == "POST":
        form = NewEntryForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            if util.get_entry(title) is not None:
                return render(request, "encyclopedia/new_page.html", {
                    "error": f"The Page you created with title:{title} is already existed.",
                    "form": form 
            })
            
            util.save_entry(title, content)
            return redirect("entry", title=title)
        
    else:    
        return render(request, "encyclopedia/new_page.html", {
            "form": NewEntryForm()
            })

def search(request):
    query = request.GET.get('q', '').strip()
    all_entries = util.list_entries()
    for entry in all_entries:
        if query.lower() == entry.lower():
            return redirect("entry", title=entry)
    
    matching_entries = []
    for entry in all_entries:
        if query.lower() in entry.lower():
            matching_entries.append(entry)
    
    return render(request, "encyclopedia/search.html", {
        "query": query,
        "entries": matching_entries
    })

def random_page(request):
    title = util.list_entries()
    random_title = random.choice(title)
    return redirect("entry", title=random_title)