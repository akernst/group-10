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
import json
import jinja2
from google.appengine.api import images
from google.appengine.api import users
from event import Event 
from voluser import VolUser 
import logging

env = jinja2.Environment(
	loader=jinja2.FileSystemLoader("templates"))

class MainHandler(webapp2.RequestHandler):
	def get(self):
		# Displays events
		event_query = Event.query()
		event_results = event_query.fetch()

		chunked_events = [event_results[i:i+3] for i in xrange(0, len(event_results), 3)]
		
		data = {}
		data["chunked_events"]= chunked_events
		data["current_user"] = users.get_current_user()
		data["login"] = users.create_login_url('/')
		data["logout"] = users.create_logout_url('/')


		current_user = users.get_current_user()
		if current_user:
			greeting = ('Welcome, %s! (<a href="%s">sign out</a>)' %
			(current_user.nickname(), users.create_logout_url('/')))
		else:
			greeting = ('<a href="%s">Sign in or register</a>.' %
			users.create_login_url('/'))

		template = env.get_template("home.html")
		self.response.write(template.render(data))

class SearchHandler(webapp2.RequestHandler):
	def get(self):
		# Gets the search term entered
		query = self.request.get("search_term", "default")

		# looks for search term in tags of events
		event_query = Event.query().filter(Event.tags == query)
		matchedEvents = event_query.fetch()

		# puts entries into a ditionary
		data = {}
		data["matchedEvents"]=matchedEvents

		template = env.get_template("search.html")
		self.response.write(template.render(data))

class CreateEvent(webapp2.RequestHandler):
	def get(self):
		template = env.get_template("createEvent.html")
		self.response.out.write(template.render())
	def post(self):
		eventName = self.request.get('eventName')
		eventinfo = self.request.get('eventinfo')
		eventdate = self.request.get('eventdate')
		agereq = int(self.request.get('agereq'))
		tags = self.request.get('tags')
		profile = self.request.get('profile', "No-image-found.jpg")

		event = Event(eventname = eventName,
			eventdate = eventdate, 
			eventinfo = eventinfo, 
			agereq = agereq, 
			tags = tags, 
			profile = profile)
		event.put()

class AboutHandler(webapp2.RequestHandler):
	def get(self):
		template = env.get_template("about.html")
		self.response.out.write(template.render())

class ImageHandler(webapp2.RequestHandler):
	def get(self):
		eventId = self.request.get("eventId")

		# TODO: if we pass in something besides an int this will blow up
		e = Event.get_by_id(int(eventId))

		self.response.headers['Content-Type'] = 'image/jpeg'
		self.response.out.write(e.profile)

class allEventsHandler(webapp2.RequestHandler):
	def post(self):
		self.response.out.write("hi")

		
app = webapp2.WSGIApplication([
	('/', MainHandler),
	('/search', SearchHandler),
	('/createEvent', CreateEvent),
	('/about', AboutHandler),
	('/allEvents', allEventsHandler),
	('/img', ImageHandler)
], debug=True)
