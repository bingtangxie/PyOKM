import requests
from requests.auth import HTTPBasicAuth


class OkmDocument(object):

    def __init__(self, username, password, url):
        self.auth = HTTPBasicAuth(username, password)
        self.url = url.__add__('/services/rest/document')

# We are able to upload a document to our system taking the path where it is locally.
    # The information returned includes the id of the document in the manager.

    def uploadDocument(self, srcPath):
        request = self.url.__add__('/create')
        multipart_form_data = {
            'file': open(srcPath, 'rb')
        }
        r = requests.post(request, files=multipart_form_data,
                          headers={'Content-Type': 'application/json'})

# We obtain the document selected in the source path and we save it with the destination name.

    def getDocument(self, srcPath, dstName):
        payload = {'docId': srcPath}
        request = self.url.__add__('/getContent')
        r = requests.get(request, params=payload, auth=self.auth)
        with open(''.__add__(dstName), 'wb') as file:
            file.write(r.content)
        assert r.status_code == 200

# We get a JSON with the version history of a concrete document, the JSON is saved in a file.

    def getDocumentVersionHistory(self, srcPath):
        payload = {'docId': srcPath}
        request = self.url.__add__('/getVersionHistory')
        r = requests.get(request, params=payload,
                         auth=self.auth,
                         headers={'Content-Type': 'application/json'})
        with open(''.__add__('versionHistory.json'), 'w') as file:
            file.write(r.text)
        assert r.status_code == 200

# We get the properties of a document and we save them into a JSON.

    def getDocumentProperties(self, srcPath):
        payload = {'docId': srcPath}
        request = self.url.__add__('/getProperties')
        r = requests.get(request, params=payload,
                         auth=self.auth,
                         headers={'Content-Type': 'application/json'})
        with open(''.__add__('versionHistory.json'), 'w') as file:
            file.write(r.text)
        assert r.status_code == 200

# We copy a document to another new path.

    def copyDocument(self, srcPath, dstPath):
        payload = {'docId': srcPath, 'dstId': dstPath}
        request = self.url.__add__('/copy')
        r = requests.put(request, params=payload,
                         auth=self.auth)
        assert r.status_code == 204

# We delete a document of a concrete path.

    def deleteDocument(self, srcPath):
        payload = {'docId': srcPath}
        request = self.url.__add__('/delete')
        r = requests.delete(request, params=payload, auth=self.auth)
        assert r.status_code == 204

# We move a document from a sorcePath to another one.

    def moveDocument(self, srcPath, dstPath):
        self.copyDocument(srcPath, dstPath)
        self.deleteDocument(srcPath)