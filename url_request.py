#Define a function do_search(bookstore_url, params) that takes the url of the store bookstore_url and the dictionary of 
#the search parameters params, sends a GET request to the page with the search results and returns the response object.

#Note that you do not need to read any input or call the function do_search() yourself.

#Source: JetBrains Academy

import requests

def do_search(bookstore_url, params):
    # First, I need to generate the url
    request_url = "{}?author={}&title={}".format(bookstore_url, params['author'], params['title'])
    #Then, return the response
    return requests.get(request_url)
