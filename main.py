import blink
import machine
from lib.ota_updater import OTAUpdater

def auto_start():
    blink.blink_led()

machine.Timer(-1).init(period=10, mode=machine.Timer.PERIODIC, callback=lambda t:auto_start())
print("Auto start enabled")

ota_updater = OTAUpdater(github_repo='https://github.com/asithniwantha/picoWifi')

# WiFi credentials
ssid = 'linksys'
password = 'asith1234567890'

# Connect to WiFi and install update if available after boot
if ota_updater.install_update_if_available_after_boot(ssid, password):
    print("Update installed. Rebooting...")
    machine.reset()


