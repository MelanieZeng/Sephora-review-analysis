import requests
from bs4 import BeautifulSoup

#Loop all pages
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
        array_rating.append(a['data-rating'])

    #Find locations
    location = soup.find_all(class_='rvw-aut__inf-nm')
    for all in location:
        array_location.append(all.string)

    #Find comments (TODO: need to get the second paragraph)
    comment = soup.find_all(class_='rvw-bd ca-txt-bd-2' or 'js-collapsed')
    for n in comment:
        array_comment.append(n.p)

    #The number of people that found this review helpful
    helpful = soup.find_all(class_='rvw-foot__helpful-count js-helpful-count ca-txt--clr-gray')
    for h in helpful:
        array_helpful.append(h.strong)

    #Data printer
    datafile = open ("data.txt", 'a', encoding="utf-8")   
    for iterator in range(len(array_reviewID)):
        datafile.write ('Rating ID: ' + array_reviewID[iterator] + '\n' + 'Rating Score: ' + array_rating[iterator] + '\n' + 'Name and Location: ' + array_location[iterator] + '\n' + 'Comment: ' + str(array_comment[iterator]) + '\n' + str(array_helpful[iterator]) + ' people found this review helpful. \n \n')
    datafile.close()

    
