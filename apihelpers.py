
# import single function from dbhelpers to connect
# execute and close the connection
from dbhelpers import conn_exe_close
# import request, make_response,jsonify from flask
from flask import make_response
import json

# single function to handle database interactions
# and based on results will send errors
def get_display_results(statement,args_list):
    results = conn_exe_close(statement,args_list)
    if(type(results) == list):
        if(len(results) == 0):
            return 'No Results matched your input'
        return results
    elif(type(results) == str):
        if(results.startswith('Duplicate entry')):
            return 'Duplicate data already exists, please change values and try again'
        return make_response(json.dumps(results, default=str), 400)
    else:
        return make_response(json.dumps(results, default=str) , 500)

# will verifiy end points arguments for presence
# if necessary arguments not sent then remind the user to send
def verify_endpoints_info(sent_data,required_args):
    for data in required_args:
        if(sent_data.get(data) == None):
            return f'The {data} argument is required'
