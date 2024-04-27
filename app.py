from flask import url_for, Flask, request, jsonify,render_template
import google.generativeai as genai
import time

API_KEY='AIzaSyAj8Jg91bnOzLVefAMilnHQ8cM1khMAChM'
genai.configure(api_key=API_KEY)


generation_config = {
  "temperature": 1,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 9000,
  "stop_sequences": [
    "be safe ",
  ],
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


model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

i=0
app = Flask(__name__)  # create an app instance


@app.route("/")
def index():
    bot_img=url_for('static', filename='hat.png')
    usr_img=url_for('static', filename='user.png')
    return render_template('index.html',bot_img=bot_img,usr_img=usr_img)


@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    input = msg
    return get_chat_response(input)


H=[{'role': 'user','parts':['hi']},{'role':'model','parts':['hi']}]

def get_chat_response(question,history=H):


    global i
    
    prompt=open('prompt.txt','r')
    inst=prompt.read()
    generation_config = {"temperature": 1,"top_p": 0.95,"top_k": 0,"max_output_tokens": 90000,}
    prompt.close()
    
    
    chat=model.start_chat(history=history)


    if i==0: 
        chat.send_message(inst)
    respone = chat.send_message(question)
    i+=1
    H[-1]={'role':'user','parts':[question]}
    H[-1]={'role':'model','parts':[respone.text]}
    return respone.text


if __name__=='__main__':  # on running python app.py
    app.run()  # run the flask app