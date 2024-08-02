from django import forms

# Importing model to create FORMS

from .models import Topic, Answer

class TopicForm(forms.ModelForm):
    """ Create a Form for a Topic"""
    class Meta:
        # The form it is generated based on the TOPIC model
        model = Topic
        # We create a FIELD
        fields = ["post_title", "post_text"]
        # The we remove the label from this fields
        labels = {"post_title":"Title:",
                  "post_text":"Text: "}
        
class AnswerForm(forms.ModelForm):
    """Create a form for a adding and Answer to a Topic"""
    class Meta:
        model = Answer
        fields = ["answer_text"]
        labels = {"answer_text":""}
        widgets = {"answer_text":forms.Textarea()}
    