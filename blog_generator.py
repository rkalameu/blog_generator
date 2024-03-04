
import openai
from dotenv import dotenv_values
config = dotenv_values(".env")

openai.api_key = config['API_KEY']

def generate_blog(paragraph_topic):
 response =openai.Completion.create ( 
 model = "davinci-002",   
 prompt = 'Write a paragraph about the following topic. ' + paragraph_topic,
 max_tokens = 200,
 temperature = 0.7
 )

 retrieve_blog = response.choices[0].text

 return (retrieve_blog)

keep_writing = True
while keep_writing == True:
 answer = str(input('Write a paragraph? Y for yes, anything else for no. '))
 if answer == 'y':
   paragraph_topic = str(input('What should this paragraph talk about? '))
   print(generate_blog(paragraph_topic))
 else:
  keep_writing = False
  