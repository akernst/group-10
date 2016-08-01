from google.appengine.ext import ndb


class Event(ndb.Model):
	name = ndb.StringProperty(required = True)
	datetime = ndb.DateTimeProperty(required = True)
	eventinfo = ndb.StringProperty(required = True)
	location = ndb.StringProperty(required = True)
	agereq = ndb.IntegerProperty(required = False)
	tags = ndb.StringProperty(required = True)