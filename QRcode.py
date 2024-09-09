import qrcode
import sys
from PIL import Image

# Function to generate QR code with custom colors for a given URL
def generate_qr_code(url, filename, fill_color="black", back_color="white"):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color=fill_color, back_color=back_color)
    qr_img.save(filename)
    print(f"QR code generated for {url} and saved as {filename}")

# Main program
if __name__ == "__main__":
    # Mapping of services to URLs
    services = {
        "google": "https://www.google.com",
        "youtube": "https://www.youtube.com",
        "whatsapp": "https://web.whatsapp.com",
        "facebook": "https://www.facebook.com",
        "twitter": "https://www.twitter.com",
        "instagram": "https://www.instagram.com",
        "linkedin": "https://www.linkedin.com",
        "github": "https://github.com",
        "reddit": "https://www.reddit.com",
        "snapchat": "https://www.snapchat.com",
        "spotify": "https://www.spotify.com",
        "netflix": "https://www.netflix.com",
        "amazon": "https://www.amazon.com",
        "ebay": "https://www.ebay.com",
        "zoom": "https://www.zoom.us",
        "discord": "https://www.discord.com",
        "google drive": "https://drive.google.com",
        "apple app store": "https://www.apple.com/app-store/",
        "google play store": "https://play.google.com/store",
        # Add more services as needed
    }
    
    # Check if service name is provided as a command line argument
    if len(sys.argv) != 2:
        print("Usage: python generate_qr_code.py <service_name>")
        sys.exit(1)
    
    service_name = sys.argv[1].strip().lower()
    
    # Check if the service name is valid
    if service_name in services:
        filename = f"{service_name.replace(' ', '_')}_QR.png"
        generate_qr_code(services[service_name], filename)
    else:
        print("Service not supported or URL not recognized.")