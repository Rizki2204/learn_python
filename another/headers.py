import requests as r
#buat dictionary berisi:
#"User-Agent" → "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/124.0"
#"Accept" → "application/json"
headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/124.0",
    "Accept" : "application/json"
}
#Kirim GET ke "https://httpbin.org/headers" dengan headers=headers.
response = r.get("https://httpbin.org/headers", headers = headers)
#Jika resp.ok, parse resp.json() dan tampilkan:
#User-Agent yang diterima server (hasil["headers"]["User-Agent"])
#Accept yang diterima server (hasil["headers"]["Accept"])
if response.ok:
    hasil = response.json()
    print("User-Agent: ", hasil["headers"]["User-Agent"])
    print("Accept: ", hasil["headers"]["Accept"])
#Jika gagal, tampilkan status code.
else:
    print(response.status_code)