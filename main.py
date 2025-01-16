import machine
import time
import network
import gc
from lib.ota_updater import OTAUpdater

# Configuration (REPLACE THESE WITH YOUR VALUES)
WIFI_SSID = "linksys"
WIFI_PASSWORD = "asith1234567890"
# REPO_URL = f"https://raw.githubusercontent.com/{GITHUB_USER}/{GITHUB_REPO}/main/{PROJECT_NAME}"
REPO_URL = "https://github.com/asithniwantha/picoWifi"

# Initialize onboard LED (adjust pin if needed for your board)
led = machine.Pin("LED", machine.Pin.OUT)

def connect_wifi():
    """Connects to Wi-Fi."""
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('Connecting to WiFi...')
        wlan.connect(WIFI_SSID, WIFI_PASSWORD)
        while not wlan.isconnected():
            time.sleep(1)
            print(".")
    print('WiFi connected')
    print('Network config:', wlan.ifconfig())
    return wlan

def check_for_updates():
    """Checks for and performs OTA update if available."""
    try:
        wlan = connect_wifi()
        ota_updater = OTAUpdater(REPO_URL)

        if ota_updater.check_for_update_to_install_during_next_reboot():
            print("New version found. Will install on next reboot.")
            machine.reset() # Reset to trigger the update on next boot
        else:
            print("No new version available.")
        wlan.disconnect()

    except Exception as e:
        print(f"Update check failed: {e}")
        return False # Indicate failure

    return True # Indicate success

def main():
    """Main application loop (blinking LED)."""
    print("Starting main application...")
    while True:
        led.value(1)
        print("LED ON")
        time.sleep(0.1)  # Shortened blink delay for demonstration
        led.value(0)
        print("LED OFF")
        time.sleep(0.1)
        gc.collect()  # Important for memory management

if __name__ == "__main__":
    if check_for_updates(): # Check for updates and reboot if needed
        pass # If update is scheduled, it will reboot automatically
    else:
        main() # If no update, start the application