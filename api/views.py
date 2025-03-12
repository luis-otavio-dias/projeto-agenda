from rest_framework.response import Response
from rest_framework.decorators import api_view
from contact.models import Contact
from api.serializers import ContactSerializer


@api_view(["GET"])
def getData(request):
    contacts = Contact.objects.all()
    serializer = ContactSerializer(contacts, many=True)
    return Response(serializer.data)
