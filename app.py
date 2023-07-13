from flask import Flask,render_template,url_for,request
from summarize import summariz
app=Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summary',methods=['POST'])
def summary():
    if request.method == 'POST':
        message = request.form['message']
        summary = summariz(message)
        return render_template('result.html', answer=summary)

if __name__=="__main__":
    app.run(debug=True)

