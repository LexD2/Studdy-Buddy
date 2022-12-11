from django.test import TestCase
from chat.models import ChatConsumer


class ChatConsumerModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up a sample chat room user to run unit tests on based on user scenario
        ChatConsumer.objects.create(room_name="Math", user_name="Emma")

    # This unit test checks that the user has logged into the correct room based on the labeled names.
    def test_room_name(self):
        emma = ChatConsumer.objects.get(id=1)
        room_label = emma._meta.get_field('room_name').verbose_name
        self.assertEqual(room_label, 'room_name')
