from flask import Flask, render_template, Response, g, current_app as app

app = Flask(__name__)

import os



app = Flask(__name__)



@app.route('/')
def page():
   return render_template('index.html')

@app.route('/live')
def status():
    return render_template('responsive.html', dome1=dome1, dome2=dome2, dome3=dome3, dome4=dome4, domeR1=domeR1, domeR2=domeR2, domeR3=domeR3, domeR4=domeR4)



if __name__ == '__main__':
    app.run(debug=True)


 

