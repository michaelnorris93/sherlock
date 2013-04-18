from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from auth.models import SherlockUser as SherlockUser_model
from SherlockGame.models import QuestionType as QuestionType_model
from SherlockGame.models import Answer as Answer_model

@login_required(login_url="/login/")
def PlayGame(request):
    num_photos = SherlockUser_model.objects.count() - SherlockUser_model.objects.filter(race=None).count()
    s_userID = random.(1, num_photos)
    photo_user = SherlockUser.objects.get(id=s_userID) #retrieve random SherlockUser 

    num_questions = QuestionType_ 

    return render(request, 'PlayGame.html', {'user': request.user, 'num': num_photos})
