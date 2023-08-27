from rest_framework.routers import DefaultRouter
from nextacloudapp import views

router = DefaultRouter() 
router.register(r'employees' , views.EmployeesViewSet, basename='employees')
router.register(r'employers' , views.EmployersViewSet, basename='employers')

urlpatterns = router.urls