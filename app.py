from apihelpers import get_display_results, verify_endpoints_info
from flask import Flask, request, make_response
import json
import dbcreds

app = Flask(__name__)

# get all the candies from the database
@app.get('/api/candy')
def all_candies():
    results_json = get_display_results('call all_candies()',[])
    return results_json

# post a new candy into a database
@app.post('/api/candy')
def add_candy():
    invalid = verify_endpoints_info(request.json,['name','description','image_url'])
    if(invalid != None):
        return make_response(json.dumps(invalid,default=str),400)
    results_json = get_display_results('call add_candy(?,?,?)',
    [request.json.get('name'),request.json.get('description'),request.json.get('image_url')])
    return results_json

# delete an existing candy with the help of a id

@app.delete('/api/candy')
def delete_candy():
    invalid = verify_endpoints_info(request.json, ['candy_id'])
    if(invalid != None):
        return make_response(json.dumps(invalid, default=str),400)
    results_json = get_display_results('call delete_candy(?)',[request.json.get('candy_id')])
    return results_json[0]

if(dbcreds.production_mode == True):
    print('Running in PRODUCTION MODE')
    import bjoern #type: ignore
    bjoern.run(app,'0.0.0.0',5000)
else:
    from flask_cors import CORS
    CORS(app)
    print('Running in TESTING MODE')
    app.run(debug=True)


