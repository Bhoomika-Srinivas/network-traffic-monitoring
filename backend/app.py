from flask import Flask, render_template, request, redirect, session, jsonify
from flask_sqlalchemy import SQLAlchemy
from capture import capture_packets, get_latest_stats

app = Flask(__name__)
app.secret_key = "supersecretkey"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///traffic.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

class Traffic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    packets = db.Column(db.Integer)
    upload_speed = db.Column(db.Float)
    download_speed = db.Column(db.Float)

@app.route('/')
def home():
    if 'user' in session:
        return redirect('/dashboard')
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    user = User.query.filter_by(username=request.form['username']).first()
    if user and user.password == request.form['password']:
        session['user'] = user.username
        return redirect('/dashboard')
    return "Invalid credentials"

@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect('/')
    return render_template('dashboard.html')

@app.route('/traffic-data')
def traffic_data():
    stats = get_latest_stats()
    return jsonify(stats)

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, host="0.0.0.0", port=5000)
