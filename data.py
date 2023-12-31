

import requests 

parameters= {"amount": 10,
             "difficulty": "easy",
             "type": "boolean" 
             }

response= requests.get(url= "https://opentdb.com/api.php", params= parameters)
response.raise_for_status()
data= response.json()
question_data= (data["results"])   # we only want the result key 
print(question_data)
