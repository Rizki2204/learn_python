import requests as r
url = "https://api.github.com/search/repositories"
permintaan = {
    "q" : "robotic",
    "per_page" : 5
}
respon = r.get(url, params = permintaan)
if respon.ok:
    data = respon.json()
    print(data["total_count"])
    print(len(data["items"]))
    for repo in data["items"]:
        print(repo["full_name"])
        print(repo["stargazers_count"])
else:
    print(respon.status_code)
