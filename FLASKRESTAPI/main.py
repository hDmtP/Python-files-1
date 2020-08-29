from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/amstrong/<int:n>')
def amstrng(n):
    # n = int(input("Enter any int value of n: "))  


    count=0
    m=n
    while(m>0):
        count+=1
        m//=10            

    sum=0
    temp=n

    while(temp>0):
        
        digit=temp%10
        sum+=digit**count
        temp=temp//10
    if(n==sum):
        print(n, " is an Amstrong Number\n") 
        result={
            "Number":n,
            "Amstrong":True,
            "Server IP":"123.07.00.01"
        }  
    else:
        print(n," is NOT an Amstrong Number\n")
        result={
            "Number":n,
            "Amstrong":False,
            "Server IP":"123.07.00.01"
        }    
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)    