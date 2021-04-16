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
