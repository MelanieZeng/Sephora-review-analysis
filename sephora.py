import requests
from bs4 import BeautifulSoup

#loop all pages
for page_num in range(7):
	r = requests.get('https://www.consumeraffairs.com/cosmetics/sephora.html?page=' + str(page_num))
	
	soup = BeautifulSoup(r.text, 'lxml')

	#find reviewIDs:
	reviewIDs = soup.find_all(class_='rvw js-rvw')
	for id in reviewIDs:
		print (id['data-id'])
	
	#find all ratings (need to filter out integer)
	rating = soup.find_all(class_='stars-rtg stars-rtg--sm')
	for a in rating:
		print (a['data-rating'])
    
    #find locations
	location = soup.find_all(class_='rvw-aut__inf-nm')
	for all in location:
		print (all.string)

	#find comments (need to get the second paragraph)
	comment = soup.find_all(class_='rvw-bd ca-txt-bd-2' or 'js-collapsed')
	for n in comment:
		print (n.p)

	#number of people found this review helpful
	helpful = soup.find_all(class_='rvw-foot__helpful-count js-helpful-count ca-txt--clr-gray')
	for h in helpful:
		print (h.strong)

