#!/usr/bin/python3
import requests


def number_of_subscribers(subreddit):
    """
        Returns the number of subscribers for a given subreddit
        If the subreddit is invalid, return 0
    """
    # Make a request to the Reddit API to get the sureddit information
    response = requests.get(
        f"https://www.reddit.com/r/{subreddit}/about.json",
        headers={"User-Agent": "Mozilla/5.0"},
        allow_redirects=False
    )

    # Check response if it was successful and not  redirect
    if response.status_code != 200 or response.is_redirect:
        return 0

    # Parse the JSO response to get the number of subscribers
    try:
        data = response.json()
        return data["data"]["subscribers"]
    except (KeyError, ValueError):
        return 0
