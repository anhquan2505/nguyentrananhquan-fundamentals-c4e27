from flask import Flask, render_template
app = Flask(__name__)

@app.route('/poem')
def poem():
    # poem_title  ="thơ con cóc"
    # poem_content = "hôm nay trăng lên cao quá"
    # poem_arthor =  "Quân Quý Tộc"
    poems = [{
            "title" : "thơ con cóc",
            "content" : "hôm nay trăng sáng quá",
            "arthor": "Quân Quý Tộc",
            "gender":"male"
    },     {
            "title" : "thơ con ếch",
            "content" : "chó thái",
            "arthor": "thái óc",
            "gender":"female"}]
    return render_template("poem.html", poems = poems)
@app.route('/')
def index():
    return ('bitch thai')
@app.route('/say_hi/<int:a>/<int:b>')
def say_hi(a,b):
     
    return str(a+b)


if __name__ == '__main__':
    app.run(debug=True)

 