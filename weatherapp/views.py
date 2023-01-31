from django.shortcuts import render
import requests  


def home(request):
    if request.method=='POST':
        city=request.POST.get('city')
        API_KEY='add your key' # removed for security purpose
        URL=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'
        datadetail= requests.get(URL).json()
        print(datadetail)

        weather={
             'city': city,  
            "country_code": str(datadetail['sys']['country']),  
            "coordinate": str(datadetail['coord']['lon']) + ' '  
                            + str(datadetail['coord']['lat']),  
            "temp": str("%.2f"%((datadetail['main']['temp'])-273)) + '  celsius',  
            "pressure": str(datadetail['main']['pressure']),  
            "humidity": str(datadetail['main']['humidity']),  

        }

    else:
        weather={}


    return render(request,'home.html',weather)



