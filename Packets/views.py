from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import RegisterSerializer
from .models import User
from drf_yasg.utils import swagger_auto_schema



class RegisterView(APIView):
    @swagger_auto_schema(request_body=RegisterSerializer())
    def post(self, request):
        data = request.data
        serializer = RegisterSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response("Successfully registered", 201)

class ActivationView(APIView):
    def get(self, request, email, activation_code):
        user = User.objects.filter(email=email, activation_code=activation_code).first()
        if not user:
            return Response("User doesn't exist", 400)
        user.activation_code = ''
        user.is_active = True
        user.save()
        return Response('Activated', 200)
