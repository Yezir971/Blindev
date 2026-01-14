from django.db import models

# Create your models here.
TOPIC_CHOICE = (
    ("JARGON MARKET", "JARGON MARKET"),
    ("EDITEURS / SOFTS / OUTILS", "EDITEURS / SOFTS / OUTILS"),
    ("LANGAGES / FRAMEWORKS / BIBLIOTHEQUES", "LANGAGES / FRAMEWORKS / BIBLIOTHEQUES"),
    ("BUISNESS MODEL", "BUISNESS MODEL"),
    ("METRICS", "METRICS")
)
class Quizz(models.Model):
    title = models.CharField(max_length=200)
    topic = models.CharField(choices=TOPIC_CHOICE)
    number_of_questions = models.IntegerField()
    time = models.IntegerField(help_text="Temps du quizz en minute")
    require_score_to_pass = models.IntegerField(help_text="nombre de points minimum")

    def __str__(self):
        return f"{self.title}-{self.topic}"
    def get_questions(self):
        return self.question_set.all()