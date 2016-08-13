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
import bcrypt


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
    print request
    print payload


def post_contacts_get_callback(request, payload):
    print 'A post get on "contacts" was just performed!'




def pre_students_post_callback(request):
    # assert request.path == '/students'
    # assert request.method == 'POST'
    print 'pre_students_post_callback'
    print request.path
    print request.method
    print request.get_json()["password"]
    passwd = request.get_json()["password"]
    print passwd.encode('utf-8')
    # print request.data
    print bcrypt.hashpw(passwd.encode('utf-8'), bcrypt.gensalt())
    request.get_json()["password"] = bcrypt.hashpw(passwd.encode('utf-8'), bcrypt.gensalt())
    print request.get_json()["password"]

def post_students_post_callback(request, lookup):
    print 'post_students_post_callback'
    print request
    print lookup["username"]

def pre_teachers_post_callback(request, payload):
    print 'pre_teachers_post_callback'
    print request

app = Eve()
app.debug = True
# app.on_fetched_resource += piterpy
# app.on_post_GET += post_get_callback
# app.on_pre_GET_students += pre_contacts_get_callback
# app.on_post_GET_students += post_contacts_get_callback

app.on_pre_POST_students += pre_students_post_callback
# app.on_post_POST_students += post_students_post_callback
# app.on_pre_POST_teachers += pre_teachers_post_callback

if __name__ == '__main__':
    app.run()
