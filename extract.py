import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def extract_all_urls(url):
    try:
        # Fetch the HTML content
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find all links and extract URLs
        links = soup.find_all('a')
        if not links:
            print("No links found on the page.")
            return []

        all_urls = []
        for link in links:
            if 'href' in link.attrs:
                full_url = urljoin(url, link['href'])
                all_urls.append(full_url)
            else:
                print(f"Link without href attribute: {link}")

        return all_urls

    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return []

def write_urls_to_file(urls, file_name):
    try:
        with open(file_name, 'w') as file:
            for url in urls:
                file.write(f"{url}\n")
        print(f"Extracted URLs have been written to {file_name}")
    except IOError as e:
        print(f"Error writing to file: {e}")

if __name__ == "__main__":
    page_url = 'https://example.com'  # Replace with the actual URL
    all_urls = extract_all_urls(page_url)
    
    if all_urls:
        file_name = 'urlsample.txt'
        write_urls_to_file(all_urls, file_name)
    else:
        print("No URLs found.")
