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
def button_choices(button_choice):
    if button_choice == 'Happy':
        url = 'https://upload.wikimedia.org/wikipedia/commons/4/47/StateLibQld_1_100348.jpg'
    elif button_choice == 'Sad':
        url = 'https://upload.wikimedia.org/wikipedia/commons/c/ca/LinusPaulingGraduation1922.jpg'
    elif button_choice == 'Angry':
        url = 'https://upload.wikimedia.org/wikipedia/commons/f/ff/Deep_in_thought.jpg'
    elif button_choice == 'Nervous':
        url = 'https://upload.wikimedia.org/wikipedia/commons/b/b9/Typing_computer_screen_reflection.jpg'
    elif button_choice == 'Excited':
        url = 'https://upload.wikimedia.org/wikipedia/commons/b/b9/Typing_computer_screen_reflection.jpg'
    return url
    
class AboutPage(webapp2.RequestHandler):
    def get(self):
        about_template = the_jinja_env.get_template('templates/about.html')
        self.response.write(about_template.render())
   

class ContactPage(webapp2.RequestHandler):
    def get(self):
        about_template = the_jinja_env.get_template('templates/index.html')
        self.response.write(about_template.render())
        
    def post(self):
        isError = False
        if(isError):
            self.response.write("Error dummy!")
        else:
            self.redirect("/")

app = webapp2.WSGIApplication([
    ('/', AboutPage),
    ('/contact', ContactPage),
], debug=True)