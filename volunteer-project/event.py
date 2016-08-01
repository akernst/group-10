from google.appengine.ext import ndb


class Event(ndb.Model):
	name = ndb.StringProperty(required = True)
	datetime = ndb.DateTimeProperty(required = True)
	eventinfo = ndb.StringProperty(required = True)
	location = ndb.IntegerProperty(required = True)
	agereq = ndb.IntegerProperty(required = False)
	tags = ndb.StringProperty(required = True)
	dateadded = ndb.DateProperty(required = True)
	profile = ndb.BlobProperty(required = True)