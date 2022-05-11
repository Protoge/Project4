import logging
from flask_login import current_user,login_required
from flask import Blueprint


auth = Blueprint('auth', __name__, template_folder='templates')

def test_dashboard_request(client, application):
    with application.app_context():
        response = client.get('/dashboard')
        log = logging.getLogger('transaction-log')
        log.info('Dashboard check')
        assert response.status_code == 302
        assert b"dashboard" in response.data
        assert "User is authenticated"
        assert "User is not authenticated"
