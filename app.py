from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Route for the homepage
@app.route('/')
def home():
    return render_template('home.html')

# Route for the about page
@app.route('/about')
def about():
    return render_template('about.html')

# Route for the projects page
@app.route('/projects')
def projects():
    projects = [
        {"title": "Web Development", "description": "Developed a fully functional e-commerce website."},
        {"title": "Data Analysis", "description": "Performed data analysis on financial reports using Python."},
        {"title": "Mobile App Development", "description": "Built a cross-platform mobile app using Flutter."},
        {"title": "To-Do-List App", "description": "A To-Do List App is a simple, user-friendly tool that helps you organize and manage tasks."},
        {"title": "Simple Calculator", "description": "A Simple Calculator in Python is a basic program that allows users to perform standard arithmetic operations."},
        {"title": "Weather App", "description": "A Weather App in Python fetches real-time weather data for a specific location."},
        {"title": "Expense Tracker", "description": "An Expense Tracker is a Python-based application that helps users manage their financial transactions."},
        {"title": "Number Guessing Game", "description": "A Number Guessing Game in Python where the computer selects a random number within a specified range."},
        {"title": "Simple Digital Clock", "description": "A Simple Digital Clock in Python displays the current time in a digital format."},
        {"title": "Investment Portfolio Tracker", "description": "An Investment Portfolio Tracker enables users to monitor and manage their investment portfolios."}
    ]
    return render_template('projects.html', projects=projects)

# Route for the contact page
@app.route('/contact')
def contact():
    return render_template('contact.html')

# Route for handling contact form submission
@app.route('/submit_contact', methods=['POST'])
def submit_contact():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    
    # Process the data (e.g., send email, store in the database)
    print(f"Received contact form: {name}, {email}, {message}")
    
    return redirect(url_for('thank_you'))

# Thank you page after form submission
@app.route('/thank_you')
def thank_you():
    return "<h1>Thank you for contacting me. I'll get back to you soon!</h1>"

if __name__ == "__main__":
    app.run(debug=True)


