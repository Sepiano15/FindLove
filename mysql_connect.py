import mysql.connector
import sshtunnel

sshtunnel.SSH_TIMEOUT = 5.0
sshtunnel.TUNNEL_TIMEOUT = 5.0

with sshtunnel.SSHTunnelForwarder(
    ('ssh.pythonanywhere.com'),
    ssh_username='Noriaki', ssh_password='wp2vmffjtm+',
    remote_bind_address=('Noriaki.mysql.pythonanywhere-services.com', 3306)
) as tunnel:
    connection = mysql.connector.connect(
        user='Noriaki', password='wp2vmffjtm+',
        host='127.0.0.1', port=tunnel.local_bind_port,
        database='Noriaki$findlove',
    )
    # Do stuff
    connection.close()
