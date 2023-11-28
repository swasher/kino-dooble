from django.urls import path
from kinozal import views

app_name = "kinozal"

urlpatterns = [
    path('', views.movies, name='movies'),
    path('upload_csv/', views.upload_csv, name='upload_csv'),
    path('parse_test/', views.parse_test, name='parse_test'),
    # path('order_print/<orderid>', views.order_print, name='order_print'),
]

# htmx = [
#     path('order_edit/', views.order_edit, name='order_edit'),
#     path('order_edit/<int:pk>/', views.order_edit, name='order_edit'),
#     path('detail_inline/', views.detail_inline, name='detail_inline'),
#     path('add_detail_formset/<int:current_total_formsets>', views.add_detail_formset, name='add_detail_formset')
# ]
#
# urlpatterns += htmx