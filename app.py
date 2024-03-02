import os
from flask import Flask, request, render_template

# Create Flask App
app = Flask(__name__)

# Calculator Logic
def calculate(operation, num1, num2):
    """
    Function to perform calculations based on the operation and operands provided.
    """
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Error! Division by zero."
        else:
            return num1 / num2

# Route for Home Page
@app.route('/', methods=['GET', 'POST'])
def home():
    """
    View function for the home page, handles both GET and POST requests.
    """
    if request.method == 'POST':
        operation = request.form.get('operation')
        num1 = float(request.form.get('num1'))
        num2 = float(request.form.get('num2'))
        result = calculate(operation, num1, num2)
        return render_template('index.html', result=result)
    return render_template('index.html', result="Enter your calculation")

# Main Block
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Retrieve port number from environment variable for Heroku deployment
    app.run(host='0.0.0.0', port=port)  # Run Flask app on specified host and port

