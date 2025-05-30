import requests

res = requests.post(
    "https://cloud-server-testing-production.up.railway.app/post",
    json={"TestKey": "Hello"},
)
print(res.json())
