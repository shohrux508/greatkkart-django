"""greatkart URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', views.home, name='home'),
                  path('store/', include('store.urls')),
                  path('cart/', include('carts.urls')),
                  path('login', views.login, name='login'),
                  path('register', views.register, name='register'),
                  path('dashboard', views.dashboard, name='dashboard'),
                  path('logout', views.logout, name='logout'),
                  path('submit', views.submit_review, name='submit_review'),
                  path('checkout', views.checkout, name='checkout'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
