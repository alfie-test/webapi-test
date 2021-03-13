from flask import abort, jsonify, request, Flask

app = Flask(__name__)

@app.route('/GET')
def index():

    # Return 400 if no input
    if not'int' in request.args :
        code = 400
        msg = "Please provide an integer input"
        return jsonify(msg), code

    #Check input is int
    if not str(request.args.get('int')).isnumeric():
        code = 400
        return jsonify("Please input an integer"), code

    # Initiate vars once prechecks are complete    
    res = ""
    num = int(request.args.get('int'))

    # Check If multipes
    if num % 7 == 0 and num % 9 == 0:
        res = "EG"

    elif num % 7 == 0:
        res = "E"
    
    elif num % 9 == 0:
        res = "G"
    
    # If no multiple, return original number
    else:
        return jsonify(num)

    # Return response
    return jsonify(res)