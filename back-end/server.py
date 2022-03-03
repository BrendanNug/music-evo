from flask import Flask, request
from flask_restful import Api, Resource
from flask_cors import CORS, cross_origin
from main import first, final; 


app = Flask(__name__)
api = Api(app)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'



# Static file names
FIRST_FILES= {"file1": "1.mid", "file2": "2.mid", "file3": "3.mid", "file4": "4.mid", "file5": "5.mid", "file6": "6.mid"}
SECOND_FILES = {"file7": "7.mid", "file8": "8.mid"}
FINAL_FILE = {"file9": "9.mid"}
POPULATION = []


class FirstRound(Resource):
    def post(self):
        # print(request.form.to_dict()["choice1"])
        # print(request.form.to_dict()["choice2"])
        # print(request.form.getlist('choice2[]'))
        POPULATION.extend(first(request.form.to_dict()["choice1"],request.form.to_dict()["choice2"]))

        print(POPULATION)
        return FIRST_FILES

class SecondRound(Resource):
    def post(self):
        # print(POPULATION)
        # print(request.form.to_dict()["choice1"])
        final(POPULATION, request.form.to_dict()["choice1"])
        return SECOND_FILES

api.add_resource(FirstRound, "/1")
api.add_resource(SecondRound, "/2")

if __name__ == "__main__":
    app.run(debug=True)