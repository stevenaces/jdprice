import json
import copy
# from django.core.serializers import json
from django.forms import model_to_dict
from django.shortcuts import render
from .models import ProductsInfo
from django.http import HttpResponse

# Create your views here.


def login(request):
    if request.method == 'POST':
        userneme = request.POST.get('username')
        print(userneme)
    return render(request, 'jdPrice/login.html')


def register(request):
    # if request.method == 'POST':
    #     userneme = request.POST.get('username')
    #     print(userneme)
    return render(request, 'jdPrice/register.html')


def queryid(request):
    if request.method == 'POST':
        product_id = request.POST.get('inputid')
        # print(product_id)
        products = ProductsInfo.objects.filter(product_id=product_id)
        # print(type(products))
        # print(len(products))
        brand = list()
        price = list()
        crawl_time = list()
        for product_info in products:
            # print(product_info.brand+" "+product_info.authenticate_moder+" "+str(product_info.price))
            brand.append(product_info.brand)
            price.append(product_info.price)
            crawl_time.append(product_info.crawl_time.strftime('%Y-%m-%d'))

        # print(brand)
        # print(price)
        # print(crawl_time)
        # json_products = model_to_dict(products)
        # json_products = json.dumps(products)
        # print(type(json_products))
        return render(request, 'jdPrice/queryid.html', {
            'price': json.dumps(price),
            'crawl_time': json.dumps(crawl_time)
        })
    return render(request, 'jdPrice/queryid.html')


def multiqueryid(request):
    if request.method == 'POST':
        products_id = request.POST.get('multiinputid')
        # print(product_id)
        multiqueryid = products_id.split(';')
        products_set = []
        for queryid in multiqueryid:
            products_set.append(ProductsInfo.objects.filter(product_id=queryid))

        print(products_set)
        print(type(products_set))
        # print(len(products))

        brand = []
        price_list = []
        # time_price_dict = {}
        price = []
        time = []
        crawl_time_list = []
        crawl_time = []

        for products_info in products_set:
            price.clear()
            crawl_time.clear()
            for product_info in products_info:
                # print(product_info.brand + " " + product_info.authenticate_moder + " " + str(product_info.price) + " " + product_info.crawl_time.strftime('%Y-%m-%d'))
                if product_info.price < 0:
                    price.append('-')
                else:
                    # t = product_info.crawl_time.strftime('%Y-%m-%d')
                    price.append(product_info.price)
                    # time_price_dict['t'] = product_info.price
                if brand == None or product_info.authenticate_moder not in brand:
                    brand.append(product_info.authenticate_moder)

                crawl_time.append(product_info.crawl_time.strftime('%Y-%m-%d'))
                print(price)

            print(price)
            price_list.append(copy.deepcopy(price))
            print(price_list)
            crawl_time_list.append(copy.deepcopy(crawl_time))
            print(crawl_time_list)

        # print(crawl_time_list)
        # 挑选最长时间宽度
        for time_list in crawl_time_list:
            if len(time_list) > len(time):
                time = time_list

        print(brand)
        print(price_list)
        print(time)

        return render(request, 'jdPrice/multiqueryid.html', {
            'brands': json.dumps(brand),
            'price_list': json.dumps(price_list),
            'crawl_time': json.dumps(time)
        })
    return render(request, 'jdPrice/multiqueryid.html')


def smquery(request):
    if request.method == 'POST':
        store = request.POST.get('store')
        product_modle = request.POST.get('productmodle')

        products = ProductsInfo.objects.filter(store=store, authenticate_moder=product_modle)
        print(products)

        product_id_list = []

        for product in products:
            if product_id_list == None or product.product_id not in product_id_list:
                product_id_list.append(product.product_id)

        products_set = []
        for queryid in product_id_list:
            products_set.append(ProductsInfo.objects.filter(product_id=queryid))

        brand = []
        price_list = []
        # time_price_dict = {}
        price = []
        time = []
        crawl_time_list = []
        crawl_time = []
        product_config_list = []
        for products_info in products_set:
            price.clear()
            crawl_time.clear()
            for product_info in products_info:
                if product_info.price < 0:
                    price.append('-')
                else:
                    price.append(product_info.price)
                if product_config_list == None or product_info.brief_introduction not in product_config_list:
                    product_config_list.append(product_info.brief_introduction)

                crawl_time.append(product_info.crawl_time.strftime('%Y-%m-%d'))
                # print(price)

            # print(price)
            price_list.append(copy.deepcopy(price))
            # print(price_list)
            crawl_time_list.append(copy.deepcopy(crawl_time))
            # print(crawl_time_list)

        # print(crawl_time_list)
        # 挑选最长时间宽度
        for time_list in crawl_time_list:
            if len(time_list) > len(time):
                time = time_list

        print(product_config_list)
        # print(price_list)
        # print(time)

        return render(request, 'jdPrice/storeandmodlequery.html', {
            'brands': json.dumps(product_id_list),
            'price_list': json.dumps(price_list),
            'crawl_time': json.dumps(time)
        })
    return render(request, 'jdPrice/storeandmodlequery.html')
