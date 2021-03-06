from flask import Flask,jsonify
app=Flask(__name__)

@app.route('/')
def hello_world():
    return "Hi World"
#comment
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

@app.route('/reverse/<int:n>')
def reverse(n):
    s=0
    t=n
    while n!=0:
        a=n%10
        s=(s*10)+a
        n=n//10
    ss={"Number":t,"reverse":s}
    return jsonify(ss)

@app.route('/palindrome/<int:n>')
def palindrome(n):
    s=0
    t=n
    while n!=0:
        a=n%10
        s=(s*10)+a
        n=n//10
    if t==s:

        ss={"Number":t,"reverse":s,"Palindrome":True}
    else:
        
        ss={"Number":t,"reverse":s,"Palindrome":False}
    
    return jsonify(ss)


@app.route('/hello/<string:s>')
def hello(s):
    res={
        "Guest name":s
    }
    return jsonify(res)

@app.route('/add/<int:a>/<int:b>')
def add(a,b):
    c=a+b
    res={
        "First number":a , "Second number":b , "Sum":c
    }
    return jsonify(res)

@app.route('/sub/<int:a>/<int:b>')
def diff(a,b):
    c=a-b
    res={
        "First number":a , "Second number":b , "Subtration":c
    }
    return jsonify(res)

@app.route('/prime/<int:n>')
def prime(n):
    f=False
    if(n>1):
        for i in range(2,n):
            if(n%i)==0:
                f=True
                break
        if(f):
            res={
                "Number":n,"Prime":False
                }
        else:
            res={
                "Number":n,"Prime":True
                }
    return jsonify(res)

if __name__ == "__main__":
    app.run(debug=True)
    