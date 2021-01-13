from django.shortcuts import render
from registerapp.forms import ProfileInfoForm,UserForm
# Create your views here.
def index(request) :
    return render(request , 'registerapp/index.html')
def register(request):
    registerd = False
    if request.method == 'POST':
        profile_form = ProfileInfoForm(data = request.POST)
        user_form = UserForm(data = request.POST)
        if user_form.is_valid() and profile_form.is_valid() :
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user=user

            if 'profile_pic' in request.FILES :
                profile.profile_pic = request.FILES['profile_pic']
            #profile.save()
            registerd = True
        else:
            print(profile_form.errors ,user_form.errors )
    else :

        profile_form = ProfileInfoForm()
        user_form = UserForm()
    return render(request, 'registerapp/register.html' , {'registerd' :registerd , 'profile_form' :profile_form , 'user_form' :user_form})
