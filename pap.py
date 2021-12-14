import requests

if __name__ == "__main__":
    r = requests.get('https://www.paprikaapp.com/api/v1/sync/groceries/', auth=('EMAIL', 'PASSWORD'))
    print(r.status_code)
    print(r.text)
