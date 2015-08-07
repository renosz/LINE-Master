from line import LineClient, LineGroup, LineContact

try:
    client = LineClient("tachakorn.uengpaporn@gmail.com", "saintzreddevil02")
    #client = LineClient(authToken="DTnzOwlLSfbLPtz66pe9.qI9BodrXiZ9OzRQSu5ogwq.WJYnDTEskIgqGl1aEKlOlToGNalaOXNlIkil2B9wpmQ=")
except:
    print "Login Failed"

authToken = client.authToken
print authToken

#friend = client.contacts[1]
client.contacts[1].sendMessage("Hi , Saintz!!")
#friend.sendImageWithURL("https://scontent-sin1-1.xx.fbcdn.net/hphotos-xaf1/v/l/t1.0-9/1506925_783046351743291_1026843874667393485_n.jpg?oh=e354acd79a65e40717c5943418e3acd0&oe=55E85838")
print friend
