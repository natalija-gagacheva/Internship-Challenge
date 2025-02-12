#Importing Flask so we can be able to create web applications that accept HTTP requests
from flask import Flask, request, jsonify
from difflib import get_close_matches

#We create a web app instance where this script is the main app.
app = Flask(__name__)

ADMIN_SKILLS = ['Python', 'relational database', 'Software engineering', 'data science', 'NLP',
                'natural language processing']


#Implementing match methods
def exact_match(userSkill):
    return [skill for skill in ADMIN_SKILLS if skill.lower() == userSkill.lower()]


def partial_match(userSkill):
    return get_close_matches(userSkill, ADMIN_SKILLS)

#Routing
@app.route('/')
def home():
    return "Flask API is running!"

#this method only accepts post requests submitted by the client
@app.route('/match', methods=['POST'])
def match_skill():
    #extracting data sent by the user
    userData = request.json
    #extracting the specific skill sent by user
    userSkill = userData.get('skill_name')

    #checks if the user skill exists. Throws error if doesn't exist
    if not userSkill:
        return jsonify({'error': 'Skill name is required'}), 400

    #running the match methods
    exactMatchResults = exact_match(userSkill)
    partialMatchResults = partial_match(userSkill)

    #creating a response dictionary that stores the skill submitted by the user
    #and results from both methods
    responseDictionary = {
        'user input': userSkill,
        'exact matches': exactMatchResults,
        'partial matches': partialMatchResults
    }

    #converts the response into a JSON file so the client will be able
    #to recieve the result. JSON is the standard format for web APIs and is easily processed by web apps
    return jsonify(responseDictionary)

#this part of the code starts the Flask web server
if __name__ == '__main__':
    app.run(debug=True)