import nox


@nox.session
def tests(session):
	session.install('.[dev]')
	session.run('pytest')


@nox.session()
def lint(session):
	session.install('.[dev]')
	session.run('ruff', 'check', '.')


@nox.session()
def format(session):
	session.install('.[dev]')
	session.run('ruff', 'format', '--check', '.')
