from flask import Flask, render_template, request, jsonify
import json
import os

app = Flask(__name__)

class ChatBot:
    def __init__(self):
        self.responses = {}

    def respond(self, message):
        return self.responses.get(message.lower(), "I'm sorry, I don't understand.")

    def learn(self, message, response):
        self.responses[message.lower()] = response

    def save_responses(self):
        with open('responses.json', 'w') as file:
            json.dump(self.responses, file)

    def load_responses(self):
        if os.path.exists('responses.json'):
            with open('responses.json', 'r') as file:
                self.responses = json.load(file)

chatbot = ChatBot()
chatbot.load_responses()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_message = request.form['user_message']
    response = chatbot.respond(user_message)
    return jsonify({'response': response})

@app.route('/teach', methods=['POST'])
def teach():
    user_message = request.form['user_message']
    response = request.form['response']
    chatbot.learn(user_message, response)
    chatbot.save_responses()
    return jsonify({'message': 'Thank you for teaching me!'})

if __name__ == '__main__':
    app.run(port=3551, debug=True)
