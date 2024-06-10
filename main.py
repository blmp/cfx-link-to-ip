import sys
import requests

def getip(cfx_url):
    try:
        response = requests.get(cfx_url)
        if 'X-Citizenfx-Url' in response.headers:
            realip = response.headers['X-Citizenfx-Url']
            return realip
        else:
            print(f"Error: 'X-Citizenfx-Url' header not found in the response.")
            return None
    except requests.RequestException as e:
        print(f"Error: Could not get the URL. {e}")
        return None

def main(cfx_url):
    ip = getip(cfx_url)
    if ip:
        print(f"IP: {ip}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: python main.py <cfx.re_url>")
    else:
        cfx_url = sys.argv[1]
        main(cfx_url)
