from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import IntegrityError
from .models import Employee, Attendance
from .serializers import EmployeeSerializer, AttendanceSerializer


class EmployeeListCreateView(APIView):
    def get(self, request):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except IntegrityError as e:
                if 'employee_id' in str(e):
                    return Response(
                        {'error': 'Employee ID already exists.'},
                        status=status.HTTP_400_BAD_REQUEST
                    )
                elif 'email' in str(e):
                    return Response(
                        {'error': 'Email already exists.'},
                        status=status.HTTP_400_BAD_REQUEST
                    )
                return Response(
                    {'error': 'Duplicate entry error.'},
                    status=status.HTTP_400_BAD_REQUEST
                )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmployeeDetailView(APIView):
    def get_object(self, pk):
        try:
            return Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            return None

    def get(self, request, pk):
        employee = self.get_object(pk)
        if not employee:
            return Response(
                {'error': 'Employee not found.'},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)

    def put(self, request, pk):
        employee = self.get_object(pk)
        if not employee:
            return Response(
                {'error': 'Employee not found.'},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
                return Response(serializer.data)
            except IntegrityError as e:
                if 'employee_id' in str(e):
                    return Response(
                        {'error': 'Employee ID already exists.'},
                        status=status.HTTP_400_BAD_REQUEST
                    )
                elif 'email' in str(e):
                    return Response(
                        {'error': 'Email already exists.'},
                        status=status.HTTP_400_BAD_REQUEST
                    )
                return Response(
                    {'error': 'Duplicate entry error.'},
                    status=status.HTTP_400_BAD_REQUEST
                )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        employee = self.get_object(pk)
        if not employee:
            return Response(
                {'error': 'Employee not found.'},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = EmployeeSerializer(employee, data=request.data, partial=True)
        if serializer.is_valid():
            try:
                serializer.save()
                return Response(serializer.data)
            except IntegrityError as e:
                if 'employee_id' in str(e):
                    return Response(
                        {'error': 'Employee ID already exists.'},
                        status=status.HTTP_400_BAD_REQUEST
                    )
                elif 'email' in str(e):
                    return Response(
                        {'error': 'Email already exists.'},
                        status=status.HTTP_400_BAD_REQUEST
                    )
                return Response(
                    {'error': 'Duplicate entry error.'},
                    status=status.HTTP_400_BAD_REQUEST
                )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        employee = self.get_object(pk)
        if not employee:
            return Response(
                {'error': 'Employee not found.'},
                status=status.HTTP_404_NOT_FOUND
            )
        try:
            employee.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response(
                {'error': 'Failed to delete employee.'},
                status=status.HTTP_400_BAD_REQUEST
            )


class EmployeeAttendanceView(APIView):
    def get(self, request, pk):
        try:
            employee = Employee.objects.get(pk=pk)
            attendance = employee.attendance_records.all()
            serializer = AttendanceSerializer(attendance, many=True)
            return Response(serializer.data)
        except Employee.DoesNotExist:
            return Response(
                {'error': 'Employee not found.'},
                status=status.HTTP_404_NOT_FOUND
            )


class AttendanceListCreateView(APIView):
    def get(self, request):
        attendance = Attendance.objects.all()
        serializer = AttendanceSerializer(attendance, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AttendanceSerializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except IntegrityError:
                return Response(
                    {'error': 'Attendance record already exists for this employee on this date.'},
                    status=status.HTTP_400_BAD_REQUEST
                )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AttendanceDetailView(APIView):
    def get_object(self, pk):
        try:
            return Attendance.objects.get(pk=pk)
        except Attendance.DoesNotExist:
            return None

    def get(self, request, pk):
        attendance = self.get_object(pk)
        if not attendance:
            return Response(
                {'error': 'Attendance record not found.'},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = AttendanceSerializer(attendance)
        return Response(serializer.data)

    def put(self, request, pk):
        attendance = self.get_object(pk)
        if not attendance:
            return Response(
                {'error': 'Attendance record not found.'},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = AttendanceSerializer(attendance, data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
                return Response(serializer.data)
            except IntegrityError:
                return Response(
                    {'error': 'Attendance record already exists for this employee on this date.'},
                    status=status.HTTP_400_BAD_REQUEST
                )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        attendance = self.get_object(pk)
        if not attendance:
            return Response(
                {'error': 'Attendance record not found.'},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = AttendanceSerializer(attendance, data=request.data, partial=True)
        if serializer.is_valid():
            try:
                serializer.save()
                return Response(serializer.data)
            except IntegrityError:
                return Response(
                    {'error': 'Attendance record already exists for this employee on this date.'},
                    status=status.HTTP_400_BAD_REQUEST
                )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        attendance = self.get_object(pk)
        if not attendance:
            return Response(
                {'error': 'Attendance record not found.'},
                status=status.HTTP_404_NOT_FOUND
            )
        attendance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AttendanceByEmployeeView(APIView):
    def get(self, request):
        employee_id = request.query_params.get('employee_id')
        if not employee_id:
            return Response(
                {'error': 'employee_id parameter is required.'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            employee = Employee.objects.get(employee_id=employee_id)
            attendance = employee.attendance_records.all()
            serializer = AttendanceSerializer(attendance, many=True)
            return Response(serializer.data)
        except Employee.DoesNotExist:
            return Response(
                {'error': 'Employee not found.'},
                status=status.HTTP_404_NOT_FOUND
            )


class AttendanceSummaryView(APIView):
    def get(self, request):
        employee_id = request.query_params.get('employee_id')
        if not employee_id:
            return Response(
                {'error': 'employee_id parameter is required.'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            employee = Employee.objects.get(employee_id=employee_id)
            attendance = employee.attendance_records.all()
            total_present = attendance.filter(status='Present').count()
            total_absent = attendance.filter(status='Absent').count()
            total_days = attendance.count()
            
            return Response({
                'employee_id': employee.employee_id,
                'full_name': employee.full_name,
                'total_days': total_days,
                'total_present': total_present,
                'total_absent': total_absent,
            })
        except Employee.DoesNotExist:
            return Response(
                {'error': 'Employee not found.'},
                status=status.HTTP_404_NOT_FOUND
            )
