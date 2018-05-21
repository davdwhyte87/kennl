from flask import Flask


#app setup
app=Flask(__name__)

@app.route('/')
def hello():
    return "Hello mann"

#app run
if __name__=='__main__':
    app.run()
