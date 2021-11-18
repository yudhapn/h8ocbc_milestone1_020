import json
import app
import unittest

class Test_Movies(unittest.TestCase):
    # test case for checking if response code get all movies endpoint is 200 (Success)
    def test_read_all_succeeded(self):
        connext_app = app.connex_app
        client = connext_app.app.test_client()
        url = '/api/movies'
        response = client.get(url)
        assert response.status_code == 200

    # test case for checking if response code get top rated movies endpoint is 200 (Success)
    def test_read_top_rated_is_succeeded(self):
        connext_app = app.connex_app
        client = connext_app.app.test_client()
        url = '/api/movies/top_rated'
        response = client.get(url)
        assert response.status_code == 200

    # test case for checking if response code get popular movies endpoint is 200 (Success)
    def test_read_popular_is_succeeded(self):
        connext_app = app.connex_app
        client = connext_app.app.test_client()
        url = '/api/movies/popular'
        response = client.get(url)
        assert response.status_code == 200

    # test case for checking if response code get movies by title endpoint is 200 (Success)
    def test_read_by_title_is_succeeded(self):
        connext_app = app.connex_app
        client = connext_app.app.test_client()
        url = '/api/movies/avatar'
        response = client.get(url)
        assert response.status_code == 200

class Test_Director(unittest.TestCase):
    # test case for checking if response code get all directors endpoint is 200 (Success)
    def test_read_all_is_succeeded(self):
        connext_app = app.connex_app
        client = connext_app.app.test_client()
        url = '/api/director'
        response = client.get(url)
        assert response.status_code == 200

    # test case for checking if response code get a director endpoint is 200 (Success)
    def test_read_one_is_succeeded(self):
        connext_app = app.connex_app
        client = connext_app.app.test_client()
        url = '/api/director/7110'
        response = client.get(url)
        assert response.status_code == 200

    # test case for checking if response code get directors by name endpoint is 200 (Success)
    def test_read_by_name_is_succeeded(self):
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