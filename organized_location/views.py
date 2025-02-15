import os
import pandas as pd
from django.conf import settings
from django.core.files.storage import default_storage
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from rest_framework import status
from .models import OrganizedLocation
from .serializers import OrganizedLocationSerializer
from rest_framework.generics import ListAPIView

class UploadCSVView(APIView):
    parser_classes = [MultiPartParser]

    def post(self, request, format=None):
        file = request.FILES.get('file')

        if not file:
            return Response({'error': 'No file uploaded'}, status=status.HTTP_400_BAD_REQUEST)

        # Define the upload directory
        upload_dir = os.path.join(settings.MEDIA_ROOT, 'uploads')
        os.makedirs(upload_dir, exist_ok=True)

        # Save the file
        file_path = os.path.join(upload_dir, file.name)
        with default_storage.open(file_path, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)

        # Read file
        try:
            if file.name.endswith('.csv'):
                try:
                    df = pd.read_csv(file_path, encoding='utf-8')
                except UnicodeDecodeError:
                    df = pd.read_csv(file_path, encoding='ISO-8859-1')

            elif file.name.endswith('.xlsx'):
                df = pd.read_excel(file_path, engine='openpyxl')

            else:
                return Response({'error': 'Unsupported file format'}, status=status.HTTP_400_BAD_REQUEST)

            # Convert all NaN values to empty strings
            df = df.fillna('')

            # Convert all data to string except lat/lon
            for _, row in df.iterrows():
                OrganizedLocation.objects.create(
                    appt_file_name=str(row.get('ApptFileName', '')),
                    location_number=str(row.get('LocationNumber', '')),
                    location_name=str(row.get('LocationName', '')),
                    organization=str(row.get('Organization', '')),
                    address=str(row.get('Address', '')),
                    lat=float(row.get('lat', 0.0)) if row.get('lat') else None,
                    lon=float(row.get('lon', 0.0)) if row.get('lon') else None,
                    active_status=str(row.get('Active Status', '')),
                    pelvic_health=str(row.get('Pelvic Health', '')),
                    training_haus=str(row.get('Training Haus', '')),
                    anytime_fitness=str(row.get('Anytime Fitness', '')),
                    concussion=str(row.get('Concussion', '')),
                    urgent_care=str(row.get('Urgent Care', '')),
                    nutrition_center=str(row.get('Nutrition Center', ''))
                )

            return Response({'message': 'File uploaded and processed successfully'}, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class OrganizedLocationListView(ListAPIView):
    queryset = OrganizedLocation.objects.all()
    serializer_class = OrganizedLocationSerializer
