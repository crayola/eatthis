import requests

if __name__ == "__main__":
    r = requests.get('https://www.paprikaapp.com/api/v1/sync/groceries/', auth=('timothee.carayol@gmail.com', 'dR2YpnbYvE5m'))
    print(r.status_code)
    print(r.text)
