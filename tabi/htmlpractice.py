from django.views import generic
from django.contrib.auth import views as auth_views

from .models import Hotel, Mylist
from .forms import InquiryForm
import requests

# Create your views here.

class IndexView(generic.TemplateView):
    template_name = "index.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(self.request.GET)
        if 'search' in self.request.GET:

            #楽天api, hotpapper apiが入る
            REQUEST_URL = 'http://webservice.recruit.co.jp/hotpepper/gourmet/v1/'
            APP_ID = '94dbf118bb25a8a9'

            params = {
                'format': 'json',
                'keyword': self.request.GET['search'],
                'key': APP_ID
            }

            hotpepperAPIresponse = requests.get(REQUEST_URL, params)
            hotpepperresponse = hotpepperAPIresponse.json()
            context['hotpepper'] = hotpepperresponse['results']
            import pprint
            pprint.pprint(hotpepperresponse)

        return context

class Restaurantidview(generic.TemplateView):
    template_name = "restaurantid.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        print(self.kwargs['restaurantid'])
        #次にhotpepperに問い合わせる
        # 楽天api, hotpapper apiが入る
        REQUEST_URL = 'http://webservice.recruit.co.jp/hotpepper/gourmet/v1/'
        APP_ID = '94dbf118bb25a8a9'

        #ヒント:getパラメータは使わない　押した店の情報を受け取るには
        params = {
            'format': 'json',
            'keyword': 'id',
            'key': APP_ID
        }

        hotpepperAPIresponse = requests.get(REQUEST_URL, params)
        hotpepperresponse = hotpepperAPIresponse.json()
        context['hotpepper'] = hotpepperresponse['results']
        import pprint
        pprint.pprint(hotpepperresponse)


        #hotpepperからのresponseをcontext['shop']にいれる
        context['shop']= {'name':'aaa'}
        return context

class LoginView(auth_views.LoginView):
    template_name = "login.html"

class LogoutView(auth_views.LogoutView):
    pass

class HotelView(generic.ListView):
    model = Hotel
    template_name = "hotel.html"

class AirticketView(generic.TemplateView):
    template_name = "airticket.html"

class InquiryView(generic.FormView):
    template_name = "inquiry.html"
    form_class = InquiryForm

class RestaurantView(generic.TemplateView):
    template_name = "restaurant.html"

class MylistView(generic.ListView):
    model = Mylist
    template_name = "mylist.html"
