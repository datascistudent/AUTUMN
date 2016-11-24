__author__ = 'gkannappan'


from bs4 import BeautifulSoup
with open('/Users/gkannappan/Documents/Intuit/Analytics Playground/Text Classification/AUTUMN/AMZN_Disc_Ref2.txt') as oldfile, open('/Users/gkannappan/Documents/Intuit/Analytics Playground/Text Classification/AUTUMN/AMZN_Disc_new2.txt', 'a+') as newfile:
    soup = BeautifulSoup(oldfile, "lxml")
    #id3 = soup.find_all('i', {'class' : 'a-icon a-icon-text-separator'})
    #print id3
    #id3.extract()

    for tag in soup.find_all('i', {'class' : 'a-icon a-icon-text-separator'}):
        tag.replaceWith('')

    for tag in soup.find_all('i', {'class' : 'a-icon a-icon-star-medium a-star-medium-0 ratingstars'}):
        tag.replaceWith('')

    for tag in soup.find_all('a', {'class' : 'a-link-normal a-text-normal'}):
        tag.replaceWith('')

    for tag in soup.find_all('span', {'class' : 'averagecustomerreviews'}):
        tag.replaceWith('')

    #print soup.get_text()
    print  >> newfile, soup.prettify().encode('utf-8')
