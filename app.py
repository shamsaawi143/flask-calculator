from flask import  Flask, render_template, request
app = Flask(__name__)
@app.route("/", methods=["GET","POST"])
def calculator():
    result = None
    if request.method == "POST":
        num1 = int(request.form["num1"])
        num2 = int(request.form["num2"])
        operation = request.form["operation"]
        
        if operation == "add":
            result = num1 + num2
        elif operation == "sub":
            result = num1 - num2    
        elif operation == "mul":
            result = num1 * num2    
        elif operation == "div":
            result = num1 / num2

    return render_template("index.html",result=result)
if __name__ == "__main__":
    app.run(debug=True)            