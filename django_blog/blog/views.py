from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import  login
from .forms import CustomUserCreationForm, ProfileForm
from django.contrib.auth.mixins import LoginRequiredMixin
# registration view
class RegisterView(View):
    def get(self, request):
        form = CustomUserCreationForm()
        return render(request, 'registration/register.html', {'form':form})
    
    def post(self,request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user) # log the user after registration
            return  redirect('profile') # redirect  to profile page 
        return  render(request, 'registration/register.html', {'form':form})

#profile view, only login user can view it
class ProfileView(LoginRequiredMixin, View):
    def get(self,request):
        user_form = UserChangeForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)

        return render(request,'registration/profile.html', {
            'user_form': user_form,
            'profile_form':profile_form,
        })
    
    def post(self,request):
        user_form = UserChangeForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile') # redirect to profie after update
        
        return render(request, 'registration/profile.html',{
            'user_form': user_form,
            'profile_form':profile_form,
        })