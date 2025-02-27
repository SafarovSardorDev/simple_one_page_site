from django.shortcuts import render, redirect
from .models import News
from django.http import HttpResponse
from .forms import NewsForm
# Create your views here.

def home(request):
    news = News.objects.filter(is_active=True)
    
    context = {
        "news" : news
    }

    return render(request, "home.html", context)

def new_detail(request, id):
    new = News.objects.get(id=id)
    news = News.objects.filter(is_active=True)
    context = {
        "new" : new,
        "news" : news
    }
    return render(request, 'detail.html', context)

def new_create(request):
    user = request.user
    if user.is_authenticated:
        form = NewsForm()
        if request.method == 'POST':
            form = NewsForm(data = request.POST)
            if form.is_valid():
                new = form.save(commit=False)
                new.author = user
                form.save(commit=True)
                return redirect('home')
            else:
                return render(request, 'create.html', {"form":form})
        else:
            return render(request, 'create.html', {"form":form})
    else:
        return HttpResponse("Not allowed bro")
    
def new_update(request, id):
    user = request.user
    new = News.objects.get(id=id)
    if user == new.author:
        form = NewsForm(instance=new)
        if request.method == "POST":
            form = NewsForm(instance=new, data=request.POST)
            if form.is_valid():
                form.save()
                # return HttpResponse("OK")
                return redirect('home') #iloji bo'lsa new_detailni o'ziga yuborish kk, lekin o'xshamadi
            else:
                return render(request, 'update.html', {"form": form, "new":new})
        else:
            return render(request, 'update.html', {"form": form, "new":new})
    else:
        return HttpResponse("Not allowed bro")
    
def new_delete(request, id):
    user = request.user
    new = News.objects.get(id=id)
    if user == new.author:
        if request.method == "POST":
            new.delete()
            return redirect('home')
        return render(request, "delete.html", {"new":new})
    else:
        return HttpResponse("Not allowed bro")



