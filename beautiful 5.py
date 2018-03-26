import requests
from bs4 import BeautifulSoup
url = "https://play.google.com/store/search?q=kids%20games&c=apps"
response = requests.get(url)
soup = BeautifulSoup(response.content,'html.parser')
#print soup.prettify()
#d = soup.findAll("a")
#print len(d)
#d = soup.findAll("div")
d = soup.findAll("div",{"class":"card no-rationale square-cover apps small"})
#print len(d)
#first_link = d[0]
#print type(first_link)
#print first_link.text

#titles = soup.findAll("a", {"class":"title"})
#subtitles=soup.findAll("a", {"class":"subtitle"})
#rating = soup.findAll("div",{"class":"tiny-star star-rating-non-editable-container"})
#print rating[0].get(("aria-label")
filename = "kids_games.csv"
f = open(filename, "w")
headers = "title,other_name,rating\n"
f.write(headers)
for first_link in d:
       try:
           titles1 = first_link.find_all("a", {"class": "title"})
           final_title = titles1[0].text.encode('ascii','ignore')
       except:
            pass
       try:
            subtitles1 = first_link.find_all("a", {"class": "subtitle"})
            final_subtitle = subtitles1[0].text.encode('ascii','ignore')
       except:
             pass
       try:
            rating = soup.findAll("div", {"class":"tiny-star star-rating-non-editable-container"})
            final_rating=rating[0].get("aria-label").encode('ascii','ignore')
       except:
           pass
       #print final_title
       #print final_subtitle
       #print final_rating

       print(final_title + "," + final_subtitle + "," + "," + final_rating + "\n")
       f.write(final_title + "," + final_subtitle + "," + "," + final_rating + "\n")
f.close()

















#subtitles = soup.findAll("a", {"class":"subtitle"})
#print len(subtitles)
#for link in subtitles:
    #print link.text
#print len(titles)
#ratings = soup.findAll("div",{"class":"tiny-star star-rating-non-editable-container"})
#for rating in ratings:
    #print rating.text
#print len(ratings)