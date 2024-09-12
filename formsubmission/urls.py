from django.urls import path
from .views import index
from django.conf.urls.static import static
from . import views  # Import views from the current app
from django.conf import settings


urlpatterns = [
    path('', views.index, name='index'),
    
   
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)