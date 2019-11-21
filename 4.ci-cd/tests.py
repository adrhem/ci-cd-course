from flask import Flask
from flask_testing import TestCase
from app import app
import unittest
import json

class MyTest(TestCase):

    def create_app(self):   
        return app

    def test_hello_world(self):
        response = self.client.get("/")
        self.assertEqual(response.json, dict(status=True, message = "Hello, World!"))
    
    def test_factorial_1_equal_1(self):
        response = self.client.get("/factorial?n=1")
        self.assertEqual(response.json, dict(status=True, result = 1, message = "OK"))
    
    def test_factorial_5_equal_120(self):
        response = self.client.get("/factorial?n=5")
        self.assertEqual(response.json, dict(status=True, result = 120, message = "OK"))
            
if __name__ == '__main__':
    unittest.main()