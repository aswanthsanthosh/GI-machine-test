from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import UserSerializer
import pandas as pd
from django.db import transaction


# Create your views here.

class CSVUploadView(APIView):
    def post(self, request):
        file = file = request.FILES.get('file')
        if not file.name.endswith('.csv'):
            return Response({"error": "File must be a CSV."}, status=status.HTTP_400_BAD_REQUEST)
        
        file_data = pd.read_csv(file, encoding='utf-8', na_values=['', 'NULL', 'None'])
        file_data = file_data.where(pd.notnull(file_data), None).to_dict(orient='records')
        print(file_data)
        success_count = 0
        errors = []

        with transaction.atomic():
            for data_ in file_data:
                serializer = UserSerializer(data=data_)
                if serializer.is_valid():
                    serializer.save()
                    success_count += 1
                else:
                    errors.append({"data": data_, "errors": serializer.errors})


        return Response({
            "total_succesfuly_saved": success_count,
            "rejected_datas": len(errors),
            "errors": errors
        }, status=status.HTTP_201_CREATED)
        

