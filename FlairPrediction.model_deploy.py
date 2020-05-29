from flask import Flask, jsonify, request
from pickle import load
from urllib.request import Request, urlopen
import json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
	if (request.method == 'POST'):
		input_json = request.get_json()
		url = input_json['url']
		model = load(open('model.pkl', 'rb'))
		hdr = {'User-Agent': 'osx:r/relationships.single.result:v1.0 (by /u/goodwillhunter01)'}
		url = url + ".json"
		req = Request(url)
		req.add_header('User-Agent', 'osx:r/relationships.single.result:v1.0 (by /u/goodwillhunter01)')
		content = urlopen(req).read()
		data = json.loads(content)
		data_all = data[0]["data"]['children']
		X_input = [data_all[0]['data']['created_utc'], data_all[0]['data']['num_comments'], data_all[0]['data']['score'], data_all[0]['data']['total_awards_received'], data_all[0]['data']['upvote_ratio']]
		if (str(data_all[0]['data']['allow_live_comments'])=='True'):
		    X_input.append(1)
		else:
		    X_input.append(0)
		pred = model.predict([X_input])

		return jsonify(str({"pred" : str(pred[0])}))
	return jsonify({'pred':'Invalid input'})


if __name__ == '__main__':
	app.run(debug=True)



#curl -H "Content-Type: application/json" -X POST -d '{"url":"https://www.reddit.com/r/india/comments/gsm5rg/corona_donors/"}' http://127.0.0.1:5000/