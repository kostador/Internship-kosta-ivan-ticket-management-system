from rest_framework import generics
from .models import User
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.throttling import ScopedRateThrottle
from rest_framework.permissions import IsAuthenticated,AllowAny

class RegisterView(generics.CreateAPIView):

    queryset = User.objects.all()

    serializer_class = UserSerializer

    permission_classes = []

    authentication_classes = []

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self,request):
        Token.objects.filter(user=request.user).delete()

        return Response({"detail":"Successfully logged out."},
                        status=status.HTTP_200_OK
                        )

class LoginView(ObtainAuthToken):
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'login'