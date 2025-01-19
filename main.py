from ota import OTAUpdater
from WIFI_CONFIG import SSID, PASSWORD
import blink
import time

firmware_url = "https://github.com/asithniwantha/picoWifi/"

ota_updater = OTAUpdater(SSID, PASSWORD, firmware_url, "main.py")

ota_updater.download_and_install_update_if_available()

while True:
    blink.blink_led()
    time.sleep(100) 