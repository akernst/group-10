from google.appengine.ext import ndb


class Event(ndb.Model):
	eventname = ndb.StringProperty(required = True)
	datetime = ndb.DateTimeProperty(auto_now = True)
	eventinfo = ndb.StringProperty(required = True)
	location = ndb.GeoPtProperty(required = True)
	agereq = ndb.IntegerProperty(required = False)
	tags = ndb.StringProperty(required = True)
	dateadded = ndb.DateProperty(required = True)
	profile = ndb.BlobProperty(required = True)