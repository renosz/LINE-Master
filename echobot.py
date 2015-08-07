import re
import urllib2
from line import LineClient, LineGroup, LineContact

try:
    client = LineClient("saintzst@hotmail.com", "saintzreddevil02")
    #client = LineClient(authToken="AUTHTOKEN")
except:
    print "Login Failed"

while True:
    op_list = []

    for op in client.longPoll():
        op_list.append(op)

    for op in op_list:
        sender   = op[0]
        receiver = op[1]
        message  = op[2]
        
        msg = message.text
        url=re.findall(r"(http://.+)",msg)[0]
        if url:
            req=urllib2.urlopen(url).read()
            title = re.findall(r'<title>(.+?)<\/title>',req)[0]
            receiver.sendMessage("[title] %s" % (str(title)))
        else:
            pass
        
        if msg == None:
        	msg="Sticker"
        	receiver.sendMessage("[%s] %s" % (sender.name, msg))
        else:
        	receiver.sendMessage("[%s] %s" % (sender.name, msg))