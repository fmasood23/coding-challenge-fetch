from distutils.log import debug 
from fileinput import filename 
from flask import *  
import uuid
import json
import math

class Reciept:
    def __init__(self, points):
        self.id = uuid.uuid4()
        self.points=0
    
    def getId(self):
        return self.id

    def getPoints(self):
        return self.points

    def setPoints(self, new_p):
        self.points = self.points + new_p

    


app = Flask(__name__)


reciepts = []


@app.route('/')
def index():
    return render_template('index.html')


def create_obj(data):
    new_r = Reciept("temp")
    reciepts.append(new_r)
    
    for i in data:
        if i=="retailer":
            clean_name = [s for s in data["retailer"] if s.isalnum() or s.isspace()]
            cleaned = "".join(clean_name)
            clean = cleaned.replace(" ", "")
            counts = len(clean)
            new_r.setPoints(counts)
        elif i == "total":
            total_amt = data["total"]
            cents = int (total_amt.split(".")[1])
            if cents == 0:
                new_r.setPoints(50)
            if cents == 0 or cents ==25 or cents == 50 or cents ==75:
                new_r.setPoints(25)
        elif i=="purchaseDate":
            day = data["purchaseDate"]
            just_day = int (day.split("-")[2])
            if just_day % 2 == 1:
                 new_r.setPoints(6)
        elif i=="purchaseTime":
            time = data["purchaseTime"]
            hour = int (time.split(":")[0])
            minute = int (time.split(":")[1])
            if((hour>=14 and minute>=0 and hour<16) or (hour==16 and minute==0)):
                new_r.setPoints(10)
        elif i == "items":
            count = 0
            for j in data["items"]:
                count+=1
                name = j["shortDescription"].strip()
                price = float (j["price"])
                if len(name) %3 == 0:
                    value = price * 0.2
                    rounded = math.ceil(value)
                    new_r.setPoints(rounded)
            if count%2!=0:
                count-=1
            value = (count / 2) * 5
            new_r.setPoints(value)
    return new_r



@app.route('/receipts/process', methods = ('GET','POST'))   
def post_json():  
    id=""
    if request.method == 'POST': 
        f = request.files['file'] 
        f.save(f.filename)

        x = open(f.filename)
        data = json.load(x)

        new_r=create_obj(data) 
        id=new_r.getId()
    
    return jsonify(id=id)


@app.route('/receipts/<id>/points', methods = ['GET'])   
def get_json(id):  
    points=0
    for i in reciepts:
        id = str(id)
        current = str(i.getId())
        if current == id:
            print("true 1")
            points = i.getPoints()

    return jsonify(points=points)
       
      
  
if __name__ == '__main__':   
    app.run(debug=True)


