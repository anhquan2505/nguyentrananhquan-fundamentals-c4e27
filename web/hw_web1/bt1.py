from flask import Flask, render_template, redirect
app = Flask(__name__)

@app.route('/about_me')
def about_me():
    mes = {
        "name" : "Nguyễn Trần Anh Quân",
        "age" : 19,
        "school": "HUST",
        "gender":"male"}
    return render_template("me.html", me = mes)
# @app.route('/')
# def index():
#     return ('bitch thai')
@app.route('/school')
def school():
    return redirect("http://techkids.vn", code=302)
# @app.route('/say_hi/<int:a>/<int:b>')
# def say_hi(a,b):
     
#     return str(a+b)


if __name__ == '__main__':
    app.run(debug=True)