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

from eve import Eve
from eve.auth import BasicAuth
from eve.auth import TokenAuth
import os
import redis
from eve.auth import requires_auth

class MyBasicAuth(BasicAuth):
    def check_auth(self, username, password, allowed_roles, resource,
                   method):
        return username == 'admin' and password == 'secret'

# class MyBasicAuth(BasicAuth):
#     def check_auth(self, username, password, allowed_roles, resource, method):
#         print username
#         print password
#         if resource in ('students', 'courses'):
#             # 'zipcodes' and 'countries' are public
#             return True
#         else:
#             return username == 'admin' and password == 'secre'

class BCryptAuth(BasicAuth):
    def check_auth(self, username, password, allowed_roles, resource, method):
        # use Eve's own db driver; no additional connections/resources are used
        print username
        print password
        accounts = app.data.driver.db['students']
        account = accounts.find_one({'username': 'janreyho2'})
        print account['password']
        return account and \
            bcrypt.hashpw(password, account['password']) == account['password']

class Sha1Auth(BasicAuth):
    def check_auth(self, username, password, allowed_roles, resource, method):
        # use Eve's own db driver; no additional connections/resources are used
        accounts = app.data.driver.db['accounts']
        account = accounts.find_one({'username': username})
        return account and \
            check_password_hash(account['password'], password)

class TokenAuth(TokenAuth):
    def check_auth(self, token, allowed_roles, resource, method):
        """For the purpose of this example the implementation is as simple as
        possible. A 'real' token should probably contain a hash of the
        username/password combo, which sould then validated against the account
        data stored on the DB.
        """
        # use Eve's own db driver; no additional connections/resources are used
        accounts = app.data.driver.db['accounts']
        return accounts.find_one({'token': token})

r = redis.StrictRedis(host='localhost', port=6379, db=0)
SETTINGS_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'settings.py')
app = Eve(settings=SETTINGS_PATH, auth=MyBasicAuth, redis=r)
app.debug = True

@app.route('/hello')
@requires_auth('22')
def restricted_access():
    return "You22 made it through and accessed the protected resource!"

if __name__ == '__main__':
    # app = Eve(auth=BCryptAuth)
    app.run()
