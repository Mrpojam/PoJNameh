from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.core.paginator import Paginator
from .models import Article, Mail

from django_ratelimit.decorators import ratelimit

from services import send_email

def like_dislike_article(request, article_id):
    if request.method == 'POST':
        article = Article.objects.get(pk=article_id)
        action = request.POST.get('action')
        if action == 'like':
            article.likes += 1
        elif action == 'dislike':
            article.dislikes += 1
        article.save()
        return JsonResponse({'message': 'Action successful'})
    else:
        return JsonResponse({'error': 'Invalid request method'})

def article_details(request):
    articles_list = Article.objects.all()
    paginator = Paginator(articles_list, 5)  # Paginate articles with 5 per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'index.html', {'page_obj': page_obj})

@ratelimit(key='ip', rate='1/m', method='POST', block=True)
def send_mail(request):
    if request.method == 'POST':
        text = request.POST.get("text")

        if not text:
            return render(request, "Text field is required")
        
        mail = Mail(text=text)
        mail.save()
        send_email(text=text)
        return JsonResponse({'message':'Mail Sent'})
    return redirect({'message':'error happenned'})