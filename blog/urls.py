"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf import settings
from django import views
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from blogpost import views as blogpostViews
from rest_framework import routers
from blogpost.api import BlogpostSet


apiRouter = routers.DefaultRouter()
apiRouter.register(r'blogpost', BlogpostSet, 'Blogpost')
#apiRouter.register(r'user', UserDetail, 'User')

urlpatterns = [
    url(r'^$', blogpostViews.index,name='main'),
    url(r'^blog/(?P<slug>[^\.]+).html',blogpostViews.view_post, name='view_blog_post'),
    # url(r'^blog/(?P<slug>[^\.]+).html', 'blogpost.views.view_post', name='view_blog_post'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^pages/', include('django.contrib.flatpages.urls')),
    url(r'^comments/',include('django_comments.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/', include(apiRouter.urls))
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
