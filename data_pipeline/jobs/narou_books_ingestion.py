import requests

url = "https://api.syosetu.com/novelapi/api/"

def fetch_novels(st: int):
    res = requests.get(
        url,
        params = { 
        "out": "json",
        "of": "t-n-w-gf-bg",
        "lim": 1,
        "order": "reviewcnt",
        "st": st
    })

    data = res.json()
    return data[1:][0]