from django.shortcuts import render, redirect, get_object_or_404, reverse
from .models import Article
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from .import forms

# Create your views here.
def article_list(request):
    articles = Article.objects.all().order_by('-date')
    #consider ordering by another parameter I.E.: "importance"
    return render(request, 'articles/article_list.html',{'articles' : articles})

def article_detail(request, slug):
    #article = Article.objects.get(id=slug)
    article = get_object_or_404(Article,id = slug)
    return render(request, 'articles/article_detail.html',{'article':article})

def article_list_theme(request, theme):
    articles = Article.objects.filter(theme=theme).order_by('-date')
    return render(request, 'articles/article_list.html',{'articles' : articles})

@login_required(login_url='/accounts/login/')
def article_create(request):
    if request.method == 'POST':
        form =forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            # from_email = settings.EMAIL_HOST_USER
            # send_mail('test subject',
            #         'text testas',
            #          from_email,
            #          ['elijaszaremba@gmail.com'],
            #          fail_silently=True)
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('articles:list')
    else:
        form = forms.CreateArticle()

    return render(request,'articles/article_create.html',{'form':form})

@login_required(login_url='/accounts/login/')
def article_list_private(request):
    author= request.user
    articles = Article.objects.filter(author=author).order_by('date')
    return render(request, 'articles/article_private_list.html',{'articles' : articles})

@login_required(login_url='/accounts/login/')
def article_update(request, id): #make sure that person can only edit his own
    article = Article.objects.get(id=id)
    form = forms.CreateArticle(request.POST or None, instance=article)
    if form.is_valid():
        form.save()
        return redirect('articles:list')

    return render(request,'articles/article_create.html',{'form':form,'Article':article})

@login_required(login_url='/accounts/login/')
def article_delete(request, id):#make sure that person can only edit his own
    article = Article.objects.get(id=id)
    if request.method=='POST':
        print("this fried")
        article.active = False
        article.save()
        return redirect('articles:list')
    return render(request,'articles/article_delete_confirm.html',{'Article':article})
