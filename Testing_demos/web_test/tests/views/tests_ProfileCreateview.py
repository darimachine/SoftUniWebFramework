from django.test import TestCase
from django.urls import reverse

from web_test.models import Profile


class ProfileCreateViewTest(TestCase):
    def test_create_profile_when_everything_is_valid(self):
        profile_data = {
            'first_name': 'Serhan',
            'last_name': 'Aydin',
            'age': 20,
        }
        self.client.post(
            reverse('profile create'),
            data=profile_data
        )
        profile = Profile.objects.first()
        self.assertIsNotNone(profile)

        self.assertEqual(profile.first_name, profile_data['first_name'])

    def test_redirect_profile_when_profile_is_created(self):
        profile_data = {
            'first_name': 'Serhan',
            'last_name': 'Aydin',
            'age': 20,
        }
        response = self.client.post(
            reverse('profile create'),
            data=profile_data
        )
        profile = Profile.objects.first()
        self.assertRedirects(response, reverse('profile details', kwargs={'pk': profile.pk}))

