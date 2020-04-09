from django.db import models

from apis.serializers import User


class Question(models.Model):
    ANSWER = (
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
    )

    question = models.TextField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    choice_a = models.CharField(max_length=50)
    choice_b = models.CharField(max_length=50)
    choice_c = models.CharField(max_length=50)
    choice_d = models.CharField(max_length=50)
    answer = models.CharField(max_length=1, choices=ANSWER)
    credit = models.IntegerField()

    def __str__(self):
        return self.question[:40]


class Quiz(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    questions = models.ManyToManyField(Question)
    created = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Quizzes'

    @property
    def max_credit(self):
        total = 0
        for que in self.questions.all():
            total += que.credit
        return total


class Attempted(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    got = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = 'Attempted Quizzes'