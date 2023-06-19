from django.contrib.auth.models import User

from django.contrib.auth import get_user_model,authenticate, login, logout
UserModel = get_user_model()
UserModel.objects.create_user(
    username='test',
    password='test',
    email='test'
)
print(1)