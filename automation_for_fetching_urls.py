import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin

def get_domain_links(domain):
    try:
        response = requests.get(domain)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            
            links = soup.find_all('a', href=True)
            
            domain_links = set()
            parsed_domain = urlparse(domain)
            base_url = f"{parsed_domain.scheme}://{parsed_domain.netloc}"
            
            for link in links:
                href = link['href']
                parsed_href = urlparse(href)
                if parsed_href.netloc == parsed_domain.netloc or not parsed_href.netloc:
                    full_url = urljoin(base_url, href)
                    domain_links.add(full_url)
            
            return domain_links
        else:
            print(f"Failed to fetch {domain}. Status code: {response.status_code}")
    except requests.RequestException as e:
        print(f"An error occurred: {e}")

domain = "https://google.com"  
links = get_domain_links(domain)
if links:
    print(f"All links from {domain}:")
    for link in links:
        print(link)
