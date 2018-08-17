from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'main'

# views.home = views.function
urlpatterns=[
 path('',views.home,name='home'),
 path('create/',views.create,name='create'),
 path('delete/',views.delete,name='delete'),
 path('update/',views.update,name='update'),
 path('read/',views.read,name='read')
]

