from django.urls import path
from . import views
from .views import (
    MembersApiView,
    MembersDetailApiView,
)


urlpatterns = [
  path('', views.index, name='index'),
  path('add/', views.add, name='add'),
  path('add/addrecord/', views.addrecord, name='addrecord'),
  path('delete/<int:id>', views.delete, name='delete'),
  path('update/<int:id>', views.update, name='update'),
  path('update/updaterecord/<int:id>', views.updaterecord, name='updaterecord'),
  path('api/', MembersApiView.as_view()),
  path('api/<int:todo_id>/', MembersDetailApiView.as_view()),
]