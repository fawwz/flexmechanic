from django.shortcuts import render, redirect, get_object_or_404
from .models import Garage, Services
from account.models import Mechanic
from taggit.models import Tag
from taggit.utils import parse_tags




# Create your views here.
def garages_regist(request):
    if request.method == 'POST':
        garage_name = request.POST['garage_name']
        address = request.POST['address']
        services_input = request.POST['services']

        # services = [service.strip() for service in services_input.split(',') if service.strip()]
        # print(services)

        # Get the mechanic instance of the logged-in user
        user = request.user
        mechanic_instance = Mechanic.objects.get(user_profile = user)
        
        # Create the garage and associate it with the mechanic instance
        garage = Garage.objects.create(garage_name=garage_name, address=address, mechanic=mechanic_instance)
        # garage.save()

        tags_input = services_input
        tags = parse_tags(tags_input)

        # Create an instance of the Services model and associate it with the garage
        services_instance = Services.objects.create(garage=garage)

        # Set the tags for the services_instance object
        services_instance.services_name.set(tags)

        # for service in services:
        #     service_obj, _ = Services.objects.get_or_create(garage=garage)
        #     service_obj.services_name.add(parse_tags(service))
        #     # Services.services_name.add(service)

        return render(request,'garagesregist/success.html')  # Redirect to a success page
    else:
        return render(request, 'garagesregist/real_garages_regist.html')

