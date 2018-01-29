from django.conf.urls import url, include
from system_user import views

urlpatterns = [

    # Get the list of all the sicknesses
    url(r'^sicknesses/$',
        views.GetAllSickness.as_view(), name="sickness"),

    # Get the list of all the physical activities
    url(r'^activities/$',
        views.GetAllPhysicalActivites.as_view(), name="activities"),
    
    # Get the list of all the users
    url(r'^user/(?P<userid>\d+)$',
        views.GetUserInformation.as_view(), name="users"),
    
    # Update an existing user
    url(r'^update/(?P<id>\d+)$',
        views.UpdateUser.as_view(), name="update_user"),
    
    # Update an existing user part 2
    url(r'^update2/(?P<id>\d+)$',
        views.UpdateUser2.as_view(), name="update_user2"),
    
    # Create a new user
    url(r'^create/$',
        views.CreateUser.as_view(), name="create_user"),
    
    # Create a new user part 2
    url(r'^create2/$',
        views.CreateUser2.as_view(), name="create_user2"),
    
    # Log in an existing user
    url(r'^login/$',
        views.Login.as_view(), name="login"),
]