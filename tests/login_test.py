import logging
import os


# Test Login


def test_request_login(client,application):
    with application.app_context():
        log = logging.getLogger('login-log')
        response = client.get('/login')
        log.info("Test check")
        assert response.status_code == 200
        assert b"login" in response.data
        assert "Logged in"
