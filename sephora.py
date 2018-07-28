import requests
from bs4 import BeautifulSoup
import csv 

csv_rows = []

#loop all pages
for page_num in range(7):
	r = requests.get('https://www.consumeraffairs.com/cosmetics/sephora.html?page=' + str(page_num))
	
	soup = BeautifulSoup(r.text, 'lxml')

	#Storage arrays
	array_reviewID = []
	array_rating = []
	array_location = []
	array_comment = []
	array_helpful = []

	#Find reviewIDs:
	reviewIDs = soup.find_all(class_='rvw js-rvw')
	for id in reviewIDs:
		array_reviewID.append(id['data-id'])
	
	#Find all ratings (need to filter out integer)
	rating = soup.find_all(class_='stars-rtg stars-rtg--sm')
	for a in rating:
		if a['data-rating'] not in ['1','2','3','4','5']:
			array_rating.append(a['data-rating'])
    
    #Find locations
	location = soup.find_all(class_='rvw-aut__inf-nm')
	for l in location:
		array_location.append(l.string)

	#Find comments
	comment = soup.find_all(class_='rvw-bd ca-txt-bd-2')
	hidden_comment = soup.find_all(class_='js-collapsed')
	for n in comment:
		if n.find(class_='js-collapsed')!=None: 
			result = n.p.text
			hidden_result = n.find(class_='js-collapsed').text
			final_result = result + hidden_result
			array_comment.append(final_result)
		else:
			array_comment.append(n.p.text)

	#Find how many people found the review helpful
	helpful = soup.find_all(class_='rvw-foot__helpful-count js-helpful-count ca-txt--clr-gray')
	for h in helpful:
		array_helpful.append(h.strong)

	#Data printer
	datafile = open('data.txt', 'a', encoding='utf-8')
	for iterator in range(len(array_reviewID)-1): #The -1 is to skip over the oldest review. For some reason, this review has no rating, unlike the others.  
		datafile.write ('Rating ID: ' + array_reviewID[iterator] + '\n' + 'Rating Score: ' + array_rating[iterator] + '\n' + 'Name and Location: ' + array_location[iterator] + '\n' + 'Comment: ' + str(array_comment[iterator]) + '\n' + str(array_helpful[iterator]) + ' people found this review helpful. \n \n')
	datafile.close()
	
	# setup CSV raw data
	for iterator in range(len(array_reviewID)-1): 
		csv_rows.append(
			(array_reviewID[iterator], 
			array_rating[iterator],
			array_location[iterator],
			str(array_comment[iterator]),
			str(array_helpful[iterator])
			))


	#Comment printer for nltk analysis
	commentfile = open('comment.txt', 'a', encoding='utf-8')
	commentfile.write(str(array_comment))
	commentfile.close()

# CSV ops
header = ['Rating ID', 'Rating Score', 'Name and Loc', 'Comment', 'Helpful']
with open('data.csv', 'w') as csvFile:
	writer = csv.writer(csvFile)
	writer.writerow(header)
	writer.writerows(csv_rows)