from django.db import models
from quizz.models import Quizz
# Create your models here.


class Questions(models.Model):
    terme = models.CharField(max_length=200)
    quizz = models.ForeignKey(Quizz, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.terme)
    def get_answer(self):
        return self.answer_set.all()
    
class Answer(models.Model):
    terme = models.CharField(max_length=200)
    correct = models.BooleanField(default=False)
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Définition : {self.question.terme}, answer {self.terme}, correct {self.correct}"