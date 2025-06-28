from django.test import TestCase,Client;
from django.urls import reverse;
#from login.models Subjects, Student, Faculty
from login.views import home,login,logout,password;
import json;
import pytest
from django.conf import settings
from django.contrib.auth import get_user_model

pytest.mark.parametrize('param',[('home'),('login'),('password')])
User = get_user_model()
class TestViews(TestCase):
       def setUp(self):
           self.client=Client()
           self.home=reverse('home')
           self.login=reverse('login')
           self.logout=reverse('logout')
           self.marks=reverse('marks')
       def test_home(self):
           
           response=self.client.get(self.home)
           self.assertEquals(response.status_code,200)
           self.assertTemplateUsed(response,'home.html')
       def test_login(self):
           response=self.client.get(self.login)
           self.assertEquals(response.status_code,200)
           self.assertTemplateUsed(response,'login.html')
       def test_marks(self):
           response=self.client.get(self.marks)
           self.assertEquals(response.status_code,200)
           self.assertTemplateUsed(response,'login.html')

        
class UserTestCast(TestCase):

    def setUp(self): # Python's builtin unittest
        user_a = User(username='cfe', email='cfe@invalid.com')
        # User.objects.create()
        # User.objects.create_user()
        user_a_pw = 'some_123_password'
        self.user_a_pw = user_a_pw
        user_a.is_staff = True
        user_a.is_superuser = True
        user_a.set_password(user_a_pw)
        user_a.save()
        self.user_a = user_a
    
    def test_user_exists(self):
        user_count = User.objects.all().count()
        self.assertEqual(user_count, 1) # ==
        self.assertNotEqual(user_count, 0) # !=

    # def test_user_password(self):
    #     self.assertTrue(
    #         self.user_a.check_password(self.user_a_pw)
    #     )

    def test_user_password(self):
        user_a = User.objects.get(username="cfe")
        self.assertTrue(
            user_a.check_password(self.user_a_pw)
        )
    
    def test_login_url(self):
        # login_url = "/login/"
        # self.assertEqual(settings.LOGIN_URL, login_url)
        login_url = settings.LOGIN_URL
        # python requests - manage.py runserver
        # self.client.get, self.client.post
        # response = self.client.post(url, {}, follow=True)
        data = {"username": "cfe", "password": "some_123_password"}
        response = self.client.post(login_url, data, follow=True)
        # print(dir(response))
        # print(response.request)
        status_code = response.status_code
        redirect_path = response.request.get("PATH_INFO")
        self.assertEqual(redirect_path, '/accounts/login/')
        self.assertEqual(status_code,404 )