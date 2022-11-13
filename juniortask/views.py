from rest_framework import mixins, viewsets
from juniortask.viewsets import CreateListRetrieveDestroyViewSet
from juniortask.models import  Note, Author
from juniortask.serializers import NoteDetailsSerializer
from rest_framework.response import Response
from django.http.response import JsonResponse,HttpResponse
from rest_framework import status

class NoteViewSet(CreateListRetrieveDestroyViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteDetailsSerializer
    lookup_field = 'pk'

    def list(self, request, *args, **kwargs):
        return super().list(request)

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request)

    def create(self, request, *args, **kwargs):
        return super().create( request)

    def destroy(self, request, **kwargs):
        super().destroy( request)
        return Response({'detail':'note successfuly deleted'},status=status.HTTP_204_NO_CONTENT)


note_list_view = NoteViewSet.as_view({'get': 'list'})
note_create_view = NoteViewSet.as_view({'post': 'create'})
note_detail_view = NoteViewSet.as_view({'get': 'retrieve'})
note_delete_view = NoteViewSet.as_view({'delete': 'destroy'}) 