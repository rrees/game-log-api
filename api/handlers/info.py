import flask

def root():
    return flask.jsonify({
        'message': 'Hello world',
    })