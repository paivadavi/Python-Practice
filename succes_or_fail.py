import requests

# Define a function check_success(url) that, given a URL, sends out a GET request and returns "Success" if it succeeds and "Fail" otherwise.

def check_success(url):
    response = requests.get(url)
    if response:
        # Will be True is the response status code is 
        # 2xx (request accepted) or 3xx (redirection)
        return "Success"
    else:
        return "Fail"
