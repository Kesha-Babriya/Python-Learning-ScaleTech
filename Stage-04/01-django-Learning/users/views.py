from django.contrib import messages  # For flash alert notifications
from django.shortcuts import redirect, render
from .forms import UserRegisterForm  # Import our customized registration form
from django.contrib.auth.decorators import  login_required  # The security guard decorator


def register(request):
  if request.method == 'POST':
    # User submitted data: populate form with submitted POST dictionary
    form = UserRegisterForm(request.POST)

    # Validate inputs against all built-in rules (unique username, valid email, matching passwords)
    if form.is_valid():
      # Hash password and insert the new user record into the auth_user table
      form.save()

      # Extract sanitized username for the feedback message
      username = form.cleaned_data.get('username')

      # Store a one-time flash message in session
      messages.success(
          request, f'Account created for {username}! You can now log in.'
      )

      # Redirect to prevent re-submission on refresh (Post/Redirect/Get pattern)
      return redirect('core-home')
  else:
    # User arrived via GET request: instantiate a fresh, blank form
    form = UserRegisterForm()

  # Render template: if invalid POST, it re-renders here with attached form.errors
  return render(request, 'users/register.html', {'form': form})


# The decorator checks if the user has an active session cookie.
# If logged in -> executes profile().
# If not logged in -> redirects to LOGIN_URL ('login').
@login_required
def profile(request):
  return render(request, 'users/profile.html')