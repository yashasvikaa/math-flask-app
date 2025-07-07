from flask import Flask, render_template, request
from Maths.mathematics import summation, subtraction, multiplication

app = Flask("Mathematics Problem Solver")

@app.route("/")
def render_index_page():
    return render_template('index.html')

def get_numbers_from_request():
    """Extracts and coverts num1 and num2 from the query string."""
    num1_raw = request.args.get('num1')
    num2_raw = request.args.get('num2')

    if num1_raw is None or num2_raw is None:
        raise ValueError("Both 'num1' and 'num2' parameter.")

    try:
        num1 = float(num1_raw)
        num2 = float(num2_raw)
    except ValueError:
        raise ValueError("Missing 'num1' or 'num2' parameter")

    return num1, num2

@app.route("/sum")
def sum_route():
    try: 
        num1, num2 = get_numbers_from_request()
        result = summation(num1, num2)
        return str(int(result)) if result.is_integer() else str(result)
    except ValueError as e:
        return f"Error: {str(e)}", 400

@app.route("/sub")
def sub_route():
    try: 
        num1, num2 = get_numbers_from_request()
        result = subtraction(num1, num2)
        return str(int(result)) if result.is_integer() else str(result)
    except ValueError as e:
        return f"Error: {str(e)}", 400

@app.route("/mul")
def mul_route():
    try: 
        num1, num2 = get_numbers_from_request()
        result = multiplication(num1, num2)
        return str(int(result)) if result.is_integer() else str(result)
    except ValueError as e:
        return f"Error: {str(e)}", 400

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port=8080)
