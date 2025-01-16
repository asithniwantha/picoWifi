import blink
import machine
from lib.ota_updater import OTAUpdater

def auto_start():
    blink.blink_led()

machine.Timer(-1).init(period=100, mode=machine.Timer.PERIODIC, callback=lambda t:auto_start())
print("Auto start enabled")

def download_and_install_update_if_available():
    ota_updater = OTAUpdater('url-to-your-github-project')
    ota_updater.download_and_install_update_if_available('wifi-ssid', 'wifi-password')

def start():
    print("Executing main.py")

def boot():
    download_and_install_update_if_available()
    start()


boot()