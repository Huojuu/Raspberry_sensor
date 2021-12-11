import ftplib
import Adafruit_DHT as dht
from time import sleep

DHT_SENSOR = dht.DHT22
DHT_PIN=4
path = "DHT22_data.txt"

while True:
        humidity, temperature = dht.read_retry(DHT_SENSOR, DHT_PIN)
        if humidity is not None and temperature is not None:
            print("Temp={0:0.1f}*C Humidity={1:0.1f}%".format(temperature, humidity))
            file = open(path,"w")
            file.write("Lämpötila: {0:0.1f} °C  Ilmankosteus: {1:0.1f} %".format(temperature,humidity))

        else:
            print("Failed to retrieve data from humidity sensor")
        file.close()


        ftp = ftplib.FTP("HOST")
        user = "username"
        password = "password"
        ftp.login(user, password)
        file = open('DHT22_data.txt','rb')
        ftp.storbinary("STOR DHT22_data.txt", file)
        file.close
        print("File uploaded to server")
        ftp.quit()
        sleep(5)

