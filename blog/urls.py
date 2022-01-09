from django.urls import path
from . import views


app_name = 'blog'
urlpatterns = [
    path('', views.allarticles, name="allArticles"),
    path('<int:user_id>/<slug:slug>/', views.art_detail, name='article_detail'),
    path('add_article/<int:user_id>/', views.add_article, name='add_article'),

]


