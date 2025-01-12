from django.test import TestCase

# Create your tests here.

from rest_framework.test import APITestCase
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile

class CSVUploadTests(APITestCase):
    def test_csv_upload(self):
        csv_file = SimpleUploadedFile(
            "test.csv", b"name,email,age\nJohn Doe,john@example.com,30\nNone,email@gmail.com,23\nJoseph Stal,john@example.com,23",
            content_type="text/csv"
        )
        response = self.client.post(reverse('csv-upload'), {'file': csv_file })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['total_succesfuly_saved'], 1)
        self.assertEqual(response.data['rejected_datas'], 2)
        self.assertEqual(response.data['errors'], [
            {
            "data": {
                "name": None,
                "email": "email@gmail.com",
                "age": 23
            },
            "errors": {
                "name": [
                    "This field may not be null."
                ]
            }
        },
        {
            "data": {
                "name": "Joseph Stal",
                "email": "john@example.com",
                "age": 23
            },
            "errors": {
                "email": [
                    "Email already exists."
                ]
            }
        }

        ])
    
    # def test_name_as_null(self):
    #     csv_file = SimpleUploadedFile(
    #         "test.csv", b"name,email,age\nNone,email@gmail.com,23",
    #         content_type="text/csv"
    #     )
    #     response = self.client.post(reverse('csv-upload'), {'file': csv_file })
    #     self.assertEqual(response.status_code, 201)
    #     self.assertEqual(response.data['total_succesfuly_saved'], 0)
    #     self.assertEqual(response.data['rejected_datas'], 1)
    #     self.assertEqual(response.data['errors'], [
    #     {
    #         "data": {
    #             "name": None,
    #             "email": "email@gmail.com",
    #             "age": 23
    #         },
    #         "errors": {
    #             "name": [
    #                 "This field may not be null."
    #             ]
    #         }
    #     }
    # ])
        
    # def test_duplicate_email(self):
    #     csv_file = SimpleUploadedFile(
    #         "test.csv", b"name,email,age\nJoseph Stal,john@example.com,23",
    #         content_type="text/csv"
    #     )
    #     response = self.client.post(reverse('csv-upload'), {'file': csv_file })
    #     self.assertEqual(response.status_code, 201)
    #     self.assertEqual(response.data['total_succesfuly_saved'], 0)
    #     self.assertEqual(response.data['rejected_datas'], 1)
    #     self.assertEqual(response.data['errors'], [
    #     {
    #         "data": {
    #             "name": "Joseph Stal",
    #             "email": "john@example.com",
    #             "age": 23
    #         },
    #         "errors": {
    #             "email": [
    #                 "Email already exists."
    #             ]
    #         }
    #     }
    # ])
        
    def test_invalid_age(self):
        csv_file = SimpleUploadedFile(
            "test.csv", b"name,email,age\nMike,mike@gmail.com,150",
            content_type="text/csv"
        )
        response = self.client.post(reverse('csv-upload'), {'file': csv_file })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['total_succesfuly_saved'], 0)
        self.assertEqual(response.data['rejected_datas'], 1)
        self.assertEqual(response.data['errors'], [
        {
            "data": {
                "name": "Mike",
                "email": "mike@gmail.com",
                "age": 150
            },
            "errors": {
                "age": [
                    "Age must be between 0 and 120."
                ]
            }
        }
    ])
        
    def test_invalid_email(self):
        csv_file = SimpleUploadedFile(
            "test.csv", b"name,email,age\nhenry,henry,28",
            content_type="text/csv"
        )
        response = self.client.post(reverse('csv-upload'), {'file': csv_file })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['total_succesfuly_saved'], 0)
        self.assertEqual(response.data['rejected_datas'], 1)
        self.assertEqual(response.data['errors'], [
        {
            "data": {
                "name": "henry",
                "email": "henry",
                "age": 28
            },
            "errors": {
                "email": [
                    "Enter a valid email address.",
                    "Enter a valid email address."
                ]
            }
        }
    ])

    def test_other_file(self):
        xlxs_file = SimpleUploadedFile(
                "test.xlxs", b"name,email,age\nJohn Doe,john@example.com,30",
                content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
        response = self.client.post(reverse('csv-upload'), {'file': xlxs_file })
        self.assertEqual(response.data, {
        "error": "File must be a CSV."
            })