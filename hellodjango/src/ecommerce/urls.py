from django.urls import path

from ecommerce import views

urlpatterns = [
    path("", views.product_model_list_view, name="list"),
    path("<int:product_id>", views.product_model_details_view, name="details"), #añadimos esto para recibir el product_id
    path("create", views.product_model_create_view, name="create"), #path para crear vistas
    path("<int:product_id>/edit", views.product_model_update_view, name="details"),
    path("<int:product_id>/delete", views.product_model_delete_view, name ="delete") # path para delete
]
