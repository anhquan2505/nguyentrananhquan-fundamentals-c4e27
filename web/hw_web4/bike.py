from flask import *
from bson.objectid import ObjectId
from mlab import OurBikes
# from quan import bike
app = Flask(__name__)
@app.route('/newbike' , methods=['GET','POST'])
def xedap():
    if request.method=="GET":
        return render_template("new_bike.html")
    elif request.method == "POST":
        form= request.form
        bike_model=form["model"]
        bike_dailyfee=form["dailyfee"]
        bike_image=form["image"]
        bike_year=form["year"]
        
        new_value={
            
                "Model": bike_model,
                "Daily Fee":bike_dailyfee,
                "Image":bike_image,
                "Year":bike_year,
            }
        OurBikes.insert_one(new_value)
        return redirect("/newbike")
    


if __name__ == '__main__':
    app.run( debug=True)