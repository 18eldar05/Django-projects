from django.urls import path, re_path
from django.views.decorators.cache import cache_page

from .views import *

urlpatterns = [
    # path('', cache_page(60)(EstiemHome.as_view()), name='home'),
    path('', EstiemHome.as_view(), name='home'),
    path('about/', About.as_view(), name='about'),
    path('addpage/', AddPage.as_view(), name='add_page'),
    path('contact/', ContactFormView.as_view(), name='contact'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('event/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', EstiemCategory.as_view(), name='category'),
    # path('cats/<int:catid>/', categories),  # http://127.0.0.1:4000/cats/2/
    re_path(r'^archive/(?P<year>[0-9]{4})/', archive)
]
