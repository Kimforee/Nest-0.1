from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('login/',views.loginPage,name='login'),
    path('nest/<str:pk>/',views.nest,name='nest'),
    path('logout/',views.logoutUser,name='logout'),
    path('register/',views.registerPage,name='register'),
    path('create-nest/',views.createNest,name='create-nest'),
    path('flash_message/',views.flashMessage,name='flash-message'),
    path('profile/<str:pk>/',views.userProfile,name='user-profile'),
    path('update-user/',views.updateUser,name='update-user'),
    path('update-nest/<str:pk>/',views.updateNest,name='update-nest'),
    path('delete-nest/<str:pk>/',views.deleteNest,name='delete-nest'),
    path('leave-nest/<str:pk>/',views.leave_Nest, name='leave-nest'),
    path('all-requests/<str:pk>/',views.allRequests,name='all-requests'),
    path('delete-message/<str:pk>/',views.deleteMessage,name='delete-message'),
    path('accept-join-request/<str:pk>/',views.acccept_join_request,name='accept-join-request'),
    path('reject-join-request/<str:pk>/',views.reject_join_request,name='reject-join-request'),
]