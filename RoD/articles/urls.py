
from django.urls import path
from django.conf.urls.static import static
from django.conf.urls import url
from . import views
app_name = 'articles'
urlpatterns = [
    url(r'^$',views.article_list, name= 'list'),
    url(r'create/$',views.article_create, name='create'),
    url(r'private/$',views.article_list_private,name='private_list'),
    path('edit/<int:id>/',views.article_update, name = 'update'),
    path('delete/<int:id>/',views.article_delete, name='delete'),
    path('theme/<str:theme>/', views.article_list_theme, name='theme_list'),
    #url(r'^edit/(?P<slug>\d+)/$',views.article_update, name = 'update'),
    url(r'^(?P<slug>[\w-]+)/$',views.article_detail, name = 'detail'), #this should always be in bottom (ACL logic applied)
]
