#! /usr/bin/env python3
import requests
import json
import urllib3
from pprint import pprint


# Definimos la función que alamcenará el ticket de APIC-EM

def get_auth_token():
    requests.packages.urllib3.disable_warnings()
    url = "https://devnetsbx-netacad-apicem-3.cisco.com/api/v1/ticket"
    headers = {
        "content-type": "application/json"
    }
    body_json = {
        "password": "Xj3BDqbU",
        "username": "devnetuser"
    }
    resp = requests.post(url,json.dumps(body_json),headers=headers,verify=False)  
    response_json = resp.json()
    serviceTicket = response_json["response"]["serviceTicket"]
    #print (serviceTicket)   
    return serviceTicket

if __name__ == "__main__":
  get_auth_token()

# Definimos las funciones para la elección en el menú de entrada

def get_device_list():
    
    requests.packages.urllib3.disable_warnings()
    url = "https://devnetsbx-netacad-apicem-3.cisco.com/api/v1/network-device"
    token = get_auth_token()
    headers = {
        "Content-Type" : "application/json",
        "X-Auth-Token" : token
    }
    resp = requests.get(url,headers=headers,verify=False)
    response_json = resp.json()
    #pprint(response_json)
    for equipo in response_json['response']:
       print("el hostname",equipo['hostname'],"pertenece a la familia",equipo["family"],"su Mac",equipo["macAddress"])

  


def get_host_list():
    
    requests.packages.urllib3.disable_warnings()
    url = "https://devnetsbx-netacad-apicem-3.cisco.com/api/v1/host"
    token = get_auth_token()
    headers = {
        "Content-Type" : "application/json",
        "X-Auth-Token" : token
    }
    resp = requests.get(url,headers=headers,verify=False)
    response_json = resp.json()
    #pprint(response_json)
    for equipo in response_json['response']:
        print("hostIp",equipo['hostIp'],"vlanId",equipo["vlanId"],"id",equipo["id"])

  


def get_interfaces_list():
    
    requests.packages.urllib3.disable_warnings()
    url = "https://devnetsbx-netacad-apicem-3.cisco.com/api/v1/interface"
    token = get_auth_token()
    headers = {
        "Content-Type" : "application/json",
        "X-Auth-Token" : token
    }
    resp = requests.get(url,headers=headers,verify=False)
    response_json = resp.json()
    #pprint(response_json)
    for equipo in response_json['response']:
        print("className",equipo['className'],"status",equipo["status"],"ipv4Address",equipo["ipv4Address"],"interfaceType",equipo["interfaceType"])

  
def Ip_Geolocation():
    
    requests.packages.urllib3.disable_warnings()
    url = "https://devnetsbx-netacad-apicem-3.cisco.com/api/v1/ipgeo/"+ipwan
    token = get_auth_token()
    headers = {
        "Content-Type" : "application/json",
        "X-Auth-Token" : token
    }
    resp = requests.get(url,headers=headers,verify=False)
    response_json = resp.json()
    pprint(response_json)
    

# Menú de selección de consulta

print("Seleccione operación:\n"  
        "1. NETWORK_DEVICES\n" 
        "2. HOST\n" 
        "3. INTERFACES\n"  
        "4. IP GEOLOCALIZACION\n") 
 
select = input("Seleccione operación 1, 2, 3, 4 :")
  
  
if select == '1': 
    print(get_device_list()) 
  
elif select == '2': 
    print(get_host_list()) 
  
elif select == '3': 
    print(get_interfaces_list())

elif select == '4':
    ipwan = str(input("dirección ip Wan :"))
    print(Ip_Geolocation())

else: 
    print("Invalid input")    
