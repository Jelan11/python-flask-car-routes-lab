from server.app import app


class TestApp:
    '''Flask application in server/app.py'''

    def test_index_route(self):
        '''has a resource available at "/".'''
        response = app.test_client().get('/')
        assert response.status_code == 200

    def test_index_text(self):
        '''displays "Welcome to Flatiron Cars" for the "/" route.'''
        response = app.test_client().get('/')
        assert response.data.decode() == 'Welcome to Flatiron Cars'

    def test_model_route(self):
        '''has a resource available at "/<model>".'''
        response = app.test_client().get('/Beedle')
        assert response.status_code == 200

    def test_model_text(self):
        '''displays text of the "/<model>" route.'''
        response = app.test_client().get('/Crossroads')
        assert response.data.decode() == 'Flatiron Crossroads is in our fleet!'

    def test_all_existing_models(self):
        '''every model in the catalog returns the fleet message.'''
        for model in ['Beedle', 'Crossroads', 'M2', 'Panique']:
            response = app.test_client().get(f'/{model}')
            assert response.data.decode() == f'Flatiron {model} is in our fleet!'

    def test_model_failure_text(self):
        '''displays failure text of the "/<model>" route.'''
        response = app.test_client().get('/realCar')
        assert response.data.decode() == 'No models called realCar exists in our catalog'