## **Overview:** ##

-WARNING - THIS IS NOT A POINT AND CLICK TOOL. YOU SHOULD KNOW WHAT YOU ARE DOING TO USE THIS TOOL.

- The tool will generate proof of concept CSRF HTML given an HTTP request. It will automatically check whether it is a GET or a POST request and with further validation for standard POST and Multipart/form POST.

- The tool will then create an HTML corresponding to the type of the request.

- The GET CSRF HTML includes IMG tag with SRC set to the URL being tested.

- The POST CSRF HTML is created with auto submit java script form with names and values from the HTTP request.


## **Working:** ##

**Pinata - Version 0.93 Out Now.**

- Download pinata.zip from the downloads.

- It is Python based tool. Needs Python installed – I have developed it on Python 2.6. But it should work with Python 2.7.

- The tool consists of three files, piñata.py, markup.py and CSRFBody.txt.

- To install it create a new directory like C:\Pinata and copy all three files to it.

- Piñata.py is the main file and should be run to generate the HTML.

- Markup.py is called by piñata.py to generate HTML, I did not develop it and do not take any credit for it - however I would like to thank the developer, it made much easier to write this tool.

- CSRFBody.txt holds the HTTP request.

- To use the tool go to a vulnerable page, create a request, capturing the HTTP request in the proxy. Copy this request and paste it in CSRFBody.txt, saving and closing CSRFBody.txt

- Run the tool by going to command line and typing C:\Pinata\pinata.py

- It should generate the HTML file in C:\Pinata\

Demonstration can be found here on my blog.

http://secmir.blogspot.com/2010/05/csrf-demo-video.html


## **Future Directions:** ##

- I look forward to your suggestions.

- Perhaps some features to beat referer header based CSRF protection.

- This is essentially a hack so I will work towards cleaning up the current code.


## **Questions:** ##

- Let me know if you have any questions or it suddenly stops working for you.

ahsanmir (at)gmail (dot) com