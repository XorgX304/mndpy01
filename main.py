import webapp2
import cgi
import jinja2
import os
import urllib
from google.appengine.ext import ndb


JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

def database_key(database_name='mnddb01'):
        """Constructs a Datastore key for a Guestbook entity with guestbook_name."""
        return ndb.Key('db', database_name)

MAIN_PAGE_HTML = """
<html>
  <head>
    <title>main page</title>
  </head>
  <body>
    <h3>Hello from main page</h3>
   
    <form action="/response" method="post">
      is my wife bossy?
      <select name="answer">
        <option value="yes">yes</option>
        <option value="no">no</option>
      </select>
      <div><input type="submit" value="enter"></div>
    </form>
  </body>
</html>
"""



class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.write(MAIN_PAGE_HTML)
        

class Response(webapp2.RequestHandler):
    def post(self):
        answer = cgi.escape(self.request.get('answer'))
        
        if answer == "yes":
            snidecomment = 'yes ... she is bossy'
        else:
            snidecomment = 'no ... well sometimes she is'
        
        self.response.write('</pre></body></html>')       

        template_values = {
            'meta' :  '<meta http-equiv="refresh" content="3;/" />',
            'title' : 'response',           
            'snidecomment': snidecomment,
            'answer': answer,
        }

        template = JINJA_ENVIRONMENT.get_template('/templates/mytemplate.html')
        self.response.write(template.render(template_values))
        

class Greeting(ndb.Model):
    """Models an individual database entry."""
    comment = ndb.StringProperty(indexed=False)
    date = ndb.DateTimeProperty(auto_now_add=True)
   

application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/response', Response),
], debug=True)