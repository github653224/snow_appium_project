from django.test import TestCase
from sign.models import Event,Guest
# Create your DjangoTests here.
class MedelTest(TestCase):
    def setUp(self):
        Event.objects.create(
            id=7,
            conference_name="oneplus 3 event",
            status=True,
            limit=300,
            address="shenzhen",
            start_time="2018-01-20 14:00:00",)
        Guest.objects.create(
            id=8,
            event_id=7,
            realname="alenka",
            phone="13711001109",
            email="laien@email.com",
            sign=False)

    def test_event_models(self):
        result = Event.objects.get(conference_name="oneplus 3 event")
        self.assertEqual(result.address, "shenzhen")
        self.assertTrue(result.status)

    def test_guest_models(self):
        result = Guest.objects.get(phone='13711001109')
        self.assertEqual(result.realname, "alenka")
        self.assertFalse(result.sign)










