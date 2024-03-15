import os

import chalice
import pydantic
import requests


from chalicelib import crud, models

app = chalice.Chalice(app_name=__name__)
app.debug = os.getenv('DEBUG', 'false') == 'true'


@app.route('/', methods=['GET'])
def index():
	return {'Data': 'Welcome to PQSRF API'}


@app.route('/pqrsfs', methods=['POST'])
def pqrsf_create():
	try:
		return {'Data': crud.create_pqsrf(models.PQRSF(**(app.current_request.json_body or {})))}
	except pydantic.ValidationError as ve:
		if app.debug:
			app.log.error(f'{type(ve)} -> %s', str(ve))
		raise chalice.BadRequestError(
			'We encountered some errors processing your request. Please try again later.'
		)
	except requests.HTTPError as he:
		if app.debug:
			app.log.error(f'{type(he)} -> %s', str(he))
		if he.response.status_code == 400:
			raise chalice.BadRequestError(
				'We encountered some errors processing your request. Please try again later.'
			)
		if he.response.status_code == 401:
			raise chalice.UnauthorizedError('You are not authorized to do this request.')
		if he.response.status_code == 403:
			raise chalice.ForbiddenError(
				"You don't have the enough permissions to do this request."
			)
		raise chalice.ChaliceViewError('Something went wrong. Please try again later.')
	except Exception as e:
		if app.debug:
			app.log.error(f'{type(e)} -> %s', str(e))
		raise chalice.ChaliceViewError('Something went wrong. Please try again later.')


@app.route('/{any+}', methods=['GET', 'POST', 'PUT', 'PATCH', 'HEAD', 'OPTIONS', 'DELETE'])
def not_found(**kwargs):
	raise chalice.NotFoundError()
