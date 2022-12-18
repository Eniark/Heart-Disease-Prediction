from model import Model
from config import KEY
from flask import Flask, render_template, request, flash
from forms import UserForm

app = Flask(__name__)
app.config['SECRET_KEY'] = KEY

@app.route('/', methods=('GET', 'POST'))
def index():
    form = UserForm(request.form or None)
    context = {
        'form' : form
    }

    if request.method == 'GET':
        return render_template('index.html', context=context)

    elif request.method == 'POST':
        print('='*10, 'POST REQUEST', '='*10)
        if form.validate():
            heart_model = Model('pipeline.sav')
            preprocessed_data = heart_model.preprocess(request.form)
            prediction_probas = heart_model.model.predict_proba([preprocessed_data])[:, 1]
            prediction_adjusted = heart_model.adjust_predictions(prediction_probas)
        else:
            flash('Blela')
        print('='*10, 'END OF POST', '='*10)
        return render_template('prediction.html', prediction=prediction_adjusted)


# if __name__=='__main__':
#     app.run()