#imoport libraries
import urllib.request
from bs4 import BeautifulSoup


#specify the url
url = "http://jonesso.com/inmate-roster"

#query the site ans return html
page = urllib.request.urlopen(url)

#parse html
soup = BeautifulSoup(page, 'html.parser')

# find div and return value
inmate_roster = soup.find('div', attrs={'id': 'inmate_roster'})

inmates = inmate_roster.find_all('div', attrs={'class': 'inmate'})



for inmates in inmate_roster.find_all('div', attrs={'class': 'inmate'}):
   inmate_name = inmates.find('div', attrs={'class': 'inmate-name'}).text
   inmate_book_id = inmates.find('div', attrs={'class': 'inmate-booking-id'}).text
   inmate_book_date = inmates.find('div', attrs={'class': 'inmate-booking-date'}).text

print ("{} is in jail, his bookin number is {} and on this date {}".format(inmate_name, inmate_book_id, inmate_book_date))
