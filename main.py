API_KEY='AIzaSyAj8Jg91bnOzLVefAMilnHQ8cM1khMAChM'

import google.generativeai as genai
import time
genai.configure(api_key=API_KEY)


generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 0,
  "max_output_tokens": 90000,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]
model =genai.GenerativeModel('gemini-pro',generation_config=generation_config,safety_settings=safety_settings)
chat=model.start_chat(history=[])
prompt=open('prompt.txt','r')
inst='\n'.join(prompt.readlines())
print(inst)
while 1:
    question = input('You: ')
    if question.strip() == '':
        break
    
    respone = chat.send_message(inst+'\n'+question)   
    print('\n')
    print("Bot: ")
    for i in respone.text:
        print(i,end='')
        time.sleep(0.0001)
    print('\n')
    inst=''