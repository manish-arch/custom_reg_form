from .models import ExtraInfo
from django.forms import ModelForm

class ExtraInfoForm(ModelForm):
    """
    The fields on this form are derived from the ExtraInfo model in models.py.
    """
    def __init__(self, *args, **kwargs):
        super(ExtraInfoForm, self).__init__(*args, **kwargs)
        self.fields['TMC_NO'].error_messages = {
            "invalid": u"Must have Integer Value",
        }

    class Meta(object):
        model = ExtraInfo
        fields = ('TMC_NO')
