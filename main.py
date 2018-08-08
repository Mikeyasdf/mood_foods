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
<<<<<<< HEAD
        self.response.write(about_template.render()) 
class Page_2(webapp2.RequestHandler):

    def post(self):
        about_template = the_jinja_env.get_template('templates/page_2.html')
        if True:
            self.redirect("/page_2")
        else:
            self.redirect("/") 
=======
        self.response.write(about_template.render())
        
class Angry(webapp2.RequestHandler):

    def get(self):
        about_template = the_jinja_env.get_template('templates/Angry.html')
        self.response.write(about_template.render())
>>>>>>> 0c05bc94757d95d9ddfbf2f0f2cc2a39ad5e7051

app = webapp2.WSGIApplication([
    ('/', AboutPage),
    ('/Angry', Angry),
], debug=True)