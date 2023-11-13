from django.urls import path
from . import views

app_name = "APP"
urlpatterns = [
    path("", views.addData, name="addData"),
    path("viewdata", views.viewdata, name="viewdata"),
    path("delete/<data_id>", views.deletedata, name="delete"),
    path("postmethod", views.postmethod, name="postmethod"),
    path("insert", views.insertdata, name="insertdata")
]




