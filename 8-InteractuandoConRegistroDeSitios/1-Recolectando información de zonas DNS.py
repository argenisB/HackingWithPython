import dns.resolver

"""
Código de consulta  -  Tipo de consulta
A - Dirección de host
NS - Servidor de nombre de autorización
MD - Destino de correo
MF - Reemisor de correo
CNAME - Nombre canónico para un alias
SOA - Inicio de una zona de autorización
MB - Nombre de dominio de buzón
MG - Miembro de grupo de correos
MR - Nombre de dominio de cambio de nombre de correo
NULL - RR nulo
WKS - Descripción de servicio bien conocido
PTR - Puntero de nombre de dominio
HINFO - Información del host
MINFO - Información de buzón o de lista de correos
MX - Intercambio de correo
TXT - Cadenas de caracteres de texto
AXFR - Transferencia de una zona entera
MAILB - Registros relacionados con los buzones de correo
MAILA - RR de agente de correo
ANY - Todos los registros
"""


def main():
    """
    Función para obtener información de zonas DNS
    """
    consultas = ['A', 'NS', 'SOA', 'MX', 'MF', 'MD', 'ANY', 'HINFO', 'AXFR', 'CNAME', 'TXT']
    for c in consultas:
        try:
            a = dns.resolver.resolve('url', c)  # url, codigo de consulta
            for q in a:
                print(q)
        except:
            print('No pude obtener la consulta')


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Saliendo..')
        exit()
