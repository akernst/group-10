from google.appengine.ext import ndb


class Event(ndb.Model):
	eventname = ndb.StringProperty(required = True)
	eventdate = ndb.StringProperty(required = True)
	datetime = ndb.DateTimeProperty(auto_now = True)
	eventinfo = ndb.StringProperty(required = True)
	location = ndb.StringProperty(required = True)
	zipcode = ndb.IntegerProperty(required = True)
	agereq = ndb.IntegerProperty(required = True)
	tags = ndb.StringProperty(required= False)
	profile = ndb.BlobProperty(required = False)
	signedUp = ndb.StringProperty(repeated = True)
	creator = ndb.StringProperty(required = True)