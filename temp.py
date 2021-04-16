@app.route('/palindrome/<int:n>')
def palindrome(n):
    s=0
    t=n
    while n!=0:
        a=n%10
        s=(s*10)+a
        n=n//10
    if t==s:

        ss={"Number":t,"reverse":s,"It is a palindrome"}
    else:
        
        ss={"Number":t,"reverse":s,"It is not a palindrome"}
    
    return jsonify(ss)
