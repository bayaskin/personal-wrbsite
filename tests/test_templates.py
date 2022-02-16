import pytest
from ..myapp import app

@pytest.fixture
def test_client():
    flask_app = app.test_client()
    return flask_app

def test_home_page(test_client):
    """
    GIVEN a Flask application
    WHEN the '/' page is requested (GET)
    THEN check the response is valid
    """
    response = test_client.get('/')
    assert response.status_code == 200
    assert b'Bayaskhalan Tsyzhipov' in response.data

#def test_homepage_template(self):  
#    self.assert_template_used(self.response, 'home.html')
