from flask import Flask, render_template, redirect
from service import Service
from bson.objectid import ObjectId

app = Flask(__name__)

all_services = []
@app.route('/')
def homepage():
    return render_template('homepage.html')
@app.route("/all-service")
def all_service():
    person= Service.find()
    return render_template("all_service.html", all_service=person)
@app.route("/all-service/detail/<id>")
def detail(id):
    detail_person = Service.find_one({'_id': ObjectId(id)})
    
    return render_template("detail.html", detail_person=detail_person)
@app.route('/all-service/<g>')
def gender(g):
    Servicess = Service.find({"gender":g})
    return render_template("all_service.html", all_service= Servicess)
@app.route('/all-service/delete/<id>')
def delete(id):
    Service.find_one_and_delete({"_id":ObjectId(id)})
    
    return redirect("/all-service")
if __name__ == '__main__':
    app.run( debug=True)
 