import requests
from requests.auth import HTTPBasicAuth


class OkmDocument(object):

    def __init__(self, username, password, url):
        self.auth = HTTPBasicAuth(username, password)
        self.url = url.__add__('/services/rest/document')

    def getDocument(self, srcPath, dstName):
        payload = {'docId': srcPath}
        request = self.url.__add__('/getContent')
        r = requests.get(request, params=payload, auth=self.auth)
        with open(''.__add__(dstName), 'wb') as file:
            file.write(r.content)
        assert r.status_code == 200

    def getDocumentVersionHistory(self, srcPath):
        payload = {'docId': srcPath}
        request = self.url.__add__('/getVersionHistory')
        r = requests.get(request, params=payload,
                         auth=self.auth,
                         headers={'Content-Type': 'application/json'})
        with open(''.__add__('versionHistory.json'), 'w') as file:
            file.write(r.text)
        assert r.status_code == 200

    def getDocumentProperties(self, srcPath):
        payload = {'docId': srcPath}
        request = self.url.__add__('/getProperties')
        r = requests.get(request, params=payload,
                         auth=self.auth,
                         headers={'Content-Type': 'application/json'})
        with open(''.__add__('versionHistory.json'), 'w') as file:
            file.write(r.text)
        assert r.status_code == 200

    def copyDocument(self, srcPath, dstPath):
        payload = {'docId': srcPath, 'dstId': dstPath}
        request = self.url.__add__('/copy')
        r = requests.put(request, params=payload,
                         auth=self.auth)
        assert r.status_code == 204

    def deleteDocument(self, srcPath):
        payload = {'docId': srcPath}
        request = self.url.__add__('/delete')
        r = requests.delete(request, params=payload, auth=self.auth)
        assert r.status_code == 204