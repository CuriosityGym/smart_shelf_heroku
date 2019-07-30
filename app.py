from flask import Flask, render_template, Response, g, current_app as app

app = Flask(__name__)

import os



app = Flask(__name__)



@app.route('/')
def page():
   return render_template('index.html')

@app.route('/dashboard')
def status():
    return render_template('dashboard.html')



if __name__ == '__main__':
    app.run(debug=True)


 

