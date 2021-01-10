
from django.urls import path
from .import views

urlpatterns = [
    path("", views.index, name="ShopHome"),
    path("about/", views.about, name="About US"),
    path("home/", views.home, name="Home"),
    path("productsview/<int:myid>", views.productsview, name="product"),
    path("search/", views.search, name="Search"),
    path("contact/", views.contact, name="Contact Us"),
    path("tracker/", views.tracker, name="Shipping Tracker"),
    path("checkout/", views.checkout, name="Checkout"),
    path("privacy/", views.privacy, name="Privacy Policy"),
    path("termsandcondition/", views.termsandcondition, name="Terms and Conditions")
]
