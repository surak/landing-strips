import stackprinter
from dotenv import load_dotenv
import os
import requests

stackprinter.set_excepthook(style="darkbg2")
output_dir = "images"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)


def main():
    load_dotenv()
    gmaps_api_key = os.getenv("GOOGLE_MAPS_API_KEY")
    get_map(gmaps_api_key, "38.8977,-77.0365")


def get_map(key, coords=None):
    # Construct the URL for the satellite image
    url = f"https://maps.googleapis.com/maps/api/staticmap?center={coords}&zoom=17&size=640x640&maptype=satellite&key={key}"
    # Retrieve the image data
    response = requests.get(url)
    print(url)
    # Save the image to a file
    with open(f"{output_dir}/{coords}.png", "wb") as f:
        f.write(response.content)


if __name__ == "__main__":
    main()
