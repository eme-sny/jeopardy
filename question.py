import requests 

# api documentation: https://opentdb.com/api_config.php
def get_question ():
    url = f"https://opentdb.com/api.php?amount=1"
    response = requests.get(url)
  #  if response.response_code == 0: 
    data = response.json()
    question = data['results'][0]['question']
    # need to correct special characters 
    return(question)

