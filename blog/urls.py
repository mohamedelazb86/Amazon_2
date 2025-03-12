from django.urls import path
from . import views
from . import api

app_name='blog'

urlpatterns = [
    
    
    path('',views.post_list,name='post-list'),
    path('update/<slug:slug>',views.update_post,name='update-post'),
    path('<slug:slug>',views.post_detail,name='post-detail'),
    path('<slug:slug>/delete',views.delete_post,name='delete-post'),

     # api
     path('postapi/api',api.PostApi.as_view()),
     path('postapi/<int:pk>',api.PostDetailApi.as_view()),

     path('api/post/api',api.postapiapi),

     path('api/api/api/<int:pk>',api.postall.as_view()),

     
    
]
