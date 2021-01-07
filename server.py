import json
import sys

from flask import Flask, request
from flask_cors import CORS

from investment_calc.main import calculate

app = Flask(__name__)
CORS(app)


@app.route('/calculate', methods=['GET'])
def calculate_api():
    try:
        deposit = float(request.args.get('deposit'))

        money = []
        perc = []

        for item in json.loads(request.args.get('values')).values():
            money.append(float(item[0]))
        for item in json.loads(request.args.get('percentages')).values():
            perc.append(float(item[0]))

        return {'division_perc': calculate(perc, deposit, money)}
    except:  # catch *all* exceptions
        e = sys.exc_info()[0]
        return "<p>Error \n %s</p>" % e


if __name__ == '__main__':
    app.run(port=5000, debug=False)
