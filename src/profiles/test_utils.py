import json

from django.test import TestCase

import mock

from .utils import get_youtube_subscriptions


class GetYoutubeSubscriptionsTest(TestCase):
    def setUp(self):
        self.dummy_content_dict = {
            'items': [
                {'snippet': {'title': 'Title 1'}},
                {'snippet': {'title': 'Title 2'}},
            ],
        }
        self.dummy_content_json = json.dumps(self.dummy_content_dict)

    @mock.patch('profiles.utils.requests')
    def test_successful_fetching_of_subscriptions(self, requests):
        """
        Using a valid token should return the list of channel names.
        """
        dummy_response = mock.MagicMock()
        dummy_response.status_code = 200
        dummy_response.content = self.dummy_content_json
        requests.get.return_value = dummy_response
        dummy_valid_token = 'token'

        result = get_youtube_subscriptions(dummy_valid_token)

        expected_number_of_channels = 2
        expected_channel_names = ['Title 1', 'Title 2']
        self.assertEqual(expected_number_of_channels, len(result))
        self.assertEqual(expected_channel_names, result)

    def test_invalid_token_used(self):
        """
        Using an invalid token should return an empty list.
        """
        dummy_response = mock.MagicMock()
        dummy_response.status_code = 400
        dummy_invalid_token = 'token'

        result = get_youtube_subscriptions(dummy_invalid_token)

        expected_channel_names = []
        self.assertEqual(result, expected_channel_names)
