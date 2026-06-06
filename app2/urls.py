
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('delete/<int:id>',views.delete_task,name='delete'),
    path('update/<int:id>',views.update_task,name='update'),
]
