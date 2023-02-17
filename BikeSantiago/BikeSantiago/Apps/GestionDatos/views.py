from django.shortcuts import render
from django.conf import settings
from BikeSantiago.Apps.GestionDatos.models import company, location, network, payment, extra, station, titular, representanteLegal, proyecto
import requests
import json
from bs4 import BeautifulSoup
from django.core import serializers
from django.http import JsonResponse

# Create your views here.
def obtenerInfoAPI(request):
    url = settings.LINK_API
    r = requests.get(url)
    text = r.text

    data = json.loads(text)

    #Elimino la data de todas las tablas
    station.objects.all().delete()
    extra.objects.all().delete()
    payment.objects.all().delete()
    network.objects.all().delete()
    location.objects.all().delete()
    company.objects.all().delete()

    net = data['network']
    comp = net['company']
    gbfs_href = net['gbfs_href']
    href = net['gbfs_href']
    id_network = net['id']

    loc = net['location']
    city = loc['city']
    country = loc['country']
    latitude = loc['latitude']
    longitude = loc['longitude']
    
    l1 = location(city=city, country=country, latitude=latitude, longitude=longitude)
    l1.save()
    
    name = net['name']

    n1 = network(gbfs_href=gbfs_href,href=href,id_network=id_network,location=l1,name=name)
    n1.save()

    for i in comp:
        p1 = company(name=i)
        p1.save()
        n1.company.add(p1)

    stations = net['stations']
    for s in stations:
        empty_slots = s['empty_slots']
        ex = s['extra']
        free_bikes = s['free_bikes']
        id_station = s['id']
        latitude = s['latitude']
        longitude = s['longitude']
        name = s['name']
        timestamp = s['timestamp']

        address = ex['address']
        altitude = ex['altitude']
        ebikes = ex['ebikes']
        has_ebikes = ex['has_ebikes']
        last_updated = ex['last_updated']
        normal_bikes = ex['normal_bikes']
        pay = ex['payment']
        payment_terminal = ex['payment-terminal']
        post_code = ''
        try:
            post_code = ex['post_code']
        except:
            pass
        renting = ex['renting']
        returning = ex['returning']
        slots = ex['slots']
        uid = ex['uid']

        e1 = extra(address=address, altitude=altitude, ebikes=ebikes, has_ebikes=has_ebikes, 
        last_updated=last_updated, normal_bikes=normal_bikes, payment_terminal=payment_terminal, post_code=post_code,
          renting=renting, returning=returning, slots=slots, uid=uid)
        e1.save()

        for p in pay:
            p2 = payment(name=p)
            p2.save()
            e1.payment.add(p2)

        st = station(empty_slots=empty_slots,extra=e1,free_bikes=free_bikes,id_station=id_station,latitude=latitude,
        longitude=longitude,name=name,timestamp=timestamp)
        st.save()

        n1.stations.add(st)
        

    context = {"text":text}
    return render(request, 'Datos.html', context)


def obtenerInfoURL(request):
    r = requests.get(settings.URL)
    soup = BeautifulSoup(r.content)

    #Elimino la data de todas las tablas
    titular.objects.all().delete()
    representanteLegal.objects.all().delete()
    proyecto.objects.all().delete()

    text = ''

    for a_tag in soup.find_all('a', target='_proyecto', href=True):
        r2 = requests.get(a_tag['href'])
        ct = r2.text.replace("</th>","</td>")
        soup2 = BeautifulSoup(ct)
      
        table = soup2.find('table', attrs={'class':'tabla_datos_linea'})
        table_body = table.find('tbody')

        nombre_proyecto = ''
        tipo_proyecto = ''
        monto_inversion = ''
        estado_actual = ''
        encargado = ''
        descripcion_proyecto = ''
        nombre_titular = ''
        domicilio_titular = ''
        ciudad_titular = ''
        telefono_titular = ''
        fax_titular = ''
        email_titular = ''
        nombre_rep = ''
        domicilio_rep = ''
        telefono_rep = ''
        fax_rep = ''
        email_rep = ''

        nombre_proyecto = table_body.find('td', text='Proyecto').find_next('td').text
        tipo_proyecto = table_body.find('td', text='Tipo de Proyecto').find_next('td').text
        monto_inversion = table_body.find('td', text='Monto de Inversión').find_next('td').text
        estado_actual = table_body.find('td', text='Estado Actual').find_next('td').text
        try:
            encargado = table_body.find('td', text='Encargado/a').find_next('td').text
        except:
            pass
        descripcion_proyecto = table_body.find('td', text='Descripción del Proyecto').find_next('td').text

                

        h2 = soup2.find('h2', text='Titular')
        table2 = h2.find_next('table')
        table_body2 = table2.find('tbody')

        
        nombre_titular = table_body2.find("td", text='Nombre').find_next('td').find_next('td').text
        domicilio_titular = table_body2.find("td", text='Domicilio').find_next('td').find_next('td').text
        ciudad_titular = table_body2.find("td", text='Ciudad').find_next('td').find_next('td').text
        telefono_titular = table_body2.find("td", text='Telefono').find_next('td').find_next('td').text
        fax_titular = table_body2.find("td", text='Fax').find_next('td').find_next('td').text
        email_titular = table_body2.find("td", text='E-mail').find_next('td').find_next('td').text

        tit = titular(nombre=nombre_titular, domicilio=domicilio_titular, ciudad=ciudad_titular,
        telefono=telefono_titular,fax=fax_titular,email=email_titular)
        tit.save()

        h2 = soup2.find('h2', text='Representante Legal')
        table2 = h2.find_next('table')
        table_body2 = table2.find('tbody')

        
        nombre_rep = table_body2.find("td", text='Nombre').find_next('td').find_next('td').text
        domicilio_rep = table_body2.find("td", text='Domicilio').find_next('td').find_next('td').text
        telefono_rep = table_body2.find("td", text='Telefono').find_next('td').find_next('td').text
        fax_rep = table_body2.find("td", text='Fax').find_next('td').find_next('td').text
        email_rep = table_body2.find("td", text='E-mail').find_next('td').find_next('td').text

        rep = representanteLegal(nombre=nombre_rep, domicilio=domicilio_rep,
        telefono=telefono_rep,fax=fax_rep,email=email_rep)
        rep.save()

        pro = proyecto(nombre=nombre_proyecto, tipo_proyecto=tipo_proyecto, monto_inversion=monto_inversion,
        estado_actual=estado_actual, encargado=encargado, descripcion_proyecto=descripcion_proyecto,
        titular=tit, representante_legal=rep)
        pro.save()

    posts = proyecto.objects.all()
    data = serializers.serialize('json', posts)
    return JsonResponse(json.loads(data),  safe=False, json_dumps_params={'indent': 2,'ensure_ascii': False})