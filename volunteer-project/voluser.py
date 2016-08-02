from google.appengine.ext import ndb


class VolUser(ndb.Model):
	name = ndb.StringProperty(required = True)
	email = ndb.StringProperty(required = True)
	age = ndb.IntegerProperty(required = False)
	organizationinfo = ndb.StringProperty(required = False)
	avatar = ndb.BlobProperty(required = False)