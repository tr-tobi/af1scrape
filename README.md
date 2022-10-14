# Air Force 1 Webscraper
#### Video Demo:  <https://www.youtube.com/watch?v=RAmoCeCy8z4>
#### Description: When the user runs the application, they will be notified via email whenever the price of the shoes drop below £109.95. This check will happen every 10 minutes. Using beautifulsoup from the bs4 library I was able to get the html element that contained the price of the product and from that i was able to write functions to carry out the email using the smtplib for google. I originally wanted to create a subscription site using flask where the user would enter their email and using the mailgun api i would sign them up to the mailing list and from there the price checks would occur, however I ran into some problems with flask. I will definately attempt to redo that project in the future. 

I created an AWS EC2 instance for this project so that I would be notified even if my computer is off.

![alt text](https://cdn.discordapp.com/attachments/727292252417949779/1030630008126967858/unknown.png)
