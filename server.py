import json
import sys

from flask import Flask, request, make_response
from flask_cors import CORS

from investment_calc.main import calculate

app = Flask(__name__)
CORS(app)


@app.route('/.well-known/acme-challenge/3i-hK-59J1Lrab785r7nl6alEtojUrec8UxAoNC-Xkc')
def letsencrypt_check():
    response = make_response('3i-hK-59J1Lrab785r7nl6alEtojUrec8UxAoNC-Xkc.tkC2gBMWBXsjPRY1FEsD0Eb7EOJJCZXGlCrt7QorF5c',
                             200)
    response.mimetype = "text/plain"
    return response


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
    app.run(port=5000, debug=True)
