import json
import sys

from flask import Flask, request, make_response, redirect
from flask_cors import CORS

from investment_calc.main import calculate

app = Flask(__name__)
CORS(app)


@app.route('/.well-known/acme-challenge/6xH0cnqmE2q23U0RtZ-34vgBgkGKbXjCAt79YndGABM')
def letsencrypt_check():
    response = make_response('6xH0cnqmE2q23U0RtZ-34vgBgkGKbXjCAt79YndGABM.fvaTOuVuPG89tKY1VZTQxHmGqO5Qo4g8KkqQ2orWs5Y',
                             200)
    response.mimetype = "text/plain"
    return response


@app.before_request
def before_request():
    if request.url.startswith('http://'):
        return redirect(request.url.replace('http://', 'https://'), code=301)


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
