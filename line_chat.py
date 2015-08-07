from line import LineClient, LineGroup, LineContact
 
USERNAME = 'saintzst@hotmail.com'
PASSWORD = 'saintzreddevil02'
GROUPNAME = 'BOT_TEST'
MSG = 'hello world!'
 
#optional
COMPUTERNAME = 'SAINTZST'
TOKEN = ''
 
try:
  client = LineClient(id=USERNAME, password=PASSWORD, authToken=TOKEN, com_name=COMPUTERNAME)
  #client = LineClient(authToken="DTsnf1HdqqACOML7Sjoc.p34PPUdKIMd6GLNlSNei7a.nPPxT3BKGmH/3NK2S6FYn7ODEn64sDKUvsSBN3F3pVc=")
  """
  TOKEN = client.authToken
  print "TOKEN : %s\r\n" % TOKEN
 
  client_group = client.getGroupByName(GROUPNAME)
  recent_group_msg = client_group.getRecentMessages(count=10)
  print "RecentMessages : %s\r\n" % recent_group_msg
 
  client_group.sendMessage(MSG)
  """
 
except:
    print "Login Failed"

print client.authToken
print client.contacts
#findAndAddContactByUserid(Uengpaporn)
#c=client.getContactByName("! Ball !")
#c.sendMessage("Hi , Ball")
#c.sendSticker()
#friend=client.groups[1]
#friend.sendSticker()
#c.sendImageWithURL("https://fbcdn-sphotos-c-a.akamaihd.net/hphotos-ak-xfa1/v/t1.0-9/11162205_887784064616050_6516449533241024034_n.jpg?oh=eaa23746515d25dfe712fe6a3fc2f2e5&oe=55F78444&__gda__=1445876594_704ae9b84269a168effd531952ee6bd3")

'''
friend=client.contacts
print friend
'''