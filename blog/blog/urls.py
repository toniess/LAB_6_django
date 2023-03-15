from django.contrib import admin
from django.urls import path, re_path
from articles import views
from django.contrib.auth import views as authViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.archive, name='home'),
    path('article/new', views.create_post, name='new_post'),
    path('registration/', views.registration, name='registration'),
    path('authorisation/', views.authorisation, name='authorisation'),
    re_path(r'^article/(?P<article_id>\d+)$', views.get_article, name='get_article'),
    path('exit/', authViews.LogoutView.as_view(next_page='/'), name='exit'),
]
