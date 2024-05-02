import requests 
import base64
from jeopardy.jeopardyVars import *

# api documentation: https://opentdb.com/api_config.php
def get_question ():
    TOKEN = str(getToken())
    url = str(f"https://opentdb.com/api.php?amount=1&type=multiple&encode=base64&token=")
    req = url + TOKEN
    response = requests.get(req)
    data = response.json()
    res_code = data['response_code']
    if res_code != 0: 
       print("failed to get question")
    else: 
       print("got new question")
    return(data)
    

def parse_question (trivia_response):
    dailyQ = {}
    #k = ['question', 'correct_a', 'incorrect_a']
    k = ['question', 'correct_a']
    question = base64.b64decode(trivia_response['results'][0]['question'])
    #incorrect_ans = base64.b64decode(trivia_response['results'][0]['incorrect_answers'])
    #print(incorrect_ans)
    correct_ans = base64.b64decode(trivia_response['results'][0]['correct_answer'])
    #v = [question, correct_ans, incorrect_ans]
    v = [question, correct_ans]
    dailyQ = dict(zip(k,v))
    return(dailyQ)