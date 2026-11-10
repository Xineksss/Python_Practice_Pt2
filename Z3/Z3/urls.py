from django.contrib import admin
from django.urls import path
from Z3app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('customers/', views.customers, name='customers'),
    path('customers/create/', views.create_client, name='create_client'),
    path('customers/edit/<int:id>/', views.edit_client, name='edit_client'),
    path('customers/delete/<int:id>/', views.delete_client, name='delete_client'),
    path('products/', views.products, name='products'),
    path('products/create/', views.create_gpu, name='create_gpu'),
    path('products/create_gpus/', views.create_gpus_new, name='create_gpus_new'),
    path('sale/', views.purchase, name='sale'),
    path('sale_progress', views.sale_progress, name='sale_progress'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
