# code for transferring files from the Pi to SRCF server

from fabric import Connection


def upload_data(data_location, host="shell.srcf.net", user="cnsw2"):
    with Connection(host=host, user=user) as c:
        c.put(data_location, "Raspberry_Pi/Temp_Humidity_Data")
