import unittest

from webapp import create_app
from webapp.models import db, User , Role
from webapp.extensions import admin, rest_api

class TestURLs(unittest.TestCase):
	def setUp(self):
		admin._views = []
		rest_api.resources = []
		app = create_app('webapp.config.TestConfig')
		self.client = app.test_client()
		db.app = app
		db.create_all()

	def tearDown(self):
		db.session.remove()
		db.drop_all()


	def test_catalog_home(self):
		result = self.client.get('/catalog')
		self.assertEqual(result.status_code,200)
		

if __name__ == '__main__':
	unittest.main()
