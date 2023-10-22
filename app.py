from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=["POST", "GET"])
def index():
    if request.method == "GET":
        return "Hello..."
    elif request.method == "POST":
        payload = request.json
        user_response = (payload['queryResult']['queryText'])
        bot_response = (payload['queryResult']['fulfillmentText'])
        if user_response or bot_response != "":
            print("User:" + user_response)
            print("Bot:" + bot_response)
        return "Message Received."
    else:
        print(request.data)
        return "200"

if __name__ == "__main__":
    app.run(debug=True)
