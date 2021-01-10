
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .import views
from django.contrib.sitemaps.views import sitemap

from blog.sitemaps import StaticViewsSitemap
from blog.sitemaps import BlogSitemap

sitemaps ={
    'blogpost': BlogSitemap(),
    'static': StaticViewsSitemap(),
}



urlpatterns = [
    path('admin/', admin.site.urls),
    path('shop/', include('shop.urls')),
    path('blog/', include('blog.urls')),
    path('', views.index),
    path('register/', views.registerPage),
    path('login/', views.loginPage),
    path('logout/', views.logoutUser),
    path('sitemap.xml/', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
