import requests

# res = requests.get(
#     "https://cloud-server-testing-production.up.railway.app/get",
# )
# print(res.json())

with requests.post(
    "https://cloud-server-testing-production.up.railway.app/sendQuery",
    json={"query": "write a poem"},
    stream=True,
) as response:
    for chunk in response.iter_content(chunk_size=1024):
        if chunk:
            print(chunk.decode("utf-8"), end="")
