from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from django.urls import reverse
from .views import upload_file


class ViewsTestCase(TestCase):
    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_form_view(self):
        response = self.client.get(reverse('form'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'form.html')

    def test_submitted_view(self):
        response = self.client.get(reverse('submitted'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'submitted.html')

    def test_contact_view(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')

    def test_about_view(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')

    def test_honor_view(self):
        response = self.client.get(reverse('honor'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'honor.html')

    def test_adminpanel_view(self):
        response = self.client.get(reverse('adminpanel'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'adminpanel.html')

    def test_myReports_view(self):
        response = self.client.get(reverse('myReports'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'myReports.html')

    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='secret')

    def test_upload_file_view(self):
        request = self.factory.post('/upload/', {'title': 'Test Title', 'file': 'test_file.txt'})
        request.user = self.user  # Assign user to the request
        response = upload_file(request)
        self.assertEqual(response.status_code, 200)
