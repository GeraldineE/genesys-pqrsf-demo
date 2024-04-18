import os
import uuid

import requests

from chalicelib import models
from chalicelib import helpers

requests_session = requests.session()
requests_session.headers = {
	'Authorization': f"token {os.getenv('JUPITER_API_KEY')}:{os.getenv('JUPITER_API_SECRET')}",
	'Accept': 'application/json',
	'Content-Type': 'application/json',
}

file_requests_session = requests.session()
requests_session.headers = {
	'Authorization': f"token {os.getenv('JUPITER_API_KEY')}:{os.getenv('JUPITER_API_SECRET')}",
	'Accept': 'application/json',
}


def create_pqsrf(pqsrf_model: models.PQRSF) -> None:
	payload = pqsrf_model.model_dump(exclude=['evidencias'], exclude_none=True)
	pqsrf_response = requests_session.post(
		f"{os.getenv('JUPITER_URL')}/api/resource/{os.getenv('JUPITER_PQSRF_RESOURCE_NAME')}",
		json=payload,
	)
	pqsrf_response.raise_for_status()
	pqsrf = pqsrf_response.json().get('data')
	evidences_count = 3
	if pqsrf_model.evidencias:
		for index, evidence_data_uri in enumerate(pqsrf_model.evidencias[:evidences_count], 1):
			try:
				evidence_bytes = helpers.data_uri_to_bytes(evidence_data_uri)
				evidence_attachment_response = file_requests_session.post(
					f"{os.getenv('JUPITER_URL')}/api/method/upload_file",
					data={
						'is_private': 0,
						'folder': 'Home',
						'doctype': pqsrf.get('doctype'),
						'docname': pqsrf.get('name'),
						'fieldname': f'evidencias{index}',
					},
					files={'file': (f'attach-{uuid.uuid4().hex}.png', evidence_bytes)},
				)
				evidence_attachment_response.raise_for_status()
				evidence_attachment = evidence_attachment_response.json().get('message')

				pqrsf_update_response = requests_session.put(
					f"{os.getenv('JUPITER_URL')}/api/resource/{os.getenv('JUPITER_PQSRF_RESOURCE_NAME')}/{pqsrf.get('name')}",
					json={f'evidencias{index}': evidence_attachment.get('file_url')},
				)
				pqrsf_update_response.raise_for_status()
			except Exception:
				pass
	return pqsrf
