from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/form_acknowledgement', methods=['POST'])
def acknowledge():
    name = request.form['your-name']
    email = request.form['your-email']
    return "Hi " + name + ", thank you for your message. We will respond to you as soon as possible at: " + email + "."