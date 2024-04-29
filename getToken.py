import requests

def getToken ():
    url = (f"https://opentdb.com/api_token.php?command=request")
    TOKEN = requests.get(url)
    return TOKEN