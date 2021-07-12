import requests
from bs4 import BeautifulSoup
from bs4.element import Comment

url = 'https://www.josa.ngo/blog/78/blocking-clubhouse-in-jordan-a-quick-analysis-of-internet-censorship-methods-in-use'

def check_lang(lang):
    # check article language to decide average reading words per minutes
    global WPM
    if lang == 'en' :
         WPM = 228
    elif lang == 'ar':
         WPM = 138

def extract_url(url):
    # extract text from web page
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    check_lang(soup.html['lang'])
    text = soup.findAll(text = True)
    return text

def tag_visible(element):
    # check if the tag from head elements
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    # check if text is comment 
    if isinstance(element, Comment):
        return False
    # return true if it's neither a comment or header 
    return True

def number_of_words(visible_text): 
    # count the number of words in the text
    numberOfWords = 0
    # looping through visible text to count number of words
    for sentance in list(visible_text): 
        numberOfWords += len(sentance.split())   
    # return number of words 
    return numberOfWords 

def visible_text(TEXT):
    # check text visibility
    visibleText = filter(tag_visible, TEXT)
    # return visible text 
    return visibleText

def main (url):
    # control the process of the program 
    global WPM
    WPM = 175
    text = extract_url(url)
    visibleText = visible_text(text)
    numberOfWords = number_of_words(visibleText)
    readingTime = round(numberOfWords/WPM)
    print(readingTime, 'mins')

main(url)
