# telegmail
Automatically forwards messages from private telegram channel to given gmail id

Libraries required:

1) python version 3.9 or higher
2) telethon (pip install telethon)
3) smtplib

You need a few things to set up this program

1) A telegram mobile number. And you must also be a member of the private telegram channel from which you want messages to be forwarded
2) You need a telegram API id and API hash both of which can be obtained by registering in the link below
   https://core.telegram.org/api/obtaining_api_id
3) You need to know the channel ID of the private telegram channel. This can be obtained if you open the url of the channel on telegram web.
   Its a thirteen digit negative number eg : -1001011021034
4) You need to enable two factor authentication in your gmail account. This can be done here
   https://support.google.com/accounts/answer/185839?hl=en&co=GENIE.Platform%3DDesktop
5) You need to  enable passwords and get an app password from your gmail account
   https://support.google.com/accounts/answer/185833?hl=en

Once these things are setup, you are good to go with the program

Few points about the application:
1) For running the program the first time, you will be prompted for telegram number : +91XXXXXXXXXX and the code you will receive on your telegram
2) This program is event based. It doesnt forward old data.. From the moment you run the program, all the messages that are sent on the telegram channel from that moment will be forwarded to gmail.
3) This program forwards images too

Please understand that this program is a work in progress. Few features i wish to add
1) Exception handling
2) A nice gui
3) Ability to send all media

Thanks for reading !

1) If you like this application
2) If you want any features added to this application
3) If you want to contribute to this application
4) If you have requirements for a similar application

For any of the above, please mail me at sathishkumartheta@gmail.com
