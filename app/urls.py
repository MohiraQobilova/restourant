from django.urls import path
from .import views 



urlpatterns =[
    path('base/',views.base,name='base'),
    path('',views.index,name='home'),
    path('about/',views.about,name='about_page'),
    path('book/',views.book,name='book_page'),
    path('search/',views.search_resault,name='search_resaults'),
    path('profile/', views.profile, name="profile"),
    path('profile/update', views.update_profile, name="update_profile"),
    path('cart/',views.cart,name='cart'),
    path('cart/add/',views.add_to_cart,name='add_to_cart'),
    path('cart/update/<int:item_id>/', views.update_cart, name='update_cart'),
    path('cart/delete/<int:item_id>/', views.delete_cart, name='delete_cart'),
    path('menu/',views.menu_detail,name='menu_detail_url'),
    path('product/<slug:slug>/',views.product_detail,name='product_detail_url'),
    path('register',views.register,name='register'),
    path('order/', views.order, name="order"),
    path('orders/', views.orders, name="orders"),  # hamma zakazlar adminga
    path('orders/<int:order_id>/change-status/', views.change_status, name="change_status"),
]   