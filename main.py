from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/form_acknowledgement', methods=['POST'])
def acknowledge():
    email = request.form['your-email']
    return "Thank you for your message. Your email address is: " + email