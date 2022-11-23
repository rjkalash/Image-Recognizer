from flask import Flask, request, jsonify
import util

app = Flask(__name__)


@app.route('/classify_image', methods=['GET', 'POST'])
def classify_image():
    id = request.form['id']
    response = jsonify(util.classify_image(id))
    
    return response


if __name__ == '__main__':
    print("Starting python flask server for image classification ")
    util.load_saved_artifacts()
    app.run(port=5000)
