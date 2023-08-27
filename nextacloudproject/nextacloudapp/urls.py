from rest_framework.routers import DefaultRouter
from nextacloudapp import views

router = DefaultRouter()
router.register(r'items', views.ItemsViewSet, basename='items')
router.register(r'brands', views.BrandsViewSet, basename='brands')
router.register(r'stores', views.StoreViewSet, basename='stores')
router.register(r'staff', views.StaffViewSet, basename='staff')


urlpatterns = router.urls