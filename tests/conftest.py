import pytest
from model_bakery import baker
import uuid
from app.models import FieldWorker

@pytest.fixture
def api_client():
   from rest_framework.test import APIClient
   return APIClient()


@pytest.fixture
def fw():
    def field_worker(n):
        fw = baker.make(
            FieldWorker,
            id=uuid.uuid4(),
            _quantity=n
        )
        return fw
    return field_worker