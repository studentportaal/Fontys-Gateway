import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import google.cloud
from user import User

project_id = 'pts6-bijbaan'
cred = credentials.ApplicationDefault()
firebase_admin.initialize_app(cred, {
    'projectId': project_id
})

db = firestore.client()


def get_user(username):
    doc_ref = db.collection(u'users').document(username)

    try:
        doc = doc_ref.get()
        if doc.exists():
            print(doc.to_dict())
            u = User.from_dict(doc.to_dict())
            return u
        else:
            return None

    except google.cloud.exceptions.NotFound:
        print(u'No such document!')


def create_user(name, data):
    db.collection.document(u'' + name).set(data)
