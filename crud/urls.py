from django.urls import path
from . import views
from .views import EmployeeUpdateView, EmployeeDeleteView

urlpatterns = [
    path('', views.home, name='home'),
    path('add-employee/', views.addEmployee, name='add_employee'),
    path('emp/<int:pk>/update/', EmployeeUpdateView.as_view(), name='emp-update'),
    path('emp/<int:pk>/delete/', EmployeeDeleteView.as_view(), name='emp-delete')
]
