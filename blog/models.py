from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Topic(models.Model):
    """A Topic the user is learning about"""
    post_title = models.CharField(max_length=200)
    post_text = models.TextField()
    post_user = models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Return a string representation of the model"""

        if len(self.post_title) > 50:
            return f"{self.date_added}: {self.text_field[:50]}...   "
        
        else:
            return f"{self.date_added.date()}: {self.post_title}"
        
class Answer(models.Model):
    """An Answer for a specific Topic"""
    # Thir class must to be related to the Topic class by Foreing Keys

    topic = models.ForeignKey(to=Topic, on_delete=models.CASCADE)
    answer_text = models.TextField()
    answer_user = models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    # Defining name for plurals
    class Meta:
        verbose_name_plural = "answers"
    
    def __str__(self):
        """Return a representation of the answer"""
        if len(self.answer_text) > 50:
            return f"{self.date_added.date()}: {self.answer_text[:50]}..."
        else:
            return f"{self.date_added.date()}: {self.answer_text}"