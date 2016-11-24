__author__ = 'gkannappan'

#This step would read the file and remove certain lines to make the input file look like one big html instead of
#multiple pages stitched together

rem_words = ['</html>', '<!DOCTYPE html>', '<html class="a-no-js" data-19ax5a9jf="dingo">', '<br/>']

with open('/Users/gkannappan/Documents/Intuit/Analytics Playground/Text Classification/AUTUMN/AMZN_Disc_One.txt') as oldfile, open('/Users/gkannappan/Documents/Intuit/Analytics Playground/Text Classification/AUTUMN/AMZN_Disc_Ref2.txt', 'a+') as newfile:
    print >> newfile, '<!DOCTYPE html>'
    print >> newfile, '<html class="a-no-js" data-19ax5a9jf="dingo">'
    for line in oldfile:
        if not any(rem_word in line for rem_word in rem_words):
            newfile.write(line)
    print >> newfile, '</html>'
