from django.test import TestCase, Client
from suggestions.models import DummyModel, SecondDummyModel
from .models import ObjectView, ObjectViewDictionary
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


class SuggestionsTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        User.objects.create_user(username='johndoe', password='123456')
        self.client.login(username='johndoe', password='123456')
        DummyModel.objects.create(name="Test")
        DummyModel.objects.create(name="Test2")
        SecondDummyModel.objects.create(name="Test2")

    def test_ensure_object_view_updated(self):
        init_view_count = ObjectView.objects.all().count()
        response = self.client.get(
            reverse('dummy-detail', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(ObjectView.objects.all().count(), init_view_count + 1)

    def test_ensure_dictionary_created(self):
        init_view_count = ObjectView.objects.all().count()
        response = self.client.get(
            reverse('dummy-detail', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)
        response = self.client.get(
            reverse('dummy-detail', kwargs={'pk': 2}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(ObjectView.objects.all().count(), init_view_count + 2)
        self.assertEqual(ObjectViewDictionary.objects.all().count(), 1)

    def test_ensure_dictionary_updated(self):
        init_view_count = ObjectView.objects.all().count()
        response = self.client.get(
            reverse('dummy-detail', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)
        response = self.client.get(
            reverse('dummy-detail', kwargs={'pk': 2}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(ObjectView.objects.all().count(), init_view_count + 2)
        self.assertEqual(ObjectViewDictionary.objects.all().count(), 2)
        response = self.client.get(
            reverse('dummy-detail', kwargs={'pk': 2}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(ObjectViewDictionary.objects.all().count(), 2)
        view_count = ObjectViewDictionary.objects.get(
            current_object_id=2).visits
        self.assertEqual(view_count, 2)

    def test_ensure_dictionary_not_created(self):
        init_dictionary_count = ObjectViewDictionary.objects.all().count()
        response = self.client.get(
            reverse('dummy-detail', kwargs={'pk': 1}))
        response = self.client.get(
            reverse('dummy2-detail', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            ObjectViewDictionary.objects.all().count(),
            init_dictionary_count)
