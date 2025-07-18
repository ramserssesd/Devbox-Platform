from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from .models import APIUsage
from .serializers import LoginSerializer, APIUsageSerializer, ProfileSerializer
import logging
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .serializers import LoginSerializer
from rest_framework.permissions import AllowAny
logger = logging.getLogger(__name__)

class LoginView(APIView):
    permission_classes = [AllowAny]
    @swagger_auto_schema(request_body=LoginSerializer)
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(**serializer.validated_data)
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=200)
        return Response({'error': 'Invalid credentials'}, status=401)

class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        data = {'username': request.user.username, 'email': request.user.email}
        return Response(ProfileSerializer(data).data)

class APIUsageView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        responses={200: APIUsageSerializer(many=True)}
    )
    def get(self, request):
        usage = APIUsage.objects.filter(user=request.user).order_by('-timestamp')
        return Response(APIUsageSerializer(usage, many=True).data)

    @swagger_auto_schema(
        request_body=APIUsageSerializer,
        responses={201: APIUsageSerializer}
    )
    def post(self, request):
        serializer = APIUsageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            logger.info(f"Kafka Event: {request.user.username} used {serializer.data['endpoint']}")
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
