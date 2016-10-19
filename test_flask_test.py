

	def setUp(self):
		server.app.testing = True
		self.app = server.app.test_client()

	def test_hello(self):
		response = self.app.get('/pets')
		print response.data

if __name__ == '__main__':
	unittest.main()
