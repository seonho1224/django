from django.db import models

# Create your models here.
class Question(models.Model):
    subject = models.CharField(max_length=201)
    content = models.TextField()
    create_date = models.DateTimeField()


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        return self.subject
    