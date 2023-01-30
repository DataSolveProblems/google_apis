from .exceptions import AuthException
from .google_apis import create_service

class GDrive:
    API_NAME = 'drive'
    API_VERSION = 'v3'
    SCOPES = ['https://www.googleapis.com/auth/drive']
    
    def __init__(self, client_file):
        self.client_file = client_file
        self.service = None

    def init_service(self):
        self.service = create_service(self.client_file, self.API_NAME, self.API_VERSION, self.SCOPES)

    def list_files(self, corpora=None, drive_id=None, fields='all', include_items_from_all_drives=False, include_labels=True, 
            order_by=None, page_size=1000, q=None, spaces=None, supports_all_drives=False):
        """
        https://developers.google.com/drive/api/v3/reference/files/list#request
        """
        ...

    def get_file(self, file_id):
        response = drive.service.files().get(
            fileId=file_id,
        ).execute()
        return response


if __name__ == '__main__':
    client_file = r"C:\Users\Me\Documents\PythonVenv\google_apis\client-secret.json"    
    drive = GDrive(client_file)
    drive.init_service()

    files = []
    page_token = None
    fields = ['id', 'name', 'mimeType', 'parents', 'webViewLink', 'webContentLink', 'size',
            'version', 'createdTime']

    # response = drive.service.files().get(
    #     fileId='1AtQI7QXCuAR2czHHYORfI26ES1Gt4c1e',
    #     fields='*'
    #     fields='id,name,parents,webViewLink,mimeType'
    # ).execute()

    while True:
        response = drive.service.files().list(
            fields='nextPageToken,files(id,parents)',
            # fields='nextPageToken,files({0})'.format(','.join(fields)),
            # fields='nextPageToken,files(id,name,mimeType,parents)',
            # fields='nextPageToken,files(*)',
            pageToken=page_token
        ).execute()
        
        files.extend(response['files'])    
        page_token = response.get('nextPageToken')    
        print('processing batch {0}...'.format(page_token))
        if page_token is None:
            break

    with open('file directory tree.json', 'w') as f:
        json.dump({'files': files}, f, indent=4)




