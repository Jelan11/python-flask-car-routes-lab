#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

MODELS = ['Crossroads', 'Beedle']

@app.route('/')
def index():
    return 'Welcome to Flatiron Cars'

@app.route('/<model>')
def model(model):
    if model in MODELS:
        return f'Flatiron {model} is in our fleet!'
    return f'No models called {model} exists in our catalog'

if __name__ == '__main__':
    app.run(port=5555, debug=True)