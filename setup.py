from setuptools import setup

setup(
	name='ftclotto',
	packages=['ftclotto'],
	inclide_package_data=True,
	install_requires=[
		'flask',
		'requests',
		'requests_oauthlib',
		'pyopenssl',
		'tinydb'
	]
)