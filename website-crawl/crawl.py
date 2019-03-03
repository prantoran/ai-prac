from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError
import re

isascii = lambda s: len(s) == len(s.encode())

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, dataval):
        if dataval not in self.stack:
            self.stack.append(dataval)
            return True
        return False
        
    def pop(self):
        if len(self.stack) <= 0:
            return ("No element in the Stack")
        return self.stack.pop()
    
    def empty(self):
        if len(self.stack) <= 0:
            return True
        return False
    
    def peek(self):     
	    return self.stack[0]


def getChildURLs(url):
    # print("getChildURLs url:", url)
    try:
        html = urlopen(url, timeout=20)
    except HTTPError as e:
        return None, e
    if html is None:
        print("URL is not found")
        return None, None
    try:
        hread = html.read()
        html.close()
        if hread == None:
            print("html read is None")
            return None, None
        
        bsObj = BeautifulSoup(
            hread, 
            features="html.parser", 
            from_encoding="iso-8859-1")

        urls = bsObj.find_all("a", href=True)
    except AttributeError as e:
        return None, e
    return urls, None



url_dict = {}

st = Stack()


rootURL = "http://www.northsouth.edu"
domainSTR = "northsouth.edu"

ignoreURLs = [
    "google.com",
    "youtube.com",
    "facebook.com",
    "twitter.com",
    "instagram.com",
    "linkedin.com",
    "turnitin.com",
    "www.aikbanka.rs",
    "sam.org.rs",
]

def ignoreURL(url = ""):
    
    if domainSTR not in url:
        return True
    
    for u in ignoreURLs:
        if u in url:
            return True

    
    return False






st.push(rootURL)

url_dict[rootURL] = True

err_mark = {}

while st.empty() == False:
    cURL = st.pop()
    print(cURL)

    if cURL.endswith(".pdf") or cURL.endswith(".jpg") or cURL.endswith(".png")  or cURL.endswith(".doc") or cURL.endswith(".docx"):
        url_dict[cURL] = False
        continue

    if ignoreURL(cURL):
        url_dict[cURL] = False
        continue

    # print("cURL:", cURL, " url_dict[cURL]:", url_dict[cURL])
    try:
        urls, err = getChildURLs(cURL)
    except Exception as e:
        print("children url get error:", e, " cURL:", cURL)
        url_dict[cURL] = False
        err_mark[cURL] = True
        continue


    if urls == None:
        # print("cURL:", cURL, ", no urls found")
        url_dict[cURL] = False
        continue
    elif err != None:
        print("cURL:", cURL, " err:", err)
        continue
    else:

        for a in urls:
            
            hrf = a['href'].strip()
            hrf = re.sub('\n', '', hrf)
            
            if isascii(hrf) == False:
                continue
            
            if hrf == "#" or hrf == "":
                continue
            
            if hrf.startswith("www") == False and hrf.startswith("http") == False:
                if domainSTR not in hrf:                    
                    if hrf.startswith("/"):
                        hrf = rootURL + hrf
                    else:
                        hrf = rootURL + "/" + hrf
            
            hrf = re.sub(r'\#\S+$', '', hrf)
            

            if hrf.endswith("/"):
                hrf = hrf[:-1]
            

            if hrf in url_dict:
                # print("\thrf:", hrf , " previously fnd")
                continue
            
            # print("\tsetting hrf:", hrf)
            
            
            url_dict[hrf] = True

            st.push(hrf)
            

output_list = []
output_urlnotfnd = []

for u in url_dict:
    if url_dict[u] == True:
        output_list.append(u)
    else:
        output_urlnotfnd.append(u)


# print("output_list:", output_list)

with open('output_list.txt', 'w') as f:
    for item in output_list:
        f.write("%s\n" % item)

with open('output_urlnotfnd.txt', 'w') as f:
    for item in output_urlnotfnd:
        f.write("%s\n" % item)

print("err_mark:", err_mark)