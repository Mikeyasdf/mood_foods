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

<<<<<<< HEAD
=======
<<<<<<< HEAD
=======
#add <form action="/page_2" method="post"> in the about.html to make buttons do stuff


class Page_2(webapp2.RequestHandler):

>>>>>>> f91dda4940c8a7a95e726d58893c6385bee518cd
>>>>>>> 820e002c8ce585c731a20c0d58ef0d869fc23d3a
    def post(self):
        about_template = the_jinja_env.get_template('templates/page_2.html')
        isError = False
        if(isError):
            self.redirect("/page_2")
        else:
<<<<<<< HEAD
            self.redirect("/") 

class Page_2(webapp2.RequestHandler):
    def get(self):
        about_template = the_jinja_env.get_template('templates/index.html')
        self.response.write(about_template.render())
=======
            self.redirect("/page_2")     
>>>>>>> 820e002c8ce585c731a20c0d58ef0d869fc23d3a
        
    def post(self):
        if True:
            self.response.write("Error dummy!")
        else:
            self.redirect("/")

app = webapp2.WSGIApplication([
    ('/', AboutPage),
    ('/page_2', Page_2),
], debug=True)