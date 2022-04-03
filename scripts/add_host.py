import os


def add_host(domain: str, host: str) -> None:
    """Add a new vhost on apache2."""
    txt_file = "<VirtualHost *:80>"
    txt_file += f"\n\tServerName {domain}"
    txt_file += f"\n\tProxyPass / {host}"
    txt_file += "\n</VirtualHost>"

    with open(f"/etc/apache2/sites-available/{domain}.conf", "w") as file:
        file.write(txt_file)
    
    os.system("service apache2 start")
    os.system(f"a2ensite {domain}.conf")
    os.system("service apache2 reload")
    

if __name__ == '__main__':
    domain = input('Domain (e.g.: example.my-host.com.br): ')
    host = ''
    while not host.startswith('http'):        
        host = input('Host (e.g.: "http://127.0.0.1:3000/"): ')
    if not host.endswith('/'):
        host += '/'

    add_host(domain, host)