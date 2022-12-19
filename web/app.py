from model import Model
from config import KEY
from flask import Flask, render_template, request
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
        return render_template('form.html', context=context)
    elif request.method == 'POST':
        if form.validate():
            heart_model = Model('pipeline.sav')
            preprocessed_data = heart_model.preprocess(request.form)
            prediction_probas = round(heart_model.model.predict_proba([preprocessed_data])[:, 1][0], 3)
            prediction_adjusted = heart_model.adjust_predictions(prediction_probas)
        return render_template('prediction.html', prediction=prediction_adjusted, 
                                                  prediction_probability=prediction_probas,
                                                  THRESHOLD=Model.THRESHOLD)


if __name__=='__main__':
    app.run(debug=False, host='0.0.0.0')