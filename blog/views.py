from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import Article
from .forms import ArticleAddForm
from django.utils.text import slugify
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def allarticles(request):
    art_list = Article.pub_status.all()
    paginator = Paginator(art_list, 3)  # 3 Article per page 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj}
    return render(request, 'blog/arts.html', context)


def art_detail(request, user_id, slug):
    article = get_object_or_404(Article, id=user_id, slug=slug)
    context = {'arts': article}
    return render(request, 'blog/art_detail.html', context)


@login_required
def add_article(request, user_id):
    if request.method =='POST':
        form = ArticleAddForm(request.POST)
        if form.is_valid():
            new_article = form.save(commit=False)
            new_article.slug = slugify(form.cleaned_data['title'][:30], allow_unicode=True)
            new_article.publisher = request.user
            new_article.save()
            messages.success(request, 'Article added and wil be shown after being accepted', 'success')
            return redirect('blog:allArticles')

    else:
        form = ArticleAddForm()
    return render(request, 'blog/add_post.html', {'form': form})






