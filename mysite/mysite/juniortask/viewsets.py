from rest_framework import mixins, viewsets
#custom viewset to shorten the name and hide all inheritances
class CreateListRetrieveDestroyViewSet(
        mixins.ListModelMixin,
        mixins.CreateModelMixin,
        mixins.RetrieveModelMixin,
        mixins.DestroyModelMixin,
        viewsets.GenericViewSet):
        
        pass