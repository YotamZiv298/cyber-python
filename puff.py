import sys

try:
    url = sys.argv[1]
    url = url.split('/')
    if "http" in url[0]:
        url = url[3:]
    else:
        url = url[1:]
    print(*url)
except Exception:
    print("Invalid input")
