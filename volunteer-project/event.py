from google.appengine.ext import ndb


class Event(ndb.Model):
	eventname = ndb.StringProperty(required = True)
	eventdate = ndb.StringProperty(required = True)
	datetime = ndb.DateTimeProperty(auto_now = True)
<<<<<<< HEAD
	eventinfo = ndb.StringProperty(required = False)
	location = ndb.StringProperty(required = False)
	agereq = ndb.IntegerProperty(required = False)
	tags = ndb.StringProperty(required = True)
=======
	eventdate = ndb.StringProperty(required=True)
	eventinfo = ndb.StringProperty(required = True)
	location = ndb.GeoPtProperty(required = False)
	agereq = ndb.IntegerProperty(required = False)
	tags = ndb.StringProperty(required=False)
>>>>>>> 665e6aec4c8f7152cc027917eafd5fa513b873ed
	profile = ndb.BlobProperty(required = False)