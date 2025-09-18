from django.shortcuts import render
from articles.models import Article

def articles_list(request):
    template = 'articles/news.html'
    articles = Article.objects.prefetch_related('scopes__tag').all()
    for article in articles:
        article.scopes_sorted = sorted(
            article.scopes.all(),
            key=lambda s: (not s.is_main, s.tag.name.lower())
        )
    context = {
        'object_list': articles  # шаблон использует object_list
    }
    return render(request, template, context)
