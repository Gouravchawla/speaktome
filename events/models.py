from django.db import models


class Event(models.Model):
    name = models.CharField(max_length=100)
    event_date = models.DateTimeField()

    def __str__(self):
        return self.name


class Poll(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    pub_date = models.DateTimeField('Published Date')

    def __str__(self):
        return self.name


class Question(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=255)
    pub_date = models.DateTimeField('Published Date')

    def __str__(self):
        return self.question_text


class Option(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    option_text = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.option_text + ' - ' + str(self.votes)

