import requests

# res = requests.get(
#     "https://cloud-server-testing-production.up.railway.app/get",
# )
# print(res.json())

res = requests.post(
    "https://cloud-server-testing-production.up.railway.app/sendQuery",
    json={"query": "Hello"},
)

print(res.json())
