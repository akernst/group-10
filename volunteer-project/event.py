from google.appengine.ext import ndb


class Event(ndb.Model):
	eventname = ndb.StringProperty(required = True)
	eventdate = ndb.StringProperty(required = True)
	datetime = ndb.DateTimeProperty(auto_now = True)
	eventinfo = ndb.StringProperty(required = False)
	location = ndb.IntegerProperty(required = False)
	agereq = ndb.IntegerProperty(required = True)
	tags = ndb.StringProperty(required= False)
	profile = ndb.BlobProperty(required = False)