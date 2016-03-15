from pprint import pprint

import json

import requests

YOUTUBE_SUBSCRIPTIONS_API = 'https://www.googleapis.com/youtube/v3/subscriptions'


def get_youtube_subscriptions(access_token, max_results=50):
    """
    Use `access_token` from a <User> that logged in via Google to
    fetch channel names from subscriptions of their Youtube account.
    """
    params = {
        'part': 'snippet',
        'access_token': access_token,
        'mine': True,
        'maxResults': max_results,
    }
    response = requests.get(YOUTUBE_SUBSCRIPTIONS_API, params)
    channel_names = []

    if response.status_code == 200:
        response_as_dict = json.loads(response.content)
        channel_names = [
            item['snippet']['title']
            for item in response_as_dict['items']
        ]
    else:
        response_as_dict = json.loads(response.content)
        pprint(response_as_dict)

    return channel_names
