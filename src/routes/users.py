""" This is an example to show how Blueprints work """

from flask import Blueprint, request

# Initialize a blueprint
users = Blueprint('users', __name__)

# Route decorator for the path, which in this case would be /users, and the methods allowed (GET)
@users.route('/users', methods=['GET'])
def users_route():
    ''' This is just a sample of how you return data, if you visit localhost:5000 in your browser,
        you will see 'Users Route' printed in the default font for your browser, and the status is
        200 '''
    return 'Users Route', 200

@users.route('/users/<userid>', methods=['GET'])
def single_user_route(userid):
    ''' This is an example of how you use route parameters in flask. Wrap the variable name in angle
        brackets, and then use the SAME NAME for the function definition. We will return whatever is
        in the path variable in a dict to demonstate this. '''
    user_dict = {'queriedUser': userid}
    return user_dict, 200