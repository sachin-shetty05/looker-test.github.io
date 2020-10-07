from flask import Flask 
from flask import redirect, request
import looker

app = Flask(__name__) 
 
@app.route('/looker-redirect/<id>', methods = ["GET"])  
def looker_redirect(id=64):
    print(dict(request.headers))
    return redirect(looker.generate_url(id))
 
if __name__ == '__main__': 
    app.run("0.0.0.0") 