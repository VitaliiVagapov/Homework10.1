from flask import Flask

app = flask(__Name__)

@app.route('/')
def main():
    pass

@app.route('/candidates/<candidate_id>')
def candidate(candidate_id):
    pass

@app.route('/skills/<skill>')
def skills(skill):
    pass