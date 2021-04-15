from flask import Flask,jsonify
app=Flask(__name__)

@app.route('/')
def hello_world():
    return "Hi World"

@app.route('/armstrong/<int:n>')
def armstrong(n):
    s=str(n)
    l=len(s)
    c=0
    for i in s:
        i=int(i)
        c+=(i**l)
    if(n==c):
        res={
            "Number":n,"Armstrong":True
        }
    else:
        res={
            "Number":n,"Armstrong":False
        }
    return jsonify(res)

@app.route('/hello/<string:s>')
def hello(s):
    res={
        "Guest name":s
    }
    return jsonify(res)

if __name__ == "__main__":
    app.run(debug=True)
    