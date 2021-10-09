from django.conf.urls import url 
from .import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path


urlpatterns = [
    # url('^$',views.welcome,name = 'welcome'),
    url(r'^search/', views.search, name='search_results'),
    # url(r'^image/(\d+)',views.image,name ='image'),
    # path('category/<str:category_name>',views.image, name="image"),
    # url(r'^location',views.location,name='location'),
    # path('home/',getHomePage),
    url(r'^$',views.welcome,name='index'),
    # url(r'^search/',views.search,name='search_results'),
    # url(r'^images/(\d+)',views.image,name='image'),
    url(r'^location/',views.location,name='location'),
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)