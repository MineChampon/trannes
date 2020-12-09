from django.test import Client, RequestFactory, TestCase

# Create your tests here.

class loginTests(TestCase):
    def test_bad_maths(self):
        self.assertEqual(1+1, 2)  # 失敗