import MySQLdb
import wikipedia
def iset(name, summary):
##    db = MySQLdb.connect(host="localhost", # your host, usually localhost
##                     user="root", # your username
##                      passwd="", # your password
##                      db="wikipedia") # name of the data base
    db = MySQLdb.connect(host="localhost", # your host, usually localhost
                     user="root", # your username
                      passwd="", # your password
                      db="wikipedia") # name of the data base
    cur = db.cursor() 

    # Use all the SQL you like
    cur.execute("INSERT IGNORE INTO dump(Name, Summary) VALUES ('%s','%s')"%(name, summary))
    db.commit()
def pulll(name):
    summary = (wikipedia.summary(name, sentences=4))
    iset(name, summary)
def rando():
    name = wikipedia.random(pages=1)
    name = name.encode('utf-8', 'ignore')
    print name
    pulll(name)

#name = "Facebook"
#pulll(name)
i = 0
while i < 15:
    try:
        rando()
        #i = i+1
    except:
        pass
