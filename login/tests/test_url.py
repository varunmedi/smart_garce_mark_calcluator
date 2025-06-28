from login.views import home,login,logout,password;
from django.test import SimpleTestCase;
from django.urls import reverse,resolve;

class BasicTest(SimpleTestCase):
    def test_fields(self):
           url=reverse('home')
           print(resolve(url))
           self.assertEquals(resolve(url).func,home)

    def test_login(self):
           url=reverse('login')
           print(resolve(url))
           self.assertEquals(resolve(url).func,login)
    def test_password(self):
           url=reverse('password')
           print(resolve(url))
           self.assertEquals(resolve(url).func,password)

    def test_logout(self):
           url=reverse('logout')
           print(resolve(url))
           self.assertEquals(resolve(url).func,logout)



