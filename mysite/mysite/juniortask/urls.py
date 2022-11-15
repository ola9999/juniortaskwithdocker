from rest_framework.routers import DefaultRouter
from juniortask.views import * 
from django.urls import path, include

#if you want to use default django routers urls you can use DefaultRouter().register('notes', NoteViewSet, basename='notes')

urlpatterns = [
        path('notes/list/',             note_list_view,         name='note_list' ),
        path('notes/add/',              note_create_view,       name='note_create' ),
        path('notes/get/<int:pk>',      note_detail_view,       name='note_detail'),
        path('notes/delete/<int:pk>',   note_delete_view,       name = 'note_delete'),
        ]