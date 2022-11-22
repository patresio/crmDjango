from django.urls import path
from . import views

urlpatterns = [
    #login
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutPage, name="logout"),
    path('register/', views.registerPage, name="register"),
    #User
    path('user/', views.userPage, name="user-page"),
    path('account/', views.accountSettings, name="account"),
    #dashboard
    path('', views.home, name='home'),
    path('customer/<str:pk>', views.customer, name='customer'),
    path('products/', views.products, name='products'),
    #orders
    path('create_order/<str:pk>/', views.createOrder, name='create_order'),
    path('update_order/<str:pk>/', views.updateOrder, name='update_order'),
    path('delete_order/<str:pk>/', views.deleteOrder, name='delete_order'),
    #products
    path('create_product/', views.createProduct, name='create_product'),
]

'''
1 - Submit email form                       //PasswordResetView.as_view()
2 - Email sent success messages             //PasswordResetDoneView.as_view()
3 - Link to password Rest form in email     //PasswordResetConfirmView.as_view()
4 - Password successfully changed message   //PasswordResetCompleteView.as_view()
'''