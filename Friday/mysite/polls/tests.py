import datetime

from django.utils import timezone
from django.test import TestCase

from polls.models import Poll

class PollMethodTests(TestCase):
	"""
	was_published_recently() should return False for polls whose
	pub_date is in the future
	"""

	future_poll = Poll(pub_date=timezone.now() + datetime.timedelta(days=30))
	self.assertEqual(future_poll.was_published_recently(),False)
	

# Create your tests here.
