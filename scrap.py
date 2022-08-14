#requests are used to download the html file 

import requests

#bs4 uses the html and gathers the data
from bs4 import BeautifulSoup

#res is the response variable
res = requests.get('https://news.ycombinator.com')

# print(res) #<Response [200]>

# print(res.text) #rs.text to gather the html code

#to modify(parse) the html(res.text) and sets handler to call the functions

soup = BeautifulSoup(res.text,'html.parser')

# print(soup)
# print(soup.body) #to grab the body
# print(soup.body.contents) #to list 
# print(soup.find_all('a')) #prints all the tags with 'a'
# print(soup.find('a')) #prints the first tag with 'a'
# print(soup.find(id='score_20514755_')) #grabs all the id
#print(soup.select('.score')) #gathers all the classes with score
#print(soup.select('#score')) #gathers all the ids with score

#grab all the titles of the news
links = soup.select('.titlelink')
#grab all the subtexts of the titles of the news
subtext = soup.select('.subtext')


#function to sort all the news with the votes
def sort_stories_by_votes(hnlist):
    #lamba func to sort the list of dictionary when the key is votes
    return sorted(hnlist, key= lambda k:k['votes'],reverse =True)

#to print a formatted list of dictionaries
from pprint import PrettyPrinter
pprinter=PrettyPrinter()

#function to return a list of dictionary with the title , links & votes where the news has a vote > 99
def create_custom_hn(links,subtext):
    
    hn=[]
    
    for idx,item in enumerate(links):                                                            #links[idx]=item
        
        title = item.getText()                                                                   #grabs titles text
        href = item.get('href',None)                                                             #grabs links
        vote = subtext[idx].select('.score')                                                     #grabs the subtext                                                 
        if len(vote):
            
            points = int((vote[0].getText()).replace(' points',''))
        
            if points > 99:
                
                hn.append({'title':title,'links':href,'vote':points})
    
    return hn

print(pprinter.pformat(create_custom_hn(links,subtext)))
