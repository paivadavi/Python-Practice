import requests

# Define a function get_content_type(url) that, given a URL, sends a GET request and returns the content type of the response.

def get_content_type(url):
    response = requests.get(url)
    return response.headers['content-type']
