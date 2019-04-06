from flask import *
from service import Service
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["SECRET_KEY"]="jasfijiosadjiof"

@app.route('/')
def homepage():
    return render_template('homepage.html')



@app.route("/all-service")
def all_service():
    if "logged" in session:
        if session["logged"]== True:

            person= Service.find()
            return render_template("all_service.html", all_service=person)
        else :
            return redirect("/login")
    else:
        return redirect("/login")
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
@app.route('/all-service/update/<id>', methods= ["GET","POST"]) 
def update(id):
    old_service=Service.find_one({'_id':ObjectId(id)})
    if request.method=="GET":
        return render_template('update.html', a=old_service )
    elif request.method == "POST":
        form= request.form
        service_name=form["input_name"]
        service_age=form["input_age"]
        service_gender=form["input_gender"]
        service_address=form["input_address"]
        service_height=form["input_height"]
        service_available=form["input_available"]
        new_value={
            "$set":{
                "name": service_name,
                "gender":service_gender,
                "age":service_age,
                "height":service_height,
                "available":service_available,
                "address":service_address
            }
        }
        Service.update_one(old_service,new_value)
        return redirect("/all-service/detail/{}".format(id))
@app.route('/login', methods=["GET","POST"])
def login():
    if session["logged"] == True:
        return redirect("/all-service")
    else:
        if request.method=="GET":
            return render_template("login.html")
        elif request.method =="POST":
            
            us="admin" 
            pw="admin"
            form = request.form
            username = form["input_username"]
            password = form["input_password"]
            if username == us and password == pw:
                session["logged"]= True
                return redirect("/all-service")
            else:
                # return "wrong password or username"
                return redirect("/login")
@app.route('/logout')   
def logout():
    if "logged" in session:
        session["logged"]= False
    return redirect("/login")

if __name__ == '__main__':
    app.run( debug=True)
 