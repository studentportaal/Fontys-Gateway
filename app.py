from flask import Flask
from flask import request
from flask_cors import CORS, cross_origin

import user
import storage
import requests
import json
import broker

app = Flask(__name__)
cors = CORS(app)


# Will have before first request once messagebroker gets introduced
def connect_pub_sub():
    broker.connect()


@app.route('/')
def health():
    return 'healthy'


@app.route('/message')
def message():
    broker.send_message()
    return 'sent message to generic gateway'


@app.route('/login')
@cross_origin()
def login():
    # requests the access token from the identity server
    auth_code = request.args.get('authorization')
    data = {'client_secret': 'Ohi65lAzsj07KiAJ0G6HsJq7YdnBYRVDoa11RNxK', 'client_id': 'i354549-jobbybyomm',
            'grant_type': 'authorization_code', 'code': auth_code, 'redirect_uri': 'https://vaifreecams.com'}
    r = requests.post('https://identity.fhict.nl/connect/token', data)
    response = r.json()

    # requests the information of the authenticated user
    header = {'Authorization': 'Bearer ' + response['access_token']}
    user_data = requests.get('https://api.fhict.nl/people/me', headers=header)
    person = user_data.json()
    payload = json.dumps(user_data.json())

    # requests information about this user from the Jobby server
    head = {'Content-Type': 'application/json'}
    profile = requests.post('http://localhost:9000/users/{}/profile'.format(person['mail']), data=payload, headers=head)
    print(profile.status_code)

    if profile.status_code == 200:
        user_profile = profile.json()
        return json.dumps(user_profile)
    else:
        return 'something went wrong'


if __name__ == '__main__':
    app.run()
