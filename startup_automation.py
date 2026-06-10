import webbrowser
import time
import subprocess


# Time to wait after Windows login
STARTUP_DELAY = 20

# Links to open in the default browser
LINKS = [
    "https://www.google.com",
    "https://your-email-provider.com"
]


def open_links():
    """Open configured links in the default browser."""
    print("Opening links...")

    for link in LINKS:
        webbrowser.open(link)
        time.sleep(1)


def open_whatsapp():
    """Open WhatsApp Desktop on Windows."""
    print("Opening WhatsApp...")

    try:
        subprocess.run("start whatsapp:", shell=True)
        print("WhatsApp opened successfully.")
    except Exception as error:
        print(f"Could not open WhatsApp: {error}")


def main():
    print("Starting Windows startup automation...")

    print("Waiting for Windows to finish loading...")
    time.sleep(STARTUP_DELAY)

    open_links()
    open_whatsapp()

    print("Startup routine completed.")


if __name__ == "__main__":
    main()
