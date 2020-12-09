from django.test import Client, TestCase
import json

class TestAccountCreate(TestCase):
    def test_account_create(self):
        #レスポンスでstatus_code:200とAccountCreateStatus:trueが返ってくるかどうか
        client = Client()
        test_account_create = {
            'user_id': 'test',
            'password': 'admin',
        }

        test_response = {
            "AccountCreateStatus": "true",
        }

        response = client.post('/api/account/create/', test_account_create)

        json_test_response = json.dumps(test_response, ensure_ascii=False, indent=2) 

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, json_test_response.encode(encoding='utf-8'))