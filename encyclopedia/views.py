from django.shortcuts import render, redirect
import markdown2
import random
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    markdown_content = util.get_entry(title)

    if markdown_content is None:
        return render(request, "encyclopedia/error.html", {
            "title": title,
            "message": f"Requested Page {title} was not Found."
        })

    html_content = markdown2.markdown(markdown_content)

    return render(request, "encyclopedia/entry.html", {
        "title": title,
        "content": html_content
    })

def search(request):
    query = request.GET.get('q', '').strip()

    if query:
        markdown_content = util.get_entry(query)
        
        # အတိအကျတူရင် တန်းပြန်မယ်
        if markdown_content is not None:
            return redirect("wiki_entry", title=query)
        
        # အတိအကျမတူရင် တစ်စိတ်တပိုင်းတူတာ လိုက်ရှာမယ်
        all_entries = util.list_entries()
        results = [entry for entry in all_entries if query.lower() in entry.lower()]

        return render(request, "encyclopedia/search.html", {
            "results": results,
            "query": query
        })

        
    return redirect("index.html")

def new_page(request):
    if request.method == "POST":
        new_title = request.POST.get('title').strip()
        new_content = request.POST.get('content').strip()

        entry = util.list_entries()

        if new_title in entry:
            return render(request, "encyclopedia/error.html", {
                "title": new_title,
                "message": f"New Title You Created is exited one."
            })
        else:
            util.save_entry(new_title, new_content)
            return redirect("entry", title=new_title)

    return render(request, "encyclopedia/new_page.html")

def edit(request, title):
    if request.method == "POST":
        updated_content = request.POST.get('content').strip()
        util.save_entry(title, updated_content)
        return redirect("entry", title=title)
    else:
        markdown_content = util.get_entry(title)
        
        return render(request, "encyclopedia/edit_page.html", {
            "title": title,
            "content": markdown_content
        })
    
def random_page(request):
    entries = util.list_entries()

    selected_title = random.choice(entries)

    return redirect("wiki_entry", title=selected_title)



    
    
    

    