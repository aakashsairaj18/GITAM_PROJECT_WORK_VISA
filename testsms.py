from twilio.rest import Client
SID='AC9592752068001375744cf3025bdb016d'
Auth_Token='9b5e9e3048b725695b78a4057500e4d7'
cl=Client(SID, Auth_Token)
cl.messages.create(body="Hi there this is team work visa", from_='+18316034486',to='+918340042805')
