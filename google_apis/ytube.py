from .utility import create_service


class YouTube:
	API_NAME = 'youtube'
	API_VERSION = 'v3'
	SCOPES = ['https://www.googleapis.com/auth/youtube',
			  'https://www.googleapis.com/auth/youtube.force-ssl']

	def __init__(self, client_file):
		self.client_file = client_file
		self.service = None

	def init_service(self):
		self.service = create_service(self.client_file, self.API_NAME, self.API_VERSION, self.SCOPES)

