import webapp2
import cgi
import jinja2
import os

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


def helper(mytemplate,variables):
  
  template_values = variables
  thistemplate = 'templates/'+ mytemplate
  
  template = JINJA_ENVIRONMENT.get_template(thistemplate)
  return template.render(template_values)