import os
from flask import Flask, render_template

# create the app
app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "dev-secret-key")

@app.route('/')
def home():
    """Serve the portfolio homepage"""
    return render_template('home.html', current_page='home')

@app.route('/about')
def about():
    """Serve the about page"""
    return render_template('about.html', current_page='about')

@app.route('/experience')
def experience():
    """Serve the experience page"""
    return render_template('experience.html', current_page='experience')

@app.route('/projects')
def projects():
    """Serve the projects page"""
    return render_template('projects.html', current_page='projects')

@app.route('/contact')
def contact():
    """Serve the contact page"""
    return render_template('contact.html', current_page='contact')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
