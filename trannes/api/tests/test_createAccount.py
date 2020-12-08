from django.test import Client, TestCase
import json

class createAccountTest(TestCase):
    def test_createAccount(self):
        client = Client()
        response = client.post('/api/createAccount/', {'user_id': 'test', 'password': 'admin'})

        test_response = {
            "createAccountResult": "true",
        }

        json_test_response = json.dumps(test_response, ensure_ascii=False, indent=2) 

        self.assertEqual(response.status_code, 200)
        print(response.content)
        self.assertEqual(response.content, json_test_response.encode(encoding='utf-8'))