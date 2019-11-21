import unittest
import flask_testing
from urllib import request
from flask import Flask
import json
from flask_testing import LiveServerTestCase

class Livetest(LiveServerTestCase):

    def create_app(self):
        app = Flask(__name__)
        app.config['TESTING'] = True
        app.config['LIVESERVER_PORT'] = 5000
        app.config['LIVESERVER_TIMEOUT'] = 10
        return app

    def test_server_is_up_and_running(self):
        with request.urlopen(self.get_server_url()) as response:
            self.assertEqual(response.getcode(), 200)

    def test_hello_world(self):
        with request.urlopen("%s" % self.get_server_url()) as response:
            json_response = json.loads(response.read().decode(response.info().get_param('charset') or 'utf-8'))
            self.assertEqual(json_response, dict(status=True, message = "Hello, World!"))
    
    def test_factorial_1_equal_1(self):
        with request.urlopen("%s/factorial?n=1" % self.get_server_url()) as response:
            json_response = json.loads(response.read().decode(response.info().get_param('charset') or 'utf-8'))
            self.assertEqual(json_response, dict(status=True, result = 1, message = "OK"))
    
    def test_factorial_5_equal_120(self):
        with request.urlopen("%s/factorial?n=5" % self.get_server_url()) as response:
            json_response = json.loads(response.read().decode(response.info().get_param('charset') or 'utf-8'))
            self.assertEqual(json_response, dict(status=True, result = 120, message = "OK"))
            
if __name__ == '__main__':
    unittest.main()