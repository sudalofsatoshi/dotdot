from flask import Flask, jsonify, request, abort
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, Length
from wtforms import Form, IntegerField, StringField, FieldList, validators
from wtforms.validators import DataRequired, AnyOf
from constants import *

class Input(Form):

    id = IntegerField('Id', validators=[DataRequired(), validators.NumberRange(min=0, max=999999)])
    bpm = IntegerField('Bpm', validators=[DataRequired(), validators.NumberRange(min=30, max=200)])
    audio_key = StringField('Audio Key', validators=[DataRequired(), AnyOf(KEY_MAP.keys())])
    time_signature = StringField('Time Signature', validators=[DataRequired(), AnyOf(TIME_SIG_MAP.keys())])
    pitch_range = StringField('Pitch Range', validators=[DataRequired(), AnyOf(PITCH_RANGE_MAP.keys())])
    num_measures = IntegerField('Num Measures', validators=[DataRequired(), AnyOf(NUM_MEASURES)])
    inst = StringField('Inst', validators=[DataRequired(), AnyOf(INST_MAP.keys())])
    genre = StringField('Genre', validators=[DataRequired(), AnyOf(GENRE_MAP.keys())])
    min_velocity = IntegerField('Min VeloCity', validators=[DataRequired(), validators.NumberRange(min=2, max=127)])
    max_velocity = IntegerField('Max Velocity', validators=[DataRequired(), validators.NumberRange(min=2, max=127)]) # TODO: add constraint (min <= max)
    track_role = StringField('Track Role', validators=[DataRequired(), AnyOf(TRACK_ROLE_MAP.keys())])
    rhythm = StringField('Rhythm', validators=[DataRequired(), AnyOf(RHYTHM_MAP.keys())])
    chord_progression = FieldList(StringField('Chord Progression')) # TODO: add constraints
    num_generate = IntegerField('Num Generate', validators=[DataRequired()])
    s3_prefix= StringField('S3 Prefix', validators=[DataRequired()])

app = Flask(__name__)
@app.route('/generate', methods=['POST'])
def generate():
    user_input = request.get_json()
    checker = Input(data=user_input)
    if checker.validate():
        print ("valid data")
        from pprint import pprint
        pprint (user_input)
        return jsonify({'message': user_input})

    abort(400, checker.errors)

if __name__ == '__main__':
    app.run(port=8000)