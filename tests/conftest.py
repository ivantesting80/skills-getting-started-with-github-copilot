import copy
import pytest
from fastapi.testclient import TestClient

from src.app import app, activities as activities_dict


@pytest.fixture
def client():
    with TestClient(app) as c:
        yield c


@pytest.fixture(autouse=True)
def fresh_activities():
    """Restore the in-memory `activities` dict before/after each test."""
    original = copy.deepcopy(activities_dict)
    yield
    activities_dict.clear()
    activities_dict.update(copy.deepcopy(original))
