from rest_framework.test import APITestCase, APIRequestFactory, force_authenticate

from .models import User
from .views import RegistrationView, LoginView, ForgotPasswordView, ForgotPasswordCompleteView, ChangePasswordView, LogoutView



class UserTest(APITestCase):
    
    def setUp(self):
        self.factory = APIRequestFactory()
        self.user = User.objects.create_user(email='jykymyrza@gmail.com', password='1234', is_active=True)

    def test_register(self):
        data = {'email': 'new_user@gmail.com', 'password':'1234', 'password_confirm':'1234', 'name':'whoiam', 'phone_number':'1234567891234'}
        request = self.factory.post('register/', data, format='json')
        view = RegistrationView.as_view()
        responce = view(request)
        assert responce.status_code == 201
        assert User.objects.filter(email=data['email']).exists()

    def test_login(self):
        data = {'email':'jykymyrza@gmail.com', 'password':'1234'}
        request = self.factory.post('login/', data, format='json')
        view = LoginView.as_view()
        responce = view(request)
        # print(responce.data)
        assert responce.status_code == 200
        assert 'token' in responce.data

    def test_change_password(self):
        data = {'old_password':'1234', 'new_password':'9876', 'new_password_confirm':'9876'}
        request = self.factory.post('change_password/', data, format='json')
        force_authenticate(request, user=self.user)
        view = ChangePasswordView.as_view()
        responce = view(request)
        assert responce.status_code == 200

    def test_forgot_password(self):
        data = {'email':'jykymyrza@gmail.com'}
        request = self.factory.post('forgot_password/', data, format='json')
        view = ForgotPasswordView.as_view()
        responce = view(request)
        # print(responce.data)
        assert responce.status_code == 200

    def test_forgot_password_complete(self):
        data = {'code':request, 'email':'jykymyrza@gmail.com', 'password1':'1234','password2':'1234'}
        request = self.factory.post('forgot_password_complete/', data=data, format='json')

        
        
    def test_log_out(self):
        request = self.factory.post('log_out/', format='json')
        force_authenticate(request, user=self.user)
        view = LogoutView.as_view()
        responce = view(request)
        assert responce.status_code == 200