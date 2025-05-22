from flask import Flask

app=Flask(__name__)

@app.route('/')
def Startup():
    return("Hello world")


if __name__ == "__main__":

    app.run(debug=True,port=3005)    
