from tests import TestCase


class TestSomething(TestCase):
	def test_config(self):
		self.app.loadConfig()
