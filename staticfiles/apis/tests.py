from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from books.models import Book

# Extend the APITestCase 
class APITests(APITestCase):
    @classmethod
    #Configure stuff by setting up startup data :
    def setUpTestData(cls):
        cls.book = Book.objects.create(
        title="Django for APIs",
        subtitle="Build web APIs with Python and Django",
        author="William S. Vincent",
        isbn="9781735467221",
        )

    def test_api_listview(self):
        # First check that the named url "book_list" is being used :
        response = self.client.get(reverse("book_list"))

        # Second we confirm that the HTTP status code matches 200
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Thirdly check that we hae only a single book entry (the one we ceated):
        self.assertEqual(Book.objects.count(), 1)

        # finally , confirm that the response contains all the data 
        # from our created book object
        self.assertContains(response, self.book)