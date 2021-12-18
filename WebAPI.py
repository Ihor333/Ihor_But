import http.client
import json
class Test:
    def __init__(self):
        self.url1 = http.client.HTTPSConnection("content.dropboxapi.com")
        self.url2 = http.client.HTTPSConnection("api.dropboxapi.com")
        self.url3 = http.client.HTTPSConnection("api.dropboxapi.com")

    def test_upload(self):
        payload = 'Text for test'
        headers = {
            'Dropbox-API-Arg': '{"path": "/Test_file.txt","mode": "add","autorename": true,"mute": false,"strict_conflict": false}',
            'Content-Type': 'application/octet-stream',
            'Authorization': 'Bearer 5ihZn_j5xxUAAAAAAAAAAb8I12_nNV6oEH5BJJIk4XSzaBBpRxaxTZ_JsgfAFJUM'
        }
        self.url1.request("POST", "/2/files/upload", payload, headers)
        assert self.url1.getresponse().status == 200, "test with upload failed"

    def test_get_file_metadata(self):
        payload = json.dumps({
            "path": "/Test_file.txt",
            "include_media_info": False,
            "include_deleted": False,
            "include_has_explicit_shared_members": False
        })
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer 5ihZn_j5xxUAAAAAAAAAAb8I12_nNV6oEH5BJJIk4XSzaBBpRxaxTZ_JsgfAFJUM'
        }
        self.url2.request("POST", "/2/files/get_metadata", payload, headers)
        assert self.url2.getresponse().status == 200, "test with file metadata failed"

    def test_delete_file(self):
        payload = json.dumps({
            "path": "/Test_file.txt"
        })
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer 5ihZn_j5xxUAAAAAAAAAAb8I12_nNV6oEH5BJJIk4XSzaBBpRxaxTZ_JsgfAFJUM'
        }
        self.url3.request("POST", "/2/files/delete_v2", payload, headers)
        assert self.url3.getresponse().status == 200, "test with  failed"

    def run_test(self):
        self.test_upload()
        self.test_get_file_metadata()
        self.test_delete_file()

test = Test()
test.run_test()