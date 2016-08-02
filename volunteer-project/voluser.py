from google.appengine.ext import ndb
from google.appengine.api import users


class VolUser(ndb.Model):
	avatar = ndb.BlobProperty(required = False)
	user_id = ndb.StringProperty(required = True)