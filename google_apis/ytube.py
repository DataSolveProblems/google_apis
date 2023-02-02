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


	def my_playlists(self):
		"""
		https://developers.google.com/youtube/v3/docs/playlists/list		
		"""	
		playlists = []
		response = yt.service.playlists().list(
			part='id,contentDetails,player,snippet,status',
			mine=True,
			maxResults=50
		).execute()

		playlists.extend(response.get('items'))
		next_page_token = response.get('nextPageToken')

		while next_page_token:
			response = yt.service.playlists().list(
				part='id,contentDetails,player,snippet,status',
				mine=True,
				maxResults=50,
				pageToken=next_page_token
			).execute()			
			playlists.extend(response.get('items'))
			next_page_token = response.get('nextPageToken')
		return playlsits

	def channel_playlists(self, channel_id):
		"""
		https://developers.google.com/youtube/v3/docs/playlists/list		
		"""
		playlists = []
		response = yt.service.playlists().list(
			part='id,contentDetails,player,snippet,status',
			channelId=channel_id,
			maxResults=50
		).execute()

		playlists.extend(response.get('items'))
		next_page_token = response.get('nextPageToken')

		while next_page_token:
			response = yt.service.playlists().list(
				part='id,contentDetails,player,snippet,status',
				channelId=channel_id,
				maxResults=50,
				pageToken=next_page_token
			).execute()			
			playlists.extend(response.get('items'))
			next_page_token = response.get('nextPageToken')
		return playlsits

    def create_playlist(self, title, description=None, privacy_status='public'):
        """
        https://developers.google.com/youtube/v3/docs/playlists#resource
        """
        request_body = {
            'snippet': {
                'title': title,
                'description': description,
            },
            'status': {
                'privacyStatus': privacy_status
            }
        }
        response = self.service.playlists().insert(
            part='snippet,status',
            body=request_body
        ).execute()
        return response

    def update_playlist(self, playlist_id, title, description=None, privacy_status=None):
        request_body = {
            'id': playlist_id,
            'snippet': {
                'title': title,
                'description': description
            },
            'status': {
                'privacyStatus': privacy_status
            }
        }
        response = self.service.playlists().update(
            part='snippet,status',
            body=request_body
        ).execute()
        return response        