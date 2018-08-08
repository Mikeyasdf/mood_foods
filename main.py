import webapp2
from random import shuffle
import jinja2
import os

#libraries for APIs
from google.appengine.api import urlfetch
import json

the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
    
    
class AboutPage(webapp2.RequestHandler):
    def get(self):
        about_template = the_jinja_env.get_template('templates/about.html')
        self.response.write(about_template.render())
        
class Angry(webapp2.RequestHandler):

    def get(self):
        about_template = the_jinja_env.get_template('templates/Angry.html')
        self.response.write(about_template.render())

<<<<<<< HEAD
class Happy(webapp2.RequestHandler):

    def get(self):
        about_template = the_jinja_env.get_template('templates/Happy.html')
=======
class Motivated(webapp2.RequestHandler):

    def get(self):
        about_template = the_jinja_env.get_template('templates/Motivated.html')
>>>>>>> 0434aae04e5da26149d14e1b0a86ff4cdf393ab3
        self.response.write(about_template.render())

'''
class Page_2(webapp2.RequestHandler):
    def get(self):
        about_template = the_jinja_env.get_template('templates/index.html')
        self.response.write(about_template.render())

        self.redirect("/page_2")
    def post(self):
        if True:
            self.response.write("Error dummy!")
        else:
            self.redirect("/")
'''
app = webapp2.WSGIApplication([
    ('/', AboutPage),
    ('/Angry', Angry),
<<<<<<< HEAD
    ('/Happy', Happy)
=======
    ('/Motivated', Motivated)
>>>>>>> 0434aae04e5da26149d14e1b0a86ff4cdf393ab3
], debug=True)