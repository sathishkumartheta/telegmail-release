#telegmail release version 2
# This software is provided as is
# No guarantee / warrantee

from telethon import TelegramClient, events
from telethon.tl.types import PeerChannel
import smtplib
from email.message import EmailMessage
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import os


YOUR_GOOGLE_EMAIL = ''
YOUR_GOOGLE_EMAIL_APP_PASSWORD = ''  # 16 characters eg : 'abcdabcdabcdabcd' details in readme.md
api_id = 12345678 # api id generated from gmail 
api_hash = '' # api hash generated from gmail
session_name="test"
chat = 'me'
private_channel_id=-1001234567890 # 13 digit number for the private telegram channel

smtpserver = smtplib.SMTP_SSL('smtp.gmail.com', 465)
smtpserver.ehlo()
while True:


    client = TelegramClient('anon2', api_id, api_hash)

    print('connected')
    print('waiting for new messages')
    try:
        @client.on(events.NewMessage(chats = [private_channel_id]))
        async def handler(event):
            print(event.date, ':', event.text)
            
            smtpserver = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            smtpserver.ehlo()
            smtpserver.login(YOUR_GOOGLE_EMAIL, YOUR_GOOGLE_EMAIL_APP_PASSWORD)

            msg=MIMEMultipart()
            msg['Subject'] = 'MOT'
            msg['From'] = YOUR_GOOGLE_EMAIL
            msg['To'] = YOUR_GOOGLE_EMAIL
            text = MIMEText(event.text)
        
            if(event.is_reply):
                rep=await event.get_reply_message()
                if rep is not None:
                    text=MIMEText( event.text +'  reply to:  ' + rep.text)
                    msg.attach(text)
            else:
                msg.attach(text)

            if(event.photo):
                path = await event.download_media(file="G:\\")
                print(path)
                with open(path, 'rb') as f:
                    img_data = f.read()
                image = MIMEImage(img_data, name=os.path.basename(path))
                msg.attach(image)
            
            smtpserver.sendmail(YOUR_GOOGLE_EMAIL, YOUR_GOOGLE_EMAIL, msg.as_string())
        client.start()
        client.run_until_disconnected()
        smtpserver.close()
    except Exception as e:
        print(e)


    
