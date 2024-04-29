import requests 
import base64
from getToken import *

# api documentation: https://opentdb.com/api_config.php
def get_question ():
    TOKEN = str(getToken())
    k = ['question', 'answer']
    url = str(f"https://opentdb.com/api.php?amount=1&type=multiple&encode=base64&token=")
    req = url + TOKEN
    print(req)
    response = requests.get(url)
    data = response.json()
    res_code = data['response_code']
    if res_code == 0: 
      question = base64.b64decode(data['results'][0]['question'])
      answer = base64.b64decode(data['results'][0]['correct_answer'])
      v = [question, answer]
      dailyQ = dict(zip(k,v))
    else:
       print("failed to get question")
    return(dailyQ)

