#!/usr/bin/python3

import requests


def recurse(subreddit, hot_list=[], after=""):
    """
    Queries the Reddit API and returns a list containing the titles of all hot
    articles for a given subreddit. If no results are found for the given
    subreddit, the function should return None.
    """
    # Make a request to the Reddit API to get the subreddit information
    response = requests.get(
        f"https://www.reddit.com/r/{subreddit}/hot.json",
        headers={"User-Agent": "Mozilla/5.0"},
        allow_redirects=False,
        params={"after": after}
    )

    # Check response if it was successful and not  redirect
    if response.status_code != 200 or response.is_redirect:
        return None

    # Parse the JSO response to get the number of subscribers
    try:
        data = response.json()
        for post in data["data"]["children"]:
            hot_list.append(post["data"]["title"])
        after = data["data"]["after"]
        if after is None:
            return hot_list
        return recurse(subreddit, hot_list, after)
    except (KeyError, ValueError):
        return None
