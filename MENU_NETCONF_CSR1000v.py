#!/usr/bin/env python3
# AUTOR: FRANCISCO JAVIER PENON CAMAR
# CURSO: Becas Digitaliza: Devnet- Ene 20
# Script de conexión con CSR1000v (acceso local y por Sandbox)

from ncclient import manager
import xmltodict
import xml.dom.minidom

# definimos las funciones para la eleccion del menú de entrada


def get_device_running():

    # Definimos conexión
    con = manager.connect(host="192.168.56.101", port=830,
                          username="cisco", password="cisco123!", hostkey_verify=False)

    # recoger información del dispositivo
    netconf_reply = con.get_config(source="running")

    # printamos configuración
    # print(netconf_reply)
    print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())


def create_interface():
    # Definimos conexión
    con = manager.connect(host="192.168.56.101",port=830,username="cisco",password="cisco123!",hostkey_verify=False)
    # Creamos un filtro pra Netconf
    # Creamaos una plantilla para ietf-interfaces
    netconf_interface_template = """
    <config>
        <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
            <interface>
                <name>{name}</name>
                <description>{desc}</description>
                <type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">
                    ianaift:softwareLoopback
                </type>
                <enabled>{status}</enabled>
                <ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
                    <address>
                        <ip>{ip_address}</ip>
                        <netmask>{mask}</netmask>
                    </address>
                </ipv4>
            </interface>
         </interfaces>
    </config>"""
    # Detalles de las interfaces a añadir
    new_loopback = {}
    new_loopback["name"] = "Loopback" + input("¿Que número de loopback añadimos? ")
    new_loopback["desc"] = input("¿Que descripción tiene? ")
    #new_loopback["type"] = ["ianaift:softwareloopback"]
    new_loopback["status"] = "true"
    new_loopback["ip_address"] = input("Dirección IP? ")
    new_loopback["mask"] = input("¿Mascara de subred? ")
    
    # cargamos los datos en la nueva interfaz
    netconf_data = netconf_interface_template.format(
            name = new_loopback["name"],
            desc = new_loopback["desc"],
            #type = new_loopback["type"],
            status = new_loopback["status"],
            ip_address = new_loopback["ip_address"],
            mask = new_loopback["mask"]
        )
    netconf_reply = con.edit_config(netconf_data, target = 'running') 



def delete_interface():
    # Definimos conexión
    con = manager.connect(host="192.168.56.101",port=830,username="cisco",password="cisco123!",hostkey_verify=False)
    
    netconf_interface_template = """
     <config>
         <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
             <interface operation="delete">
                 <name>{name}</name>
             </interface>
         </interfaces>
     </config>"""
    
    new_loopback = {}
    new_loopback["name"] = "Loopback" + input("¿Que número de loopback eliminamos? ")
    # Actualizamos los datos en la interfaz
    netconf_data = netconf_interface_template.format(
            name = new_loopback["name"])
    netconf_reply = con.edit_config(netconf_data, target = 'running')        


def show_routing():

    #Usamos NETCONF para conectarnos con el Router.
    #recibimos las rutas por defecto IPv4, y las mostramos como diccionario
    
    filter = """
        <filter>
             <routing-state xmlns="urn:ietf:params:xml:ns:yang:ietf-routing"
                           xmlns:rt="urn:ietf:params:xml:ns:yang:ietf-routing">
                <routing-instance>
                    <name>default</name>
                    <ribs>
                        <rib>
                            <name>ipv4-default</name>
                        </rib>
                    </ribs>
                </routing-instance>
            </routing-state>
        </filter>
        """
    
        # Definimos conexión con router de DevNet Sandbox.
        # (En el momento de realizar el programa no era necesario crear VPN con Cisco)
        
    with manager.connect(
         host="ios-xe-mgmt.cisco.com",
         port=10000,
         username="developer",
         password="C1sco12345",
         hostkey_verify=False,
    ) as m:
     
        
        r = m.get(filter)
        
                
        # Procesamos los datos como diccionario
    response_dict = xmltodict.parse(r.xml)
    
    routes = response_dict["rpc-reply"]["data"]["routing-state"][
        "routing-instance"
    ]["ribs"]["rib"]["routes"]["route"]
        
    print(routes)

    
# Menú de selección de consulta

print("Seleccione operación:\n"
      "1. Visualizar configuración\n"
      "2. Crear Interafces (loopback)\n"
      "3. Borrar interfaces (loopback)\n"
      "4. Visualización tabla de Routing\n")

select = input("Seleccione operación 1, 2, 3, 4 :")

if select == '1':
    print(get_device_running())

elif select == '2':
    print(create_interface())

elif select == '3':
    print(delete_interface())

elif select == '4':
    print(show_routing())    

else:
    print("Invalid input")
