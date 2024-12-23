from bs4 import BeautifulSoup
import requests
import sys

def get_pdf_links(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    links = soup.find_all('a', href=True)
    
    for link in links:
        uri = link.get('href')
        #print(uri)
        
        if uri:
            if not uri.startswith('http'):
                uri = f'{url}/{uri}'
            #print(uri)

        try:
            
            r = requests.get(uri, timeout=120)
            r.raise_for_status()
        
            if r.headers['Content-Type'] == 'application/pdf':
                content_length = r.headers.get('Content-Length')
    
                print(f'URI: {uri}')
                print(f'Final URI: {r.url}')
                print(f'Content Length: {content_length} bytes')
    
        except requests.exceptions.HTTPError as e:
            print(f'HTTP Error: {e.response.status_code} for URL: {uri}')

        except requests.exceptions.Timeout as e:
            print(f'Timeout Error: The request for {uri} took longer than 2 minutes')

        except requests.exceptions.ConnectionError:
            print(f'Connection Error: Failed to connect to {uri}')

        except Exception as e:
            print(f'An unexpected error occurred for {uri}: {e}')

if __name__ == "__main__":
    url = sys.argv[1]
    get_pdf_links(url)
