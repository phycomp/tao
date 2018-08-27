from django.urls import path, re_path
from .views import Profile, MePagination, ProfilePagination, ME, Login, Logout, EditProfile, passwordForgot, passwordReset, SignUp, Others, checkEmail#, checkUsername

urlpatterns = [
    path(r'me/', ME.as_view(), name='me'),
    path(r'me-pagination/', MePagination.as_view(), name='me-pagination'),
    path(r'profile-pagination/', ProfilePagination.as_view(), name='profile-pagination'),
    path(r'others/', Others.as_view(), name='others'),
    path(r'login/', Login.as_view(), name='login'),
    path(r'signup/', SignUp.as_view(), name='signup'),
    path(r'logout/', Logout.as_view(), name='logout'),
    path(r'password-reset/', passwordReset.as_view(), name='password-reset'),
    path(r'password-forgot/', passwordForgot.as_view(), name='password-forgot'),
    path(r'edit-profile/', EditProfile.as_view(), name='edit-profile'),
    #path(r'check-username/', checkUsername.as_view(), name='check-username'),
    path(r'check-email/', checkEmail.as_view(), name='check-email'),
    path(r'<int:oid>/', Profile.as_view(), name='profile'),
    #re_path(r'(?P<pid>\d+)/', Profile.as_view(), name='profile'),
    #path(r'check-password-reset/', checkPasswordReset.as_view(), name='check-password-reset'),
]
