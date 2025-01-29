import requests
 
website_url = [
    "https://library.umkc.edu", 
    "https://digital.library.umkc.edu", 
    "https://exhibits.library.umkc.edu", 

]
 
statuses = {
    200: "Website Available",
    301: "Permanent Redirect",
    302: "Temporary Redirect",
    404: "Not Found",
    500: "Internal Server Error",
    503: "Service Unavailable"
}
 
for url in website_url:
    try:
        web_response = requests.get(url)
        print(url, statuses[web_response.status_code])
 
    except:
        print(url, statuses[web_response.status_code])