# mock up references https://docs.guidewire.com/cloud/cc/202306/apiref/generated/Claim%20API/claim-infos--claimInfoId---get/

from flask import Flask,Response, make_response
from flask import Flask,render_template,request,jsonify,redirect,url_for,session,abort,request, \
redirect

import json
from jsonschema import validate

from colorama import init
init()
from colorama import Fore, Back, Style

from schema_json import *
from config_data import *
import claim_activity



app = Flask(__name__)

@app.route("/claims_post/",methods=["POST","GET"])
def claims_post():
    print("Method",request.method)
    if request.method != "POST":
        return make_response(jsonify({"Error":"Method Not Allowed"}),405)
    try:
        claims_data=request.get_json(silent=True)
        print(claims_data)
        validate(instance=claims_data, schema=post_claim_schema)
        # add claimid in list, so can be refered in get call
        claims_data_request_list=claims_data['requests']
        for each_request in claims_data_request_list:
            for each_header in each_request['headers']:
                if each_header.get("name") == 'ClaimId':
                    #print(each_header.get("value"))
                    new_claim_id=each_header.get("value")
                    if int(each_header.get("value")) in claims_in_system:
                         print( f"{Fore.RED}Error: ClaimId already exist:{new_claim_id}")
                         return  make_response(jsonify({"Error":"Claim Id already exist"}),409)
                    claims_in_system.append(int(each_header.get("value")))
        print(F"Claims In System: {claims_in_system} New ClaimID:{new_claim_id}")
        #end of claimid 
        return make_response(jsonify(claims_data),200)
    except Exception as e:
        return  make_response(jsonify({"Error":"Invalid/No JSON"}),400)


@app.route("/claims/<string:claim_id>/")
def claim_withid(claim_id):
    #print(claim_id)

    if int(claim_id) in claims_in_system:
        cr=claiminfo_response.copy()
        cr["data"]['attributes']['claim']['assignedByUser']['refid']=claim_id
        cr["data"]['attributes']['claim']['assignedByUser']['id']=claim_id
        return  make_response(jsonify(claiminfo_response),200)
    else:
        print(f"{Fore.CYAN} Claim not found,claim ID: {claim_id}")
        return make_response(jsonify({"Error":"Claim Not Found"}),200)

@app.route("/claims/<string:claim_id>/activities",methods=['POST'])
def new_activity_on_claim(claim_id):
    try:
        claims_activities_data=request.get_json(silent=True)
        print("++++"*10)
        
        if claims_activities_data:
            print(f"Request Body: Contract Valid ")
            validate(instance=claims_activities_data, schema=claim_activity.request_schema)
            return make_response(jsonify(claim_activity.response_data),201)
        else:
             return make_response(jsonify({"Error":"Invalid/No JSON"}),400)

        print("++++"*10)
        
    except Exception as e:
        return  make_response(jsonify({"Error":"Invalid/No JSON"}),400)
    


@app.route("/claims/",methods=['GET'])
def return_all_claims():
    api_key=request.headers.get("APIKEY")
    print(F"Auth key:{api_key}")
    if api_key in api_keys_in_db:
        return make_response(jsonify(claims_in_system),200)
    else:
        return make_response(jsonify({"Error":"Invalid API Key"}),200)

@app.errorhandler(405)
def method_not_allowed(e):
    # note that we set the 404 status explicitly
    return make_response(jsonify({"Error":"Method Not Allowed"}),405)

if __name__ == '__main__':
    app.run(debug=True,port=4200)