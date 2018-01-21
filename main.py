from google.appengine.api import users
import webapp2
import json

class MainPage(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            self.response.headers['Content-Type'] = 'application/json'
            res = { 'nickname': user.nickname() }
            self.response.out.write(json.dumps(res))
        else:
            login_url = users.create_login_url('/')
            greeting = '<a href="{}">Sign in</a>'.format(login_url)
            self.response.write('<html><body>{}</body></html>'.format(greeting))

app = webapp2.WSGIApplication([('/', MainPage)], debug=True)
