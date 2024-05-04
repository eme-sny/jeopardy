import requests 
import base64
from urllib.parse import unquote
from jeopardy.jeopardyVars import *
import random

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
       formatted_answer = format_answer(question_dict)
       email_formats = [formatted_question, formatted_answer]

    return(email_formats)

def parse_question (trivia_response):
    dailyQ = {}
    k = ['question', 'a1', 'a2', 'a3', 'a4']
    question = base64.b64decode(trivia_response['results'][0]['question']).decode('ASCII')
    incorrect_ans1 = base64.b64decode(trivia_response['results'][0]['incorrect_answers'][0]).decode('ASCII')
    incorrect_ans2 = base64.b64decode(trivia_response['results'][0]['incorrect_answers'][1]).decode('ASCII')
    incorrect_ans3 = base64.b64decode(trivia_response['results'][0]['incorrect_answers'][2]).decode('ASCII')
    correct_ans = base64.b64decode(trivia_response['results'][0]['correct_answer']).decode('ASCII')
    v = [question, correct_ans, incorrect_ans1, incorrect_ans2, incorrect_ans3]
    dailyQ = dict(zip(k,v))
    return(dailyQ)

def format_question (dailyQ):
    q_email_body = f"{dailyQ.get('question')}\n\na. {dailyQ.get('a1')}\nb. {dailyQ.get('a2')}\nc. {dailyQ.get('a3')}\nd. {dailyQ.get('a4')}"
    return q_email_body

def format_answer (dailyQ):
    q_email_body = f"Correct answer: {dailyQ.get('a1')}"
    return q_email_body

def shuffle_choices (question_dict):
    question = question_dict.get("question")
    correct_ans = question_dict.get("a1")
    question_dict.pop("question")
    answer_keys = list(question_dict.keys())
    answers = list(question_dict.values())
    random.shuffle(answers)
    answer_keys.append("question")
    answers.append(question)
    answers.append(correct_ans)
    randomized_question = dict(zip(answer_keys,answers))
    return randomized_question