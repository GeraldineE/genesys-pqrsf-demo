import json

import chalice.test

from app import app


def test_index():
	with chalice.test.Client(app) as client:
		result = client.http.get('/')
		assert result.json_body == {'Data': 'Welcome to PQSRF API'}


def test_pqrsf_create_success():
	with chalice.test.Client(app) as client:
		result = client.http.post('/pqrsfs', body=json.dumps({}))
		pass


def test_pqrsf_create_validation_error():
	with chalice.test.Client(app) as client:
		result = client.http.post('/pqrsfs', body=json.dumps({}))
		pass


def test_pqrsf_create_api_validation_error():
	with chalice.test.Client(app) as client:
		result = client.http.post('/pqrsfs', body=json.dumps({}))
		pass


def test_pqrsf_create_api_unauthorized_error():
	with chalice.test.Client(app) as client:
		result = client.http.post('/pqrsfs', body=json.dumps({}))
		pass


def test_pqrsf_create_api_forbidden_error():
	with chalice.test.Client(app) as client:
		result = client.http.post('/pqrsfs', body=json.dumps({}))
		pass
