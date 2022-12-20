from flask import render_template, request, Blueprint, abort
from forms import UserForm
from model import Model
from jinja2 import TemplateNotFound

entry_page = Blueprint('entry_page', __name__)

@entry_page.route('/', methods=('GET', 'POST'))
def index():
    
    """Main page"""
    
    form = UserForm(request.form or None)
    context = {
        'form' : form
    }
    try:
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
    except TemplateNotFound:
        abort(404)
