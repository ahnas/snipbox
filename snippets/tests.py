import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Snippet

@pytest.mark.django_db
class TestSnippetDetailView:
    def test_get_snippet_success(self, client, snippet_factory):
        snippet = snippet_factory()
        url = reverse('snippet-detail', kwargs={'pk': snippet.pk})
        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert response.data['id'] == snippet.pk
        assert response.data['title'] == snippet.title
        assert response.data['code'] == snippet.code

    def test_get_snippet_failure(self, client):
        url = reverse('snippet-detail', kwargs={'pk': 999})
        response = client.get(url)
        assert response.status_code == status.HTTP_404_NOT_FOUND

    def test_update_snippet_success(self, client, snippet_factory):
        snippet = snippet_factory()
        url = reverse('snippet-detail', kwargs={'pk': snippet.pk})
        data = {'title': 'New title', 'code': 'New code'}
        response = client.put(url, data, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert response.data['id'] == snippet.pk
        assert response.data['title'] == 'New title'
        assert response.data['code'] == 'New code'

    def test_update_snippet_failure(self, client, snippet_factory):
        snippet = snippet_factory()
        url = reverse('snippet-detail', kwargs={'pk': snippet.pk})
        data = {'title': '', 'code': ''} 
        response = client.put(url, data, format='json')
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_delete_snippet_success(self, client, snippet_factory):
        snippet = snippet_factory()
        url = reverse('snippet-detail', kwargs={'pk': snippet.pk})
        response = client.delete(url)
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert not Snippet.objects.filter(pk=snippet.pk).exists()

    def test_delete_snippet_failure(self, client):
        url = reverse('snippet-detail', kwargs={'pk': 999})
        response = client.delete(url)
        assert response.status_code == status.HTTP_404_NOT_FOUND