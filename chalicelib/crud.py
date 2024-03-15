import os

import requests

from chalicelib import models


requests_session = requests.session()
requests_session.headers = {
	'Authorization': f"token {os.getenv('JUPITER_API_KEY')}:{os.getenv('JUPITER_API_SECRET')}",
	'Accept': 'application/json',
	'Content-Type': 'application/json',
}


def create_pqsrf(pqsrf_model: models.PQRSF) -> None:
	response = requests_session.post(
		f"{os.getenv('JUPITER_URL')}/api/resource/{os.getenv('JUPITER_PQSRF_RESOURCE_NAME')}",
		json=pqsrf_model.model_dump(exclude_none=True),
	)
	response.raise_for_status()
	return response.json().get('data')
