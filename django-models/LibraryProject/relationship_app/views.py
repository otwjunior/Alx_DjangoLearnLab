from django.contrib.auth import login
from django.shortcuts import render, get_object_or_404, redirect
from .models import Library
from .models import Book, UserProfile
from django.contrib.auth.views import  LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.detail import DetailView 
from django.views import View
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator


#class based view
def list_books(request):
    books = Book.objects.all()
    return render (request, 'relationship_app/list_books.html',{'books': books})


class LibraryDetailView(DetailView):
    model = Library
    template_name= "relationship_app/library_detail.html"
    context_object_name = 'library'

    # tell Django to use name field for the library
    slug_field = 'name' # field in model
    slug_url_kwarg = 'name' # keyword argument from URL

class CustomLoginView(LoginView):
    template_name = 'relationship_app/login.html'

class CustomLogoutView(LogoutView):
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
    

class RegisterView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'relationship_app/register.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login') # after registration go to login page
        return render(request, 'relationship_app/register.html', {'form': form})

@login_required
def home_view(request):
    return render (request, 'relationship_app/home.html')

register = RegisterView.as_view()

#Helper functions
def is_admin(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'
def is_librarian(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and  user.userprofile.role == 'Librarian'
def is_member(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Member'


# defining users views
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')