from flask import Flask


#app setup
app=Flask(__name__,instance_relative_config=True)

@app.route('/')
def hello():
    return "Hello mann"

#app run
if __name__=='__main__':
    app.run()
