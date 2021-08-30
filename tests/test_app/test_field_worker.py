from model_bakery import baker
import factory
import json
import pytest
from uuid import UUID

from app.models import FieldWorker


def validate_uuid4(uuid_string):
    try:
        val = UUID(uuid_string, version=4)
    except ValueError:
        return False
    return True


class TestFieldWorkerEndpoints:
    endpoint = '/v1/field-worker/'

    @pytest.mark.django_db
    def test_list(self, api_client):
        baker.make(FieldWorker, _quantity=3)
        response = api_client.get(
            self.endpoint
        )
        assert response.status_code == 200
        assert len(json.loads(response.content).get('results')) == 3

    @pytest.mark.django_db
    def test_create(self, api_client, fw):
        field_worker = fw(1)[0]
        expected_json = {
            'first_name': field_worker.first_name,
            'last_name': field_worker.last_name,
            'function': field_worker.function
        }

        response = api_client.post(
            self.endpoint,
            data=expected_json,
            format='json'
        )
        json_response = json.loads(response.content)
        id = json_response.pop('id')
        assert response.status_code == 201
        assert json_response == expected_json
        assert validate_uuid4(id) is True

    @pytest.mark.django_db
    def test_create_incompleted_data(self, api_client, fw):
        field_worker = fw(1)[0]
        expected_json = {
            'first_name': field_worker.first_name,
        }

        response = api_client.post(
            self.endpoint,
            data=expected_json,
            format='json'
        )
        assert response.status_code == 400
 
    @pytest.mark.django_db
    def test_update(self, rf, api_client, fw):
        old_field_worker = fw(1)[0]
        new_field_worker = fw(1)[0]
        field_worker_dict = {
            'first_name': new_field_worker.first_name,
            'last_name': new_field_worker.last_name,
            'function': new_field_worker.function
        } 

        url = f'{self.endpoint}{old_field_worker.id}/'

        response = api_client.patch(
            url,
            field_worker_dict,
            format='json'
        )
        json_response = json.loads(response.content)
        id = json_response.pop('id')
        assert response.status_code == 200
        assert json_response == field_worker_dict
        assert validate_uuid4(id) is True
        assert id == str(old_field_worker.id)

    @pytest.mark.django_db
    def test_cant_update_unknow_function(self, rf, api_client, fw):
        old_field_worker = fw(1)[0]
        field_worker_dict = {
            'function': 5
        } 

        url = f'{self.endpoint}{old_field_worker.id}/'

        response = api_client.patch(
            url,
            field_worker_dict,
            format='json'
        )
        assert response.status_code == 400

    @pytest.mark.django_db
    def test_delete(self, api_client, fw):
        field_worker = fw(1)[0]
        url = f'{self.endpoint}{field_worker.id}/'

        response = api_client.delete(url)

        assert response.status_code == 204
        assert FieldWorker.objects.all().count() == 0