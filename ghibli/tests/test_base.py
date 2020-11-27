"""
Test Base
"""

from fastapi.testclient import TestClient
from ghibli.main import app

client = TestClient(app)
