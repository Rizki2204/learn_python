import requests as r
url = "https://api.github.com/users/octocat"
target = r.get(url)
if target.ok:
    informasi = target.json()
    print(f"informasi login: {informasi.get("login")}, informasi nama: {informasi.get("name")}, informasi followers: {informasi.get("followers")}, informasi repository public: {informasi.get("public_repos")}")