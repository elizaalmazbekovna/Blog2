from django.urls import path

from Blog import views
from untitled6 import settings
from django.conf.urls.static import static

urlpatterns =[
    path('',views.Blog_view),
    path('random/',views.random_view),
    path('form/',views.test_form),

]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + \
              static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)