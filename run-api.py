# -*- coding: utf-8 -*-

"""
    Eve Demo
    ~~~~~~~~

    A demostration of a simple API powered by Eve REST API.

    The live demo is available at eve-demo.herokuapp.com. Please keep in mind
    that the it is running on Heroku's free tier using a free MongoHQ
    sandbox, which means that the first request to the service will probably
    be slow. The database gets a reset every now and then.

    :copyright: (c) 2016 by Nicola Iarocci.
    :license: BSD, see LICENSE for more details.
"""

import os
from eve import Eve
from eve_swagger import swagger
# from flask.ext.sentinel import ResourceOwnerPasswordCredentials, oauth

# Heroku support: bind to PORT if defined, otherwise default to 5000.
if 'PORT' in os.environ:
    port = int(os.environ.get('PORT'))
    # use '0.0.0.0' to ensure your REST API is reachable from all your
    # network (and not only your computer).
    host = '0.0.0.0'
else:
    port = 5000
    host = '127.0.0.1'

SETTINGS_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'settings.py')
app = Eve(settings=SETTINGS_PATH)

# add eve-swagger
# /api-docs
# curl -k -H "Authorization: Bearer tnIpW1XWyrrUQSlIUZbG2O2TNjp3W7" https://localhost:5000/api-docs
app.register_blueprint(swagger)

# required. See http://swagger.io/specification/#infoObject for details.
app.config['SWAGGER_INFO'] = {
    'title': '学吧辅导 API',
    'version': '0.1',
    'description': '一对一辅导，提供实时语音，和教学白板。',
    'termsOfService': 'my terms of service',
    'contact': {
        'name': 'hejiayi',
        'url': 'http://192.168.0.40:5000'
    },
    # 'license': {
    #     'name': 'BSD',
    #     'url': 'https://github.com/nicolaiarocci/eve-swagger/blob/master/LICENSE',
    # }
}

# optional. Will use flask.request.host if missing.
app.config['SWAGGER_HOST'] = '192.168.0.40:5000'

# add flask-sentinel
# curl -k -X POST -d "client_id=o0DKRNzRNJouovo2oJupkto8jDFwa6NouU7cOQ5N&grant_type=password&username=janreyho&password=123456" https://localhost:5000/oauth/token
# curl -k -H "Authorization: Bearer tnIpW1XWyrrUQSlIUZbG2O2TNjp3W7" https://localhost:5000/
# @app.route('/endpoint')
# @oauth.require_oauth()
# def restricted_access():
#     return "You made it through and accessed the protected resource!"

@app.route('/testapi')
def testapi():
    return 'testapi Hello, World!'

@app.route('/students')
def teststudents():
    print 'students Hello, World!'

if __name__ == '__main__':
    # ResourceOwnerPasswordCredentials(app)
    # app.run(host=host, port=port,ssl_context='adhoc')
    app.run(host, port)
