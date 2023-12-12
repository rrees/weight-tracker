import wtforms


class WeightForm(wtforms.form.Form):
    weight = wtforms.fields.DecimalField(
        validators=[
            wtforms.validators.DataRequired(),
            wtforms.validators.NumberRange(75, 120),
        ]
    )
