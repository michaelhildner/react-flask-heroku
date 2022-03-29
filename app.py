from flask import Flask, Request, request, send_from_directory
#from flask_cors import CORS, cross_origin

#static folder used to route to my-app
app = Flask(__name__, static_folder='my-app/build', static_url_path='')
#CORS(app)
@app.route('/api', methods=['GET'])
#@cross_origin()
def index():
    args = request.args.to_dict(flat=False)
    firstName = ''
    message = 'User Not Found'
    if 'name' in args:
        firstName = request.args.get('name')
    if firstName.lower() == 'michael' :
        message = 'hildner'
    elif firstName.lower() == 'ta':
        message = 'please give me a 100'
    else:
        message = 'User Not Found'

    return {
        "lastname" : message
    }

@app.route('/')
#@cross_origin()
def serve():
    return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    app.run()
