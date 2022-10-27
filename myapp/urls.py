<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> f354554 (merge conflict resolved)
from . import views
from django.urls import path,include

urlpatterns = [
    path('', views.user_profile,name='profile'),
    path('login', views.user_login,name='login'),
    path('signup', views.user_signup,name='signup'),
    path('logout', views.user_logout,name='logout'),

    #for forgot password
    # path('forgot_password', views.forgot_password,name='forgot_password'),
    # path('change_password/<token>', views.change_password,name='change_password'),
    
<<<<<<< HEAD
=======
=======
from . import views
from django.urls import path,include

urlpatterns = [
    path('', views.user_profile,name='profile'),
    path('login', views.user_login,name='login'),
    path('signup', views.user_signup,name='signup'),
    path('logout', views.user_logout,name='logout'),

    #for forgot password
    # path('forgot_password', views.forgot_password,name='forgot_password'),
    # path('change_password/<token>', views.change_password,name='change_password'),
    
>>>>>>> eaeb8de009e9ad4518da51a5278af6ac47aea828
>>>>>>> f354554 (merge conflict resolved)
]