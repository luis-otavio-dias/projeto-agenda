from rest_framework.response import Response
from rest_framework.decorators import api_view
from api.serializers import ContactSerializer
from django.db.models import Count
from contact.models import Contact


@api_view(["GET"])
def getData(request):
    contacts = Contact.objects.all()
    serializer = ContactSerializer(contacts, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def contact_stats(request):
    stats = (
        Contact.objects.filter(category_id__in=[2, 3, 4])
        .values("category__name")
        .annotate(total=Count("id"))
    )

    response_data = {}

    for entry in stats:
        category_name = entry["category__name"]
        print(category_name)
        total = entry["total"]
        response_data[category_name] = total

    return Response(response_data)
