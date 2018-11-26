"""Blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import urls as auth_urls
from django.views.generic import TemplateView

from Blog import settings
from Post.views import index as post_index
from Post.views import detail as post_detail
from Post.views import create as post_create
from Post.views import search as post_search
from Comment.views import create as comment_create
from Rating.views import rating_create
from Auth.views import SignUpView

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html')),
    path('admin/', admin.site.urls),
    path('user/', include(auth_urls)),
    path('user/register/', SignUpView.as_view()),
    path('post/', post_index, name='post_index'),
    path('post/<int:request_post_id>', post_detail, name='post_detail'),
    path('post/search/', post_search, name='post_search'),
    path('comment/create/<int:post_id>', comment_create, name='comment_create'),
    path('rating/create/<int:post_id>', rating_create, name='rating_create'),
    path('post/create', post_create, name='post_create')
] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
