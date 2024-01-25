from django.urls import path
from api import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import ObtainAuthToken



router=DefaultRouter()
router.register("v1/employees",views.EmployeeViewSetView,basename="employ")
router.register("v2/employees",views.EmployeeModeViewSetView,basename="employee")
router.register("v2/task",views. TaskView,basename="task")

urlpatterns=[
    path("v2/token/",ObtainAuthToken.as_view())
]+router.urls