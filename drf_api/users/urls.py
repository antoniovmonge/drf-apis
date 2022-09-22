from django.urls import path

from drf_api.users.views import user_detail_view, user_redirect_view, user_update_view

# from drf_api.users.api.views import UserList, UserDetail


app_name = "users"
urlpatterns = [
    # path("v1/users/", UserList.as_view()),
    # path("v1/users/<int:pk>/", UserDetail.as_view()),
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("~update/", view=user_update_view, name="update"),
    path("<str:email>/", view=user_detail_view, name="detail"),
]
