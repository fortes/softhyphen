from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

import os
import sys
# Add current folder to path
sys.path.insert(0, os.path.dirname(__file__))
import handlers

application = webapp.WSGIApplication([
    ('/.*', handlers.HtmlHyphenator)
])

def main():
    run_wsgi_app(application)

if __name__ == '__main__':
    main()
