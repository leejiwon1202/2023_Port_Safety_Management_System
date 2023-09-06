import firebase_admin
from firebase_admin import credentials, db
import datetime

cred = credentials.Certificate("C:/Users/sjmama/sjmama-c1a00-firebase-adminsdk-bi9q1-50b5eea227.json")
firebase_admin.initialize_app(cred,
                              {'databaseURL' : 'https://sjmama-c1a00-default-rtdb.firebaseio.com'})

class Sdata:
    def __init__(self, cam_no):
        self.cam_no=cam_no
        self.event_type=0
        self.link_storage=''
        self.date=''
        self.time=''
