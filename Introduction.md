#This will server as the place holder on how to effectively use the tool.

# Introduction #

Pinata was developed to assist with the explanation of the Cross Site Request Forgery and how a vulnerable application can be exploited - this is often useful when you are trying to explain to the client that their application is vulnerable to this particular class of vulnerability and of course this was in response to a considerable number of developers not understanding what and how their application can be exploited.

Once a tester identifies a function as vulnerable, she can use this tool to create a proof of concept HTML, perhaps modify it and play it against the vulnerable system to confirm the vulnerability. It also helps in identification of ineffective CSRF protection where by the application uses the same CSRF token for different sessions or does not invalidate previous CSRF tokens.

To effectively use the tool one should know what and how Cross Site Request Forgery works. You can find my detail write up CSRF on the project Home page under my blog. You should also have access to a proxy tool. Burp, Paros, Webscarb, any proxy will do, as long as you can capture the raw HTTP request. Also you should have access to the application you are testing and of couse you must have explicit permission from the owner of the application to test it.

One might ask; how an attacker can possibly access a vulnerable application. There are so many applications both free and paid that any up can access, either free or a little fee(These are your SAAS type applications), multiple tenants using the same application with pretty much the same application structure for all clients.


# Details #

I will add detail Tutorial on how to use the tool shortly.