from google.appengine.ext import ndb


class Event(ndb.Model):
	eventname = ndb.StringProperty(required = True)
	eventdate = ndb.StringProperty(required = True)
	datetime = ndb.DateTimeProperty(auto_now = True)
	eventinfo = ndb.StringProperty(required = False)
	location = ndb.StringProperty(required = False)
	agereq = ndb.IntegerProperty(required = False)
	tags = ndb.StringProperty(required = True)
	profile = ndb.BlobProperty(required = False)