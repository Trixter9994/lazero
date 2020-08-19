from flask import Flask, request
import threading
import pytesseract
import time
import copy

def scanner(mainfile,filerefresh):
    while True:
        if (filerefresh[0]):
            try:
                data=copy.copy(mainfile[0])
                print(type(data),data)
            except:
                print("MISSED")
        else:
            time.sleep(1)
mainfile=[None]
filerefresh=[False]
app = Flask(__name__)
@app.route('/sample', methods=['POST'])
# use a separate thread to process this saving thing.
def result():
    # get all things.
    #print(request.data)
    files=request.files
    form=request.form
    pr=[files[x] for x in list(files)]
    pr0=[form[x] for x in list(form)]
    if len(pr0)==1:
        if pr0[0]=="screenshot":
            mainfile[0]=pr[0].read()
            filerefresh[0]=True
            #print(pr[0])
    #print(request.form['foo']) # should display 'bar'
    return 'Received !' # response to your request.

p=threading.Thread(target=scanner,args=(mainfile,filerefresh))
p.setDaemon(True)
p.start()
app.run(port=4999)
