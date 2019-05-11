from flask import jsonify

def custom_response(data, status_code):
    """
    Custom Response Function
    """
    reponse = jsonify(data)
    reponse.status_code = status_code
    return reponse