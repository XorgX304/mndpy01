import webapp2
import cgi


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
        self.response.write('<html><head><meta http-equiv="refresh" content="3;/" /><title>response</title></head><body><pre>')
        answer = cgi.escape(self.request.get('answer'))
        
        if answer == "yes":
          self.response.write('yes ... she is bossy')
        else:
          self.response.write ('no ... well sometimes she is') 
        
        self.response.write('</pre></body></html>')

application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/response', Response),
], debug=True)