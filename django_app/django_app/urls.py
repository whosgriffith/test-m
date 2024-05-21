from django.urls import path
from users.views import SignupView, UsersListView
from products.views import ListProductsView

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('users/', UsersListView.as_view(), name='users_list'),
    path('products/', ListProductsView.as_view(), name='products_list'),
]
