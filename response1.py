import webapp2
import cgi
#import jinja2
import os
import viewhelper


class Response(webapp2.RequestHandler):
    def post(self):
        answer = cgi.escape(self.request.get('answer'))
        
        if answer == "yes":
            snidecomment = 'yes ... she is bossy'
        else:
            snidecomment = 'no ... well sometimes she is'
      
        template_values = {
            'meta' : '<meta http-equiv="refresh" content="3;/" />',
            'title' : 'response',           
            'snidecomment': snidecomment,
            'answer': answer,
        }
        mytemplate = 'templateresult.html'
        
        view = viewhelper.helper(mytemplate,template_values)
        
        self.response.write(view)
       
        