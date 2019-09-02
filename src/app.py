import os
from flask import Flask, jsonify, request, render_template
app = Flask(__name__)
import utils
import time


@app.route('/process_search')
def gen_search_json():
    start_time = time.time()
    query = request.args.get("q", '')
    query = utils.process_term(query)
    results = utils.get_results(query.strip())
    resp = jsonify(results=results[:10])  # top 10 results
    resp.headers['Access-Control-Allow-Origin'] = '*'
    end_time = time.time()
    #print("Response time : " + str(end_time - start_time))
    return resp


@app.route('/home', methods=['GET'])
def render_html():
    return render_template('index.html')

if __name__== '__main__':
    app.run(debug=True)
