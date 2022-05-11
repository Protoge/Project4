import logging
# Test Register
def test_request_register(client,application):
    with application.app_context():
        response = client.get('/register')
        log = logging.getLogger('register-log')
        log.info("Register check")
        assert response.status_code == 200
        assert b'register' in response.data
        assert "Test check"