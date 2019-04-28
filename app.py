import os
from flask import Flask, jsonify, request, render_template
app = Flask(__name__)
import utils
import time
# FILE = os.environ.get("FILE", "test_data_sample.csv")

# with open(FILE) as f:
#     reader = csv.reader(f)
#     terms = [row[0] for row in reader]


@app.route('/process_search')
def gen_search_json():
    start_time = time.time()
    query = request.args.get("q", '')
    #print("query  " + query)
    query = utils.process_term(query)
    #print("After Processing query  " + query)
    
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
