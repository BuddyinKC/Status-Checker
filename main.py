import requests
 
sites = [
    {"name": "Library Website", "url": "https://library.umkc.edu"},
    {"name": "Digital Collections (Islandora)", "url": "https://digital.library.umkc.edu"},
    {"name": "Digital Exhibits (Omeka S)", "url": "https://exhibits.library.umkc.edu"},
    {"name": "FOLIO", "url": "https://umsystem.folio.ebsco.com/"},
]

website_name = [
    "",
    "",
    "",
    "",
]

website_url = [
    "https://library.umkc.edu", 
    "https://digital.library.umkc.edu", 
    "https://exhibits.library.umkc.edu",
    "https://umsystem.folio.ebsco.com/", 
]
 
statuses = {
    200: "Website Available",
    301: "Permanent Redirect",
    302: "Temporary Redirect",
    404: "Not Found",
    500: "Internal Server Error",
    503: "Service Unavailable"
}
 
columns = ["Name", "URL", "Response"]

table_head = f"<thead>\n<tr><th>{'</th><th>'.join(columns)}</th></tr>\n</thead>"
table_body = "\n<tbody>\n"

for site in website_url:
    try:
        web_response = requests.get(site)
        print(site, statuses[web_response.status_code])
        site_data = ["NAME", f"{site}", f"{statuses[web_response.status_code]}"]
        table_body += f"<tr><td>{'</td><td>'.join(site_data)}</td></tr>\n"
 
    except:
        print("NAME", site, statuses[web_response.status_code])

table_body += "</tbody>\n"

print(f"<table>\n{table_head}{table_body}</table>")        
