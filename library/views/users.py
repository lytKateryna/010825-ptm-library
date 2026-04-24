from rest_framework.generics import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from library.models import User
from library.serializers import UserSerializer
from library.permissions import IsAdminOnly
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action



class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminOnly]

    @action(detail=False, methods=['get'], url_path='me')
    def get_me(self, request, *args, **kwargs):
        # queryset = User.objects.filter(id=request.user.id).first() - first wariant
        obj = get_object_or_404(User, pk=request.user.id)
        serializer = self.get_serializer(obj)
        return Response(serializer.data, status.HTTP_200_OK)