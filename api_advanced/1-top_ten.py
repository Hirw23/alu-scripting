#!/usr/bin/python3

"""
This module contains a function that queries the Reddit API and 
returns the top 10 hot posts for a given subreddit.
"""

import requests

def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of
    the top 10 hot posts for a given subreddit.
    
    Args:
        subreddit (str): The name of the subreddit to query.
    
    Returns:
        None: Prints the titles of the top 10 hot posts or
        None if the subreddit is invalid.
    """
