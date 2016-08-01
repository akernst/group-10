from google.appengine.ext import ndb


class User(ndb.Model):
	name = ndb.StringProperty(required = True)
	email = ndb.StringProperty(required = True)
	age = ndb.IntegerProperty(required = True)
	organizationinfo = ndb.StringProperty(required = False)