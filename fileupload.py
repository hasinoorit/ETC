from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK
from django.core.files.storage import FileSystemStorage
import imghdr
import time

class UploadPhoto(APIView):

    # Only post method are allowed to upload file
    def post(self, request, format='jpg'):
        # Checking request for file
        if not request.FILES.get('photoFile'):
            return Response({"error": "No file selected"}, status=HTTP_400_BAD_REQUEST)
        myfile = request.FILES['photoFile']
        # checking file size Here file size allowed upto 256kb
        if myfile.size > (1024*256):
            return Response({"error": "File size should not be more than 256 kb"}, status=HTTP_400_BAD_REQUEST)
        # Checking valid image file
        fileType = imghdr.what(myfile)
        if not fileType:
            return Response({"error": "Invalid Image"}, status=HTTP_400_BAD_REQUEST)
        # FileSystemStorage() is using to get media directory
        fs = FileSystemStorage()
        # using unix timestamp to make file name unique
        firstName = str(int(time.time()))
        # getting file extension
        ext = myfile.name.split('.')[-1]
        # generating filename using timestamp and extension
        newFileName = firstName+"."+ext
        # Saving file
        filename = fs.save('product_photo/'+newFileName, myfile)
        # getting file url
        uploaded_file_url = fs.url(filename)
        return Response({"url": uploaded_file_url, "fileType": fileType}, status=HTTP_200_OK)
