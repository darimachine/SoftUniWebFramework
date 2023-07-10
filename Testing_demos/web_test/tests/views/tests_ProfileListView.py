from django.contrib.auth import login, get_user_model
from django.test import TestCase
from django.urls import reverse

from web_test.models import Profile
from web_test.views import ProfileListView

UserModel=get_user_model()
class ProfilesListViewTest(TestCase):

    def test_get__expect_correct_template(self):
        response = self.client.get(reverse('profile list'))
        self.assertTemplateUsed(response, 'profile/list.html')
        #self.assertEqual(response.status_code,200)
    def test_get__when_two_profiles__expect_context_to_contain_two_profile(self):
        profiles_to_create=(
            {'first_name': 'Serhan', 'last_name': 'Aydin', 'age': 20},
            {'first_name': 'Dari', 'last_name': 'Beba', 'age': 21},
        )
        for profile in profiles_to_create:
            #Profile.objects.create(**profile)
            self.client.post(reverse('profile create'), profile)  #trqbvda da ima forma s create profile view
        #second -------------------
        # profiles_to_create2=(
        #     Profile(first_name='Serhan', last_name='Aydin', age=20),
        #     Profile(first_name='Dari', last_name='Beba', age=21),
        # )
        # Profile.objects.bulk_create(profiles_to_create2)
        response = self.client.get(reverse('profile list'))
        profiles = response.context['object_list']
        self.assertEqual(len(profiles),2)

    def test_get__when_not_logged_in_user__expect_context_user_to_be_NoUser(self):
        response = self.client.get(reverse('profile list'))
        self.assertEqual(response.context['user'],'No User')
    def test_get__when_user_is_logged_in__except_context_user_to_be_his_Username(self):
        user_data = {
            'username': 'serhan2',
            'password': '123456',
        }
        UserModel.objects.create_user(**user_data)
        self.client.login(**user_data)
        response = self.client.get(reverse('profile list'))
        self.assertEqual(user_data['username'],response.context['user'])