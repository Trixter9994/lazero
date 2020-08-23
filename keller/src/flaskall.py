from flask import Flask, request
#from flask import Flask, render_template
app = Flask(__name__)
"""
@app.route('/', defaults={'path': ''},methods=['POST','GET'])
def catch_all(path):
    print("path",path)
    return render_template('index.html')
"""

@app.route('/', defaults={'path': ''},methods=['POST','GET'])
@app.route('/<path:path>',methods=['POST','GET'])
def catch_all(path):
    print("path",path)
    if path=="keller":
#        pass
        print(request.data)
# should you be dynamic?
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
