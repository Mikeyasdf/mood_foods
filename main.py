import webapp2
from random import shuffle
import jinja2
import os

#libraries for APIs
from google.appengine.api import urlfetch

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

#add <form action="/page_2" method="post"> in the about.html to make buttons do stuff


class Page_2(webapp2.RequestHandler):

    def post(self):
        about_template = the_jinja_env.get_template('templates/page_2.html')
        if True:
            self.redirect("/page_2")
        else:
            self.redirect("/")     


app = webapp2.WSGIApplication([
    ('/', AboutPage),
    ('/page_2', Page_2),
], debug=True)