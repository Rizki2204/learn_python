import requests as r
url = "https://api.github.com/"
respon = r.get(url)
content_type = respon.headers.get("content-type")
print(f"Status code: {respon.status_code}, reason: {respon.reason}, OK: {respon.ok}, URL: {respon.url}, Elapsed: {respon.elapsed}, Content-Type: {content_type}")
if respon.ok == True :
    print("Requests Successfully")
else:
    print("Requests Failed")    


