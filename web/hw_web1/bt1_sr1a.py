from flask import Flask, render_template
app = Flask(__name__)


@app.route("/BMI/<int:weight>/<int:height>")
def BMI(weight,height):
    change= height/100
    bmi = (weight/(change*change))
    if bmi < 16 : 
        return ("chỉ số bmi là: "+ str(bmi)+"  ==> Severely underweight")
    elif bmi < 18.5 and bmi >= 16 : 
        return ("chỉ số bmi là: " +str(bmi) +"  ==> Underweight")
    elif bmi < 25 and bmi >= 18.5  :
        return("chỉ số bmi là: "+ str(bmi)+"  ==> Normal")
    elif bmi < 30 and bmi >= 25 : 
        return ("chỉ số bmi là: "+str(bmi)+"  ==> Overweight")
    else: 
        return ("chỉ số bmi là: " +str(bmi)+"  ==> Obese")





if __name__ == '__main__':
    app.run(debug=True)