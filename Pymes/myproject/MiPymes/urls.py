from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include

urlpatterns = [
    path('',views.vistaIndex, name='inicio'),
    path('login/',views.vistaLogin, name='login'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)