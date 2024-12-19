from django.shortcuts import render
import urllib.request
import json
from django.shortcuts import render,redirect
from .forms import MemberForm
from .models import Member

# Create your views here.

def index(request):

    if request.method == 'POST':
        city = request.POST['city']

        source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=<API-KEY-GOES-HERE>').read()
        list_of_data = json.loads(source)

        data = {
            "country_code": str(list_of_data['sys']['country']),
            "coordinate": str(list_of_data['coord']['lon']) + ', '
            + str(list_of_data['coord']['lat']),

            "temp": str(list_of_data['main']['temp']) + ' °C',
            "pressure": str(list_of_data['main']['pressure']),
            "humidity": str(list_of_data['main']['humidity']),
            'main': str(list_of_data['weather'][0]['main']),
            'description': str(list_of_data['weather'][0]['description']),
            'icon': list_of_data['weather'][0]['icon'],
        }
        print(data)
    else:
        data = {}

    return render(request, "main/index.html", data)


def add_member(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
                      
    else:
        form = MemberForm()
        
    return render(request, 'main/addMember.html', {'form':form})    


def members_list (request):
    members = Member.objects.all()
    return render(request, 'main/memberslist.html', {'members': members})
