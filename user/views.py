from rest_framework import viewsets
from user.serializers import UserSerializer
from user.models import User

# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
