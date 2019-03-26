from flask import Flask, render_template
app = Flask(__name__)

   
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
@app.route('/poem')
def poem():
    return render_template("poem.html", poems = poems)

@app.route('/poem/<int:index>')
def detail(index):
    poem = poems[index-1]    
    return render_template('poem_detail.html', poem=poem, index = index )

     
    


if __name__ == '__main__':
    app.run(debug=True)

 