from email.policy import default
from apihelpers import get_display_results, verify_endpoints_info
from flask import Flask, request, make_response
import json
import dbcreds

app = Flask(__name__)

# get all the candies from the database
@app.get('/api/candy')
def all_candies():
    # it does not need any of the params
    results = get_display_results('call all_candies()',[])
    return make_response(json.dumps(results,default=str),200)

# post a new candy into a database
@app.post('/api/candy')
def add_candy():
    # it will verify the required data for a request
    invalid = verify_endpoints_info(request.json,['name','description','image_url'])
    if(invalid != None):
        # if somevalues are missing it will show the message
        return make_response(json.dumps(invalid,default=str),400)
    # if every value is recieved then call the get display funtion to send data to the database
    results = get_display_results('call add_candy(?,?,?)',
    [request.json.get('name'),request.json.get('description'),request.json.get('image_url')])
    if(len(results) == 1):
        # if length of results is 1 then return the id if not then return the message
        return make_response(json.dumps(results[0][0],default=str),200) 
    elif(len(results) == 0):
        return make_response(json.dumps("No candy is added",default=str),500)

# delete an existing candy with the help of a id
# and display the results 
@app.delete('/api/candy')
def delete_candy():
    # will verify the data required for the endpoint
    invalid = verify_endpoints_info(request.json, ['candy_id'])
    if(invalid != None):
        # if missing something then will show a msg and not proceed further
        return make_response(json.dumps(invalid, default=str),400)
    results = get_display_results('call delete_candy(?)',[request.json.get('candy_id')])
    deleted_items = results[0][0]
    # will show the appropraite msg based on response
    # if something is not deleted then response is 0 then the msg will say no candy deleted
    # if response is 1 then the msg will display as item deleted
    # else if error msg 
    if(deleted_items == 0):
        return "No candy deleted, please enter the valid id for candy"
    elif(deleted_items == 1):
        return make_response(json.dumps('item deleted',default=str),200)
    else:
        return "There is an error in deleting candy"

# if production mode is true then bjoern server will run
# else the app.run
if(dbcreds.production_mode == True):
    print('Running in PRODUCTION MODE')
    import bjoern #type: ignore
    bjoern.run(app,'0.0.0.0',5100)
else:
    from flask_cors import CORS
    CORS(app)
    print('Running in TESTING MODE')
    app.run(debug=True)


