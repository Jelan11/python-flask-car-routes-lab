from flask import Flask

app = Flask(__name__)

existing_models = ['Beedle', 'Crossroads', 'M2', 'Panique']

#default route
@app.route('/')
def index():
    return 'Welcome to Flatiron Cars'

#route for model
@app.route('/<model>')
def get_model(model):
    if model in existing_models:
        return f'Flatiron {model} is in our fleet!'
    return f'No models called {model} exists in our catalog'


if __name__ == '__main__':
    app.run(port=5555, debug=True)