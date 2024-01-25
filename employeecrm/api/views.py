from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework import authentication,permissions

from api.models import Employees,Tasks
from api.serializers import EmployeeSerializer,TaskSerializer



class EmployeeViewSetView(viewsets.ViewSet):
    def list(self,request,*args,**kwargs):
        qs=Employees.objects.all()
        serializer=EmployeeSerializer(qs,many=True)
        return Response(data=serializer.data)


    def retrieve(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Employees.objects.get(id=id)
        serializer=EmployeeSerializer(qs)
        return Response(data=serializer.data)
    
    def create(self,request,*args,**kwargs):
        serializer=EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)  
        else:
            return Response(data=serializer.errors)  
        

    def update(self,request,*args,**kwargs):
        id=kwargs.get("pk")    
        employee_object=Employees.objects.get(id=id)
        serializer=EmployeeSerializer(data=request.data,instance=employee_object)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
        

    def  destroy(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Employees.objects.get(id=id).delete()
        return Response(data=({"message":"data deleted successfully"}))  
   

        
class EmployeeModeViewSetView(viewsets.ModelViewSet):
    permission_classes=[permissions.IsAdminUser]
    authentication_classes=[authentication.TokenAuthentication]
    serializer_class=EmployeeSerializer
    model=Employees
    queryset=Employees.objects.all()


    def list(self,request,*args,**kwargs):
        qs=Employees.objects.all()
        print(request.query_params)
        if "department" in request.query_params:
            value=request.query_params.get("department")
            print(value)
            qs=qs.filter(department=value)

        serializer=EmployeeSerializer(qs,many=True)
        return Response(data=serializer.data)    
        # localhost:8000/api/v2/employees//category=HR

# localhost:8000/v2/employees/departments/ 
    #methods=post
    @action(methods=["get"],detail=False)
    def departments(self,request,*args,**kwargs):
        data=Employees.objects.all().values_list("department",flat=True)
        return Response(data=data)
# assign a task to an employee
# localhost:8000/api/v2/employee{id}/add_task
    @action(methods=["post"],detail=True)  
    def add_task(self,request,*args,**kwargs):
        id=kwargs.get("pk")  
        employee_object=Employees.objects.get(id=id)
        serializer=TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(employee=employee_object)
            return Response(data=serializer.data)  
        else:
            return Response(data=serializer.errors)

# localhost:8000/api/v2/employees/{id}/tasks/
# to take all the tasks assigned to an employee
    @action(detail=True, methods=['get'])
    def Tasks(self,request,*args,**kwargs) :
        id=kwargs.get("pk")   
        employee_object=Employees.objects.get(id=id)
        qs=Tasks.objects.filter(employee=employee_object)
        # qs=Tasks.objects.filter(employee__id=id)#so that employee will be redirected Employee model
        serializer=TaskSerializer(qs,many=True)
        return Response(data=serializer.data)
    # or
    # id=kwargs.get("pk")   
    
        # qs=Tasks.objects.filter(employee__id=id)#so that employee will be redirected Employee model
    
    # localost:8000/api/v2/task/{taskid}/update/
    # method:put


    
class TaskView(viewsets.ViewSet):

    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    def update(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        task_object=Tasks.objects.get(id=id)
        serializer=TaskSerializer(data=request.data,instance=task_object)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
        


    def  retrieve(self,request,*args,**kwargs):
        id=kwargs.get("pk")    
        qs=Tasks.objects.get(id=id)
        serializer=TaskSerializer(qs)
        return Response(data=serializer.data)


    def destroy(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Tasks.objects.get(id=id).delete()
        return Response(data={"message":"deleted"})


