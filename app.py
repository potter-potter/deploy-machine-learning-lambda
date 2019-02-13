from chalice import Chalice
import pickle
from io import BytesIO

import boto3
from botocore.exceptions import ClientError

S3 = boto3.client('s3', region_name='us-west-2')
BUCKET = 'deploy-machine-learning-lambda'

app = Chalice(app_name='deploy-machine-learning-lambda')
app.debug = True



s3 = boto3.resource('s3')
with BytesIO() as data:
    s3.Bucket("telegram-csv-storage").download_fileobj("model.pkl", data)
    data.seek(0)    # move back to the beginning after writing
    model = pickle.load(data)
# Loading the machine learning model
# model_url = S3.get_object(Bucket=BUCKET, Key='model.pkl')
print(model)
print(type(model))
# model = pickle.load(open(pickled_model,"rb"))


@app.route('/')
def index():
    return {'hello': 'friend'}


# The view function above will return {"hello": "world"}
# whenever you make an HTTP GET request to '/'.
#
# Here are a few more examples:
#
# @app.route('/hello/{name}')
# def hello_name(name):
#    # '/hello/james' -> {"hello": "james"}
#    return {'hello': name}
#
# @app.route('/users', methods=['POST'])
# def create_user():
#     # This is the JSON body the user sent in their POST request.
#     user_as_json = app.current_request.json_body
#     # We'll echo the json body back to the user in a 'user' key.
#     return {'user': user_as_json}
#
# See the README documentation for more examples.
#
