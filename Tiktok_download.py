import pyktok as pyk

# Specify the browser to use
pyk.specify_browser('chrome')

# List of URLs to download
urls = """
Paste your urls to download onto here
"""

# Convert the string of URLs into a list
def convert_to_list(string):
    return list(string.strip().split("\n"))

urls_list = convert_to_list(urls)

# Loop through each URL and download
for url in urls_list:
    pyk.save_tiktok(url, True, 'video_data.csv', 'chrome')
