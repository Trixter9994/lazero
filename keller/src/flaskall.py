from flask import Flask, request
import random
from curl_baidu import get_url
#from flask import Flask, render_template
app = Flask(__name__)
"""
@app.route('/', defaults={'path': ''},methods=['POST','GET'])
def catch_all(path):
    print("path",path)
    return render_template('index.html')
"""
rng=random.SystemRandom()
lst=["how to kill your father","how to kill your mother"]
@app.route('/', defaults={'path': ''},methods=['POST','GET'])
@app.route('/<path:path>',methods=['POST','GET'])
def catch_all(path):
    print("path",path)
    if path=="keller":
#        pass
        print(request.data)
    elif path=="url":
        return get_url(rng.choice(lst))
# should you be dynamic?
# create a heart-beat package. choose from avaliable candidates.
# use redis.
# so captcha over there.
        # cannot get data here.
    return "PATH "+path
    #return render_template('index.html')
    # are you sure it is utf-8? not concerned.

# do not use browser. use code like js or curl to test connection.
"""
@app.route('/')
def homepage():
    return "Hello world!"
"""
app.run(port=7777)
