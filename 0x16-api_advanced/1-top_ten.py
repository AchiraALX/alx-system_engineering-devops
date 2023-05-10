#!/usr/bin/python3
import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts listed for a given subreddit
    """
    # Make a request to the Reddit API to get the subreddit information
    response = requests.get(
        f"https://www.reddit.com/r/{subreddit}/hot.json",
        headers={"User-Agent": "Mozilla/5.0"},
        allow_redirects=False,
        params={"limit": 10}
    )

    # Check response if it was successful and not  redirect
    if response.status_code != 200 or response.is_redirect:
        print(None)
        return

    # Parse the JSO response to get the number of subscribers
    try:
        data = response.json()
        for post in data["data"]["children"]:
            print(post["data"]["title"])
    except (KeyError, ValueError):
        print(None)
        return
