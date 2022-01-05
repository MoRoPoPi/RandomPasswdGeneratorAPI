from flask import Flask
from flask_restful import Resource, Api
from random import randint, choice

app = Flask(__name__)
api = Api(app)

class random(Resource):
    def get(self, length):
        l = []
        letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        for i in range(int(length/2)):
            l.append(choice(letters)+str(randint(0, 9)))
        return{'passwd':(''.join(l))}


api.add_resource(random, '/rdmpasswd/length=<int:length>')

    
if __name__ == '__main__':
    app.run(debug=True, host="localhost", port=80)


# this is a simple example of how to create a random Password Generator 
# MoRoPoPi MIT | 2020
