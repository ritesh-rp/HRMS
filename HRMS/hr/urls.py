from django.urls import path
from .views import (
    EmployeeListCreateView,
    EmployeeDetailView,
    EmployeeAttendanceView,
    AttendanceListCreateView,
    AttendanceDetailView,
    AttendanceByEmployeeView,
    AttendanceSummaryView,
)

urlpatterns = [
    path('employees/', EmployeeListCreateView.as_view(), name='employee-list-create'),
    path('employees/<int:pk>/', EmployeeDetailView.as_view(), name='employee-detail'),
    path('employees/<int:pk>/attendance/', EmployeeAttendanceView.as_view(), name='employee-attendance'),
    path('attendance/', AttendanceListCreateView.as_view(), name='attendance-list-create'),
    path('attendance/<int:pk>/', AttendanceDetailView.as_view(), name='attendance-detail'),
    path('attendance/by-employee/', AttendanceByEmployeeView.as_view(), name='attendance-by-employee'),
    path('attendance/summary/', AttendanceSummaryView.as_view(), name='attendance-summary'),
]
