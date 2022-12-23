from config import KEY
from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = KEY
MAXIMIZED_DEFAULTS = True # you can change this to true 
                            # if you want form to be filled for you in a probability maximization way

from views import entry_page


app.register_blueprint(entry_page)


if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')