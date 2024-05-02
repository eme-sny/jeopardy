import requests 
import base64
from urllib.parse import unquote
from jeopardy.jeopardyVars import *
from random import randrange

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
       question_dict = parse_question(data)
       shuffled_question = shuffle_choices(question_dict)
       formatted_question = format_question(shuffled_question)
    return(formatted_question)

def parse_question (trivia_response):
    dailyQ = {}
    k = ['question', 'correct_a', 'incorrect_a1', 'incorrect_a2', 'incorrect_a3']
    question = base64.b64decode(trivia_response['results'][0]['question']).decode('ASCII')
    incorrect_ans1 = base64.b64decode(trivia_response['results'][0]['incorrect_answers'][0]).decode('ASCII')
    incorrect_ans2 = base64.b64decode(trivia_response['results'][0]['incorrect_answers'][1]).decode('ASCII')
    incorrect_ans3 = base64.b64decode(trivia_response['results'][0]['incorrect_answers'][2]).decode('ASCII')
    correct_ans = base64.b64decode(trivia_response['results'][0]['correct_answer']).decode('ASCII')
    v = [question, correct_ans, incorrect_ans1, incorrect_ans2, incorrect_ans3]
    dailyQ = dict(zip(k,v))
    return(dailyQ)

def format_question (dailyQ):
    q_email_body = f"{dailyQ.get('question')}\n\na. {dailyQ.get('correct_a')}\nb. {dailyQ.get('incorrect_a1')}\nc. {dailyQ.get('incorrect_a2')}\nd. {dailyQ.get('incorrect_a3')}"
    return q_email_body

def shuffle_choices (question_dict):
    print(question_dict)
    question_dict.pop("question")
    print(question_dict)
    c = 0
    sorts = randrange(25)
    #while c < sorts:
    keys = question_dict.keys()
    print(keys)
    index = randrange(4)
    print(index)
    shufffle_key = question_dict[index]
    #print(shufffle_key)
    #question_dict.pop(index)
    #  question_dict.append(keys[2])
    #  c += 1
    #  print(question_dict)
    return(question_dict)