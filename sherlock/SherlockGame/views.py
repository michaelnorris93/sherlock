from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from auth.models import SherlockUser as SherlockUser_model
from SherlockGame.models import QuestionType as QuestionType_model
from SherlockGame.models import Answer as Answer_model

import random

@login_required(login_url="/login/")
def PlayGame(request):
    if request.POST:
        if(request.POST.get('skipped') == 'True'):
            #what to do if user skips question
            #need to separately handle the case where the user skips before/after answering
            #save the previous question appropriately and load a new one
        else:
            #what to do if user submits his answer
    num_photos = SherlockUser_model.objects.count() - SherlockUser_model.objects.filter(race=None).count()
    s_userID = random.randint(1, num_photos)
    photo_user = SherlockUser_model.objects.get(id=s_userID) #retrieve random SherlockUser 

    num_questions = QuestionType_model.objects.filter(active=True).count() 
    questionID = random.randint(1, num_questions)
    questiontype = QuestionType_model.objects.get(id=questionID) #retrieve random question

    return render(request, 'PlayGame.html', {'user': request.user, 'photo_user': photo_user, 'question': questiontype})
