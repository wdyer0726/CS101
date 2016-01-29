# Define a procedure, add_page_to_index,
# that takes three inputs:

#   - index
#   - url (String)
#   - content (String)

# It should update the index to include
# all of the word occurences found in the
# page content by adding the url to the
# word's associated url list.

index = []


def add_to_index(index,keyword,url):
    for entry in index:
        if entry[0] == keyword:
            entry[1].append(url)
            return
    index.append([keyword,[url]])
    
def lookup(index,keyword):
    for entry in index:
        if entry[0] == keyword:
            return entry[1]        
    return []

def add_page_to_index(index,url,content):
    words = content.split()
    for word in words:
        add_to_index(index, word, url)
        
    
    
add_page_to_index(index,'fake.text',"This is a test")
add_page_to_index(index,'real.text',"This is not a test")
add_page_to_index(index, 'abelincoln.text', """Better to remain silent and be thought a fool than 
                                                to speak out and remove all doubt.
                                                      Abraham Lincoln """

print index
print lookup (index, 'a')
print lookup (index, 'all')


