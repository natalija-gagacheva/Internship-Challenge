from flask import Flask, request, jsonify

app = Flask(__name__)

adminSkills = ['Python', 'relational database', 'Software engineering', 'data science', 'NLP', 'natural language processing']

#Implementing match method
def matchMethod(userSkill):
    return [skill for skill in adminSkills if skill == userSkill]

@app.route('/')
def home():
    return "Connection is successful"

#this method only accepts post requests submitted by the client
@app.route('/match-methods', methods=['POST'])
def matchingMethods():
    #extracting data sent by the user
    userData = request.json
    #extracting the specific skill sent by user
    userSkill = userData.get('skill')

    matchResult = matchMethod(userSkill)

    # creating a dictionary that stores the skill submitted by the user and results from both methods
    dict = {
        'user input': userSkill,
        'exact matches': matchResult,
    }

    # convert the response into a JSON file so the client will be able to recieve the result.
    return jsonify(dict)

#this part of the code starts the Flask web server
if __name__ == '__main__':
    app.run(debug=True)

