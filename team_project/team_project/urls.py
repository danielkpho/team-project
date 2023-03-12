from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
# from homepage import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.authtoken')),
    # path('homepage/', views.homepage),
    # path('vue-homepage/', views.vue_homepage),
    path('api/v1/', include('events.urls')),
    path('', include('events.urls')),
    # path('homepage', include('homepage.urls')),
] 
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


