from flask import Flask, render_template,request
Flask_App=Flask(__name__)
@Flask_App.route('/',methods=['GET'])
def index():
    return render_template('second.html')
@Flask_App.route('/operation_result/',methods=['POST'])
def operation_result():
    first_input = request.form['a']
    second_input = request.form['b']
    operation = request.form['operation']
    try:
        a=float(first_input)
        b=float(second_input)
        if operation =="+":
            result=a+b
        elif operation =="-":
            result=a-b
        elif operation == "*":
            result = a * b
        elif operation == "/":
            result = a / b
        elif operation=="%":
            operation == "%"
            result = a % b
        else:
            operation=="**"
            result=pow(a,b)
        return render_template('second.html',a=a,b=b,operation=operation,result=result,caliculation_success=True)
    except ZeroDivisionError:
        return render_template('second.html',a=a,b=b,operation=operation,result="bad input",caliculation_success=False,error="you cannot divide by zero")
    except ValueError:
        return render_template('second.html',a=a,b=b,operation=operation,result="bad input",caliculation_success=False,error="cannot peform numeric operations wth given details")


if __name__=='__main__':
    Flask_App.debug=True
    Flask_App.run()

