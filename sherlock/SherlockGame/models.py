from django.db import models
from auth.models import SherlockUser

#model representing the possible questions a user can receive
class QuestionType(models.Model):
    active = models.BooleanField() #whether or not the question is currently active
    info_type = models.CharField(max_length=1024) #what info the question is asking for. Race, Age, etc
    text = models.CharField(max_length=1024) #Text that the question will display
    submit_format = models.CharField(max_length=1024) #what kind of submittion. radio? text input? number? etc

#model representing a user's answer
class Answer(models.Model):
    question_type = models.ForeignKey(QuestionType) #question type
    time_started = models.DateField() #time the user started
    time_answered = models.DateField() #time the user answered
    user_answering = models.ForeignKey(SherlockUser, related_name='user_answering') #user answering the question
    user_photo = models.ForeignKey(SherlockUser, related_name='user_photo') #user in the photo
    answer_passed = models.BooleanField() #whether or not the user skipped
    answer_raw = models.CharField(max_length=1024) #user's submitted answer
    answer_correct = models.CharField(max_length=1024) #correct answer retrieved from the user_photo's profile 
    correct = models.BooleanField() #whether or not the answer is correct. redundant informatino but it might save some computation
