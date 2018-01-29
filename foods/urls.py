from django.conf.urls import url, include
from foods import views

urlpatterns = [

    # Get the list of all the user's food history
    url(r'^history/(?P<pk>\d+)$',
         views.FoodHistory.as_view(), name="food_history"),
    
    # Recommends a food for the user
    url(r'^recommend/(?P<id>\d+)$',
         views.SuggestFood.as_view(), name="recommender"),
    
    # Search for a food in the database
    url(r'^search/(?P<search>[\w|\W]+)$',
         views.FoodSearch.as_view(), name="search_food"),

    # Get a food in the database
    url(r'^get/(?P<pk>\d+)$',
         views.GetFood.as_view(), name="get_food"),

    # Get a food in the database
    url(r'^all/$',
         views.AllFood.as_view(), name="all_food"),
    
    # Get the list of all the user's favorite foods
    url(r'^favorite/(?P<pk>\d+)$',
         views.GetFavoriteFood.as_view(), name="favorite_food"),

    # Update user's Food History
    url(r'^history/update/(?P<pk>\d+)$',
         views.UpdateFoodHistory.as_view(), name="update_history"),

    # Search user's Food History
    url(r'^history/search/(?P<pk>\d+)/(?P<date>[\w|\W]+)$',
         views.SearchFoodHistory.as_view(), name="search_history"),

    # New user's Food History
    url(r'^history/create/$',
         views.NewFoodHistory.as_view(), name="new_history"),
]