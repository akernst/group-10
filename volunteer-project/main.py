#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import jinja2
from google.appengine.api import images
from google.appengine.api import users
from event import Event 
from user import User 

env = jinja2.Environment(
	loader=jinja2.FileSystemLoader("templates"))

class MainHandler(webapp2.RequestHandler):
	def get(self):

		'''This section initiates the log in function'''
		user = users.get_current_user()
		if user:
			greeting = ('Welcome, %s! (<a href="%s">sign out</a>)' %
			(user.nickname(), users.create_logout_url('/')))
		else:
			greeting = ('<a href="%s">Sign in or register</a>.' %
			users.create_login_url('/'))

		self.response.out.write('<html><body>%s</body></html>' % greeting)
   		
	

class HomeHandler(webapp2.RequestHandler):
	def get(self):
		template = env.get_template("home.html")
		
		event_query = Event.query()
  	event_results = event_query.fetch()

		query = self.request.get("search_term", "default")
		

		self.response.write(template.render())
	
class SearchHandler(webapp2.RequestHnadler):
	def get(self):
		template = env.get_template("search.html")

class allEventsHandler(webapp2.RequestHandler):
	def get(self):

		
app = webapp2.WSGIApplication([
	('/', MainHandler),
	('/home', HomeHandler),
	('/search',SearchHandler),
	('/allEvents', allEventHandler)
], debug=True)
