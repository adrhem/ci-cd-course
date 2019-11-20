import os
from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

def factorial(n):
    if n < 1: 
        raise ValueError("N tiene que ser mayor a 1")
    elif n <= 2:
        return n
    else:
        return n * factorial(n - 1)

@app.route('/')
def route_helloworld():
  return jsonify(status=True, message="Hello, World!")

@app.route('/factorial')
def route_factorial():
    try:
        n = request.args.get('n')
        if not n.isnumeric():
            raise ValueError("La entrada tiene que ser número.")

        return jsonify(status=True, message = "OK", result = factorial(int(n)))
    except ValueError as identifier:
        return jsonify(status=False, message = str(identifier))
    except Exception as default:
        return jsonify(status=False, message = str(default))