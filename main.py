"""
pixela_endpoint = "https://pixe.la/v1/users"
user_parameters = {
    "token": USERNAME, "username": TOKEN, "agreeTermsofService": "yes", "notMinor": "yes"
}
user_response = requests.post(url=pixela_endpoint, json=user_parameters)
print(user_response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_parameters = {
    "id": GRAPH_ID, "name": "Running Graph", "unit": "Km", "type": "float", "color": "sora",
}
headers = {
    "X-USER-TOKEN": TOKEN
}
"""

import requests
from datetime import datetime
from flask import Flask, render_template, request

app = Flask(__name__)

USERNAME = "matrixavenger"
TOKEN = "habittrackerstart"
GRAPH_ID = "graph1"
PIXELA_ENDPOINT = "https://pixe.la/v1/users"


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/add_pixel', methods=['POST'])
def add_pixel():
    date = request.form['date']
    quantity = request.form['quantity']

    # Convert date to datetime object
    date_obj = datetime.strptime(date, "%Y-%m-%d")

    # Make API request to add pixel
    pixel_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"
    pixel_parameters = {
        "date": date_obj.strftime("%Y%m%d"),
        "quantity": quantity,
    }
    headers = {
        "X-USER-TOKEN": TOKEN
    }
    pixel_response = requests.post(url=pixel_endpoint, json=pixel_parameters, headers=headers)

    if pixel_response.status_code == 200:
        return "Success!"
    else:
        return "Error adding pixel"


@app.route('/reset_activity', methods=['POST'])
def reset_activity():
    # Retrieve the date from the request data
    date = request.form['date']
    date_obj = datetime.strptime(date, "%Y-%m-%d")

    # Make API request to delete all pixels in graph
    reset_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{date_obj.strftime('%Y%m%d')}"
    headers = {"X-USER-TOKEN": TOKEN}
    reset_response = requests.delete(url=reset_endpoint, headers=headers)

    if reset_response.status_code == 200:
        return "Success!"
    else:
        return "Error resetting activity"


if __name__ == '__main__':
    app.run(debug=True)
