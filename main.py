import webapp2
from random import shuffle
import jinja2
import os

<<<<<<< HEAD
#libraries for APIs
from google.appengine.api import urlfetch
=======

#libraries for APIs
from google.appengine.api import urlfetch
import json

>>>>>>> cd0855338a743c98cc68ffee41ae7f445ce3420f

the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
    
    
class AboutPage(webapp2.RequestHandler):
    def get(self):
        about_template = the_jinja_env.get_template('templates/about.html')
        self.response.write(about_template.render())
<<<<<<< HEAD
=======
   

>>>>>>> cd0855338a743c98cc68ffee41ae7f445ce3420f

class ContactPage(webapp2.RequestHandler):
    def get(self):
        about_template = the_jinja_env.get_template('templates/index.html')
        self.response.write(about_template.render())
<<<<<<< HEAD
   
    def post(self):
        isError = False
        if(isError):
            self.response.write("Error dummy!")
        else:
            self.redirect("/")
=======

>>>>>>> cd0855338a743c98cc68ffee41ae7f445ce3420f

app = webapp2.WSGIApplication([
    ('/', AboutPage),
    ('/contact', ContactPage),
<<<<<<< HEAD
], debug=True)
=======
], debug=True)


>>>>>>> cd0855338a743c98cc68ffee41ae7f445ce3420f
