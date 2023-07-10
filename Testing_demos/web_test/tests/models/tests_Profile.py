from xml.dom import ValidationErr

from django.core.exceptions import ValidationError
from django.test import TestCase

from web_test.models import Profile


class ProfileTests(TestCase):
    VALID_USER_DATA = {
        'first_name': 'Serhan',
        'last_name': 'Yılmaz',
        'age': 15
    }
    def test_profile_create__whenFirstNameContainsOnlyLetters_ExpectSucces(self):

        profile = Profile(
            **self.VALID_USER_DATA,
        )
        profile.save()
        self.assertIsNotNone(profile.pk)
    def test_profile_create__WhenFirstNameContainsDigit_ExpectToFail(self):
        first_name = 'Ser21han'
        profile = Profile(
            first_name=first_name,
            last_name= 'Yılmaz',
            age= 15,
        )
        with self.assertRaises(ValidationError) as context:
            profile.full_clean()
            profile.save()
        self.assertIsNotNone(context.exception)

    def test_profile_create__WhenFirstNameContainsDolar_ExpectToFail(self):
        first_name = 'Ser$han'
        profile = Profile(
            first_name=first_name,
            last_name='Yılmaz',
            age=15,
        )
        with self.assertRaises(ValidationError) as context:
            profile.full_clean()
            profile.save()
        self.assertIsNotNone(context.exception)
    def test_profile_create__WhenFirstNameContainsSpace_ExpectToFail(self):
        first_name = 'Ser han'
        profile = Profile(
            first_name=first_name,
            last_name='Yılmaz',
            age=15,
        )
        with self.assertRaises(ValidationError) as context:
            profile.full_clean()
            profile.save()
        self.assertIsNotNone(context.exception)

    def test_profile_FullName__WhenValid_ExpectCorrectFullName(self):
        profile = Profile(
            first_name="Serhan",
            last_name="Yılmaz",
            age=15,
        )
        self.assertEquals(profile.full_name, "Serhan Yılmaz")
