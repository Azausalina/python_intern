from typing import Optional
from fastapi import FastAPI
import requests
import sys


"""
app example

"""

host_checker = FastAPI()

@host_checker.get("/foo")
def check_host(hostname: Optional[str] = None):
    if hostname is None:
        return {"error" : "hostname is not specifide"}

    answer = is_alive_host(hostname)
    return {"status" : "up" if answer else "down"}

def is_alive_host(hostname):
    """Проверить, что запрашиваемый хост возвращает http status 100<=x<400."""
    if type(hostname) != str:
        raise TypeError("hostname must be str not {}".format(type(hostname)))

    host_url = hostname

    if not hostname.startswith("http://") and not hostname.startswith("https://"):
        host_url = 'http://' + host_url

    try:
        r = requests.get(host_url)
        if 100 <= r.status_code < 400:
            return True
    except requests.exceptions.ConnectionError as err:
        print("Error: {}".format(err))
    return False


def help():
    print("Params:")
    print("\tmode:\tstatus\t\tcheck hostname status")
    print("\tmode:\tapp\t\tstart app")
    print("\thostame: <hostname>\thostname for check status (Needed for status mode)")
    print("\nExample: python3 app.py mode=status hostname=http://google.com")
    exit()

if __name__ == "__main__":

    try:
        params = {key:value for key,value in map(lambda x: x.lower().split("="), sys.argv[1:])}
    except:
        help()

    if not "mode" in params or params["mode"] == "help":
        help()

    if params["mode"] == "status":
        if 'hostname' in params:
            print("Checking host status...")
            status = is_alive_host(params["hostname"])
            print("{} {} alive".format(params["hostname"], "is" if status else "isn't"))
        else:
            print("Not specifide hostname")
            help()
    elif params["mode"] == "app":
        print("Not done yet")
    else:
        print("Unknown mode: {}".format(params["mode"]))
        help()
