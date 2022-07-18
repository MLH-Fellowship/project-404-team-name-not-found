import os
import unittest
import os
os.environ['TESTING'] = 'true'

from app import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
    
    def test_home(self):
        response = self.client.get("/")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert "<title>MLH Fellow</title>" in html
        response2 = self.client.get("/static/img/smrithi.jpg")
        assert response2.status_code == 200

    def test_timeline(self):
        response = self.client.get("/api/timeline_post")
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert "timelineposts" in json
        assert len(json["timelineposts"]) == 0
        self.client.post("/api/timeline_post", data={"name": "Ashley", "email": "ashley@example.com", "content":"Hello my name is Ashley !"}, content_type='multipart/form-data')
        response = self.client.get("/api/timeline_post")
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        text = response.get_data(as_text=True)
        assert "Ashley" in text
        assert len(json["timelineposts"]) == 1
        response = self.client.get("/timeline")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert "Timeline" in html

    def test_malformed_timeline_post(self):
        # POST request missing name
        response = self.client.post("/api/timeline_post", data={"email": "ashley@example.com", "content":"Hello my name is Ashley !"}, content_type='multipart/form-data')
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid name" in html

        # POST request with empty content
        response = self.client.post("/api/timeline_post", data={"name": "Ashley", "email": "ashley@example.com", "content":""}, content_type='multipart/form-data')
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid content" in html

        # POST request with malformed email
        response = self.client.post("/api/timeline_post", data={"name": "Ashley", "email": "what's an email?", "content":"Hello my name is Ashley !"}, content_type='multipart/form-data')
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid email" in html



