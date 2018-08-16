from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'home'

# views.home = views.function
urlpatterns=[
 path('',views.home,name='home'), 
]

# urlpatterns=[
#  path('',views.home,name='home'),
# ] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)