
from dbhelpers import conn_exe_close
from apihelpers import get_display_results, verify_endpoints_info
from flask import Flask, request, make_response
import json
import dbcreds

app = Flask(__name__)

if(dbcreds.production_mode == True):
    print('Running in PRODUCTION MODE')
    app.run(debug=True)
else:
    from flask_cors import CORS
    CORS(app)
    print('Running in TESTING MODE')
    app.run(debug=True)


