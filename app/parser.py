from bs4 import BeautifulSoup
import requests
import requests
from requests.utils import get_environ_proxies


def parse_html(url):
    try:
        print("当前环境代理设置：", get_environ_proxies("http://example.com"))
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
            'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }
        
        response = requests.get(url,headers=headers, timeout=5)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'lxml')
        
        title = soup.title.string if soup.title else 'No title found'
        price = None
        
        # Example: Look for common price patterns
        price_tags = soup.find('p', id='dd-price')
        if price_tags:
            price = price_tags.text.strip()
        if price and price.startswith('¥'):
            price = price[1:]
    
        return {
            'title': title,
            'price': price
        }
    except requests.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return None
    except Exception as e:
        print(f"Error parsing the HTML: {e}")
        return None