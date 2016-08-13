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


def piterpy(endpoint, response):
    print "hejiayi"
    print endpoint
    print response
    for document in response['_items']:
        document['PITERPY'] = 'IS SO COOL!'

def post_get_callback(resource, request, payload):
    print 'A GET on the "%s" endpoint was just performed!' % resource


def pre_contacts_get_callback(request, payload):
    print 'A pre get on "contacts" was just performed!'
    abort(403)

def post_contacts_get_callback(request, payload):
    print 'A post get on "contacts" was just performed!'

app = Eve()
# app.on_fetched_resource += piterpy
# app.on_post_GET += post_get_callback
app.on_pre_GET_students += pre_contacts_get_callback
# app.on_post_GET_students += post_contacts_get_callback

if __name__ == '__main__':
    app.run()
