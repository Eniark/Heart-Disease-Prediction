from flask_wtf import FlaskForm
from wtforms import (SubmitField, 
                    DecimalField, 
                    IntegerField,
                    RadioField,
                    SelectField)
from wtforms.validators import InputRequired, NumberRange
from enums import NumOfVesselsEnum, ThalEnum
from config import DEBUG_STATUS

class UserForm(FlaskForm):
    Age = IntegerField('Age', 
                        validators=[InputRequired(), NumberRange(min=1, max=100)],
                        render_kw={"placeholder": "Age..."},
                        default=45 if DEBUG_STATUS else None)
                        
    cholesterol = DecimalField('Cholesterol level', 
                                places=1, validators=[InputRequired(), NumberRange(min=100, max=300)], 
                                render_kw={"placeholder": "Cholesterol level..."},
                                default=220 if DEBUG_STATUS else None) # add step to decimalfields

    max_heart_rate = IntegerField('Maximum heart rate', 
                                    validators=[InputRequired(), NumberRange(min=70, max=200)], 
                                    render_kw={"placeholder": "Max heart rate..."},
                                    default=160 if DEBUG_STATUS else None)

    blood_pressure = DecimalField('Rest time blood pressure', 
                                    places=1,
                                    validators=[InputRequired(), NumberRange(min=80, max=220)],
                                    render_kw={"placeholder": "Blood pressure at rest time..."},
                                    default=130 if DEBUG_STATUS else None)
    st_depression = IntegerField('ST Depression test results', 
                                    validators=[InputRequired(), NumberRange(min=0, max=7)], 
                                    render_kw={"placeholder": "ST Depression..."},
                                    default=0 if DEBUG_STATUS else None)

    chest_pain_type = RadioField('Pain Type',
                       choices=['Typical Angina', 
                                'Atypical Angina',
                                'Non-anginal pain',
                                'Asymptomatic'],
                       validators=[InputRequired()]) 
    number_of_vessels = SelectField('Number of major Vessels',
                                    choices=[(0, NumOfVesselsEnum.no_vessels.value), 
                                            (1,NumOfVesselsEnum.one.value), 
                                            (2,NumOfVesselsEnum.two.value), 
                                            (3,NumOfVesselsEnum.three.value)], 
                                    # validators=[NumberRange(min=1, max=4)],
                                    render_kw={"placeholder": "Number of vessels..."})
    
    thal = SelectField('Thal', 
                        choices=((0,ThalEnum.none.value), 
                                (1,ThalEnum.one.value), 
                                (2,ThalEnum.two.value), 
                                (3,ThalEnum.three.value)),
                        validators=[InputRequired()], # NumberRange(min=1, max=3) 
                        render_kw={"placeholder": "Thal.."})


    submit = SubmitField(label='Submit')
    