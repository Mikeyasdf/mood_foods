import tkinter 
import webapp2


button = tk.Button(
        frame, text = "button", fg = "green", command = "submit")

        
        
app = webapp2.WSGIApplication([
    ('/', EnterInfoHandler),
], debug=True)