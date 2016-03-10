"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include,patterns
from django.contrib import admin
from django.views.generic import RedirectView 
from django.conf.urls.static import static  
from django.conf import settings 

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^polls/',include('polls.urls')),
    url(r'^bootstrap/',include('bootstrap.urls')),
    url(r'^$', RedirectView.as_view(url='/bootstrap/list/')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)       


'''
urlpatterns = patterns('',  
    (r'^bootstrap/', include('bootstrap.urls')),  
    (r'^$', RedirectView.as_view(url='/mysite/bootstrap/list/')), # Just for ease of use.  
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
'''
