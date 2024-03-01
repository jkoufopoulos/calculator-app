from flask import Flask, request, render_template

app = Flask(__name__)

def calculate(operation, num1, num2):
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

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        operation = request.form.get('operation')
        num1 = float(request.form.get('num1'))
        num2 = float(request.form.get('num2'))
        result = calculate(operation, num1, num2)
        return render_template('index.html', result=result)
    return render_template('index.html', result="Enter your calculation")

if __name__ == '__main__':
    app.run(debug=True)
