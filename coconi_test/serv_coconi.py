import os
import webapp2
import jinja2

import logging

from google.appengine.ext import db

#template_dir = os.path.join(os.path.dirname(__file__), 'templates')
#jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
#                               autoescape=True)

jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
                                       autoescape=True)

class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))


class MainPage(Handler):
    def render_front(self):
        logging.error('rendering MainPage')
        
        self.render("coconi.html")


    def get(self):

        self.render_front()


#import StringIO
##import numpy as np
#os.environ["MATPLOTLIBDATA"] = os.getcwdu()  # own matplotlib data
#os.environ["MPLCONFIGDIR"] = os.getcwdu()    # own matplotlibrc
#import numpy, matplotlib, matplotlib.pyplot as plt



class Analysis(Handler):
  def post(self):
    logging.error('writing Analysis')

    #self.redirect('/')
    
#    pl.plot(np.random.random((20)))
#    sio = StringIO.StringIO()
#    pl.savefig(sio, format="png")
#    img_b64 = sio.getvalue().encode("base64").strip()
#    pl.clf()
#    sio.close()

    self.write("""<html><body>You got it! <br>""")
    #self.write("<img src='data:image/png;base64,%s'/>" % img_b64)
    self.write("""</body> </html>""")


app = webapp2.WSGIApplication([('/', MainPage), ('/analysis', Analysis)], debug=True)


