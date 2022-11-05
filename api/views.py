from rest_framework.response import Response
from rest_framework.decorators import api_view
from home.models import Contact
from .serializers import ContactSerializer


@api_view(['GET'])
def getData(request):
    contacts = Contact.objects.all()
    serializer = ContactSerializer(contacts, many=True)
    return Response({
        'status': True,
        'message': 'Data Fetched successfully',
        'data': serializer.data
    })


@api_view(['POST'])
def addData(request):
    try:
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': True,
                'message': 'Data saved successfully',
                'data': serializer.data
            })
        return Response({
            'status': False,
            'message': 'Invalid data'
        })
    except Exception as e:
        print(e)
        return Response(
            {
                'status': False,
                'message': 'Something went wrong'
            }
        )
