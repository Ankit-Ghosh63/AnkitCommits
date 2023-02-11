from flask import Flask , request,jsonify,render_template

app=Flask(__name__) #defining app name

#Route
@app.route('/') #Home Page
def hello_world():
    return render_template("index.html")

@app.route('/aboutus') #about us page
def aboutus():
    return 'We are ineuron'

@app.route('/demo',methods=['POST']) #POST request code
def math_operation():
    if(request.method == 'POST'):
        operation=request.json['operation']
        num1=request.json['num1']
        num2=request.json['num2']
        result = 0

        if operation == 'add':
            result = num1 + num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'division':
            result = num1/num2
        else:
            result = num1 - num2

        return jsonify(f'The operation is {operation} and the result is {result}')

@app.route('/multiply',methods=['POST']) #POST request code
def multiply():
    if(request.method == 'POST'):
        operation=request.json['operation']
        num1=request.json['num1']
        num2=request.json['num2']
        result = num1 * num2

        return jsonify(f'The operation is {operation} and the result is {result}')


@app.route('/operation',methods=['POST']) #POST request code
def operation():
    if(request.method == 'POST'):
        operation=request.form['operation']
        num1= int(request.form['num1'])
        num2= int(request.form['num2'])
        result = 0

        if operation == 'add':
            result = num1 + num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'division':
            result = num1/num2
        else:
            result = num1 - num2
            
        return render_template("results.html",result = result)

if __name__=="__main__":
    app.run(host='0.0.0.0',port=5000)


