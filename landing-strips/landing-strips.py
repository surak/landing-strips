import stackprinter
from dotenv import load_dotenv
import os


stackprinter.set_excepthook(style="darkbg2")


def main():
    load_dotenv()
    gmaps_api_key = os.getenv("GOOGLE_MAPS_API_KEY")
    print("Api key:", gmaps_api_key)


if __name__ == "__main__":
    main()
