from flask import jsonify

def custom_response(data,status_code):
    """
    Custom Response Function
    """
    return jsonify(data), status_code

def custom_response(data,api_token, status_code):
    """
    Custom Response Function
    """
    return jsonify(data=data,api_token=api_token), status_code