import firebase_admin
from firebase_admin import credentials, db
import datetime

cred = credentials.Certificate("C:/Users/sjmama/sjmama-c1a00-firebase-adminsdk-bi9q1-50b5eea227.json")
firebase_admin.initialize_app(cred,
                              {'databaseURL' : 'https://sjmama-c1a00-default-rtdb.firebaseio.com'})
datapath=''
ref=db.reference('')

class Sdata:
    def __init__(self, cam_no):
        self.cam_no=cam_no
        self.event_type=0
        self.link_storage=''
        self.date=''
        self.time=''
        

sdata=Sdata('0001')

now = datetime.datetime.now()
sdata.date=now.strftime("%Y-%m-%d")
sdata.time=now.strftime("%Hh%Mm%Ss")
date = now.strftime("%Y-%m-%d")
time = now.strftime("%Hh%Mm%Ss")
new_filename = f"{date}#{time}.mp4"

sdata.date=date
sdata.time=time
sdata.event_type=3
sdata.link_storage="https://sjmama1.s3.ap-northeast-2.amazonaws.com/2023-07-15%2304h08m25s.mp4"
sdata_dict=sdata.__dict__
print(sdata_dict)
ref.push(sdata_dict)
