from flask import Flask, render_template
import psycopg2
app = Flask(__name__)



@app.route('/')
def home_page():
    
    return render_template('index.html')

@app.route('/dashboard/')
def dashboard():
   # return("PLEASE GIVE ME THE FORM	")
    return render_template('dashboard.html')    

if __name__ == "__main__":
    app.run()