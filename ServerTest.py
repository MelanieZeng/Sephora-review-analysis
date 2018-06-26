#test
def get_one_page(url):
	response = requests.get(url)
	if response.status_code == 200:
		return response.text
	return None

def main():
	url = 'https://www.consumeraffairs.com/cosmetics/sephora.html'
	html = get_one_page(url)
	print(html)

main()
