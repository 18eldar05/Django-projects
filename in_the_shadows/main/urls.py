from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='Main.html'),
    path('tour', views.concerts, name='Concerts.html'),
    path('stay_in_touch', views.contacts, name='Contacts.html'),
    path('info', views.about, name='Bout_us.html'),
    path('saint-petersburg', views.piter, name='Product_page_Piter.html')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
