from google.appengine.ext import ndb


class Event(ndb.Model):
	eventname = ndb.StringProperty(required = True)
	datetime = ndb.DateTimeProperty(auto_now = True)
	eventdate = ndb.StringProperty(required=True)
	eventinfo = ndb.StringProperty(required = True)
	location = ndb.GeoPtProperty(required = False)
	agereq = ndb.IntegerProperty(required = False)
	tags = ndb.StringProperty(required=False)
	profile = ndb.BlobProperty(required = False)