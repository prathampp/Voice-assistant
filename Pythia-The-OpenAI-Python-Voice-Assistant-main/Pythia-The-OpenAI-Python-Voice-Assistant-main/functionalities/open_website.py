import webbrowser

def open_website(site_name):
    sites = {
        "youtube": "https://www.youtube.com",
        "wikipedia": "https://www.wikipedia.com",
        "google": "https://www.google.com",
        "LINKDIN":"https://www.linkedin.com"
    }
    if site_name.lower() in sites:
        webbrowser.open(sites[site_name.lower()])
        return f"Opening {site_name} Sir..."
    else:
        return f"Sorry, I can't open {site_name}."
# Checkd