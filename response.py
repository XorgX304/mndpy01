import webapp2
import cgi
import jinja2
import os

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class Response(webapp2.RequestHandler):
    def post(self):
        answer = cgi.escape(self.request.get('answer'))
        
        if answer == "yes":
            snidecomment = 'yes ... she is bossy'
        else:
            snidecomment = 'no ... well sometimes she is'

        template_values = {
            'meta' :  '<meta http-equiv="refresh" content="3;/" />',
            'title' : 'response',           
            'snidecomment': snidecomment,
            'answer': answer,
        }

        template = JINJA_ENVIRONMENT.get_template('/templates/templateresult.html')
        self.response.write(template.render(template_values))
        