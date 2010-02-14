from google.appengine.ext import webapp
from google.appengine.api import memcache
from google.appengine.ext.webapp import template

import hyphenate_html

class BaseHandler(webapp.RequestHandler):
    def render_template(self, template_name='base.html', values={}):
        return template.render(template_name, values)

class HtmlHyphenator(BaseHandler):
    def get(self):
        self.response.out.write(self.render_template())

    def post(self):
        content = self.request.get('content')
        lang = self.request.get('lang', 'en-us')
        output = hyphenate_html.hyphenate_html(content, lang)
        self.response.out.write(self.render_template('base.html', {
            'content': content,
            'lang': lang,
            'output': output
        }))
