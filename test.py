import json
import app
import unittest

class Test_Movies(unittest.TestCase):
    def test_read_all(self):
        connext_app = app.connex_app
        client = connext_app.app.test_client()
        url = '/api/movies'
        response = client.get(url)
        assert response.status_code == 200

    def test_read_top_rated(self):
        connext_app = app.connex_app
        client = connext_app.app.test_client()
        url = '/api/movies/top_rated'
        response = client.get(url)
        assert response.status_code == 200

    def test_read_popular(self):
        connext_app = app.connex_app
        client = connext_app.app.test_client()
        url = '/api/movies/popular'
        response = client.get(url)
        assert response.status_code == 200

    def test_read_by_title(self):
        connext_app = app.connex_app
        client = connext_app.app.test_client()
        url = '/api/movies/avatar'
        response = client.get(url)
        assert response.status_code == 200

class Test_Director(unittest.TestCase):
    def test_read_all(self):
        connext_app = app.connex_app
        client = connext_app.app.test_client()
        url = '/api/director'
        response = client.get(url)
        assert response.status_code == 200

    def test_read_one(self):
        connext_app = app.connex_app
        client = connext_app.app.test_client()
        url = '/api/director/7110'

        response = client.get(url)
        assert response.status_code == 200

    def test_read_by_name(self):
        connext_app = app.connex_app
        client = connext_app.app.test_client()
        url = '/api/director/search/james'
        response = client.get(url)
        assert response.status_code == 200
 
    # def test_create_director(self):
    #     connext_app = app.connex_app
    #     # connext_app.add_api("swagger.yml")
    #     client = connext_app.app.test_client()
    #     url = '/api/director'
    #     mock_request_headers =  {'Content-Type': 'application/json', 'charset': 'utf-8'}
    #     mock_request_data  = {
    #         "department": "directing",
    #         "gender": 2,
    #         "name": "lala",
    #         "uid": 32412
    #         }

    #     response = client.post(url, data=json.dumps(mock_request_data), headers=mock_request_headers)
    #     print(response)
    #     assert response.status_code == 200

if __name__ == "__main__":
    unittest.main()
    print("Everything passed")