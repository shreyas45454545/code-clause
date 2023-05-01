import pyshorteners

link=input("Enter the Link:")

shortener=pyshorteners.Shortener()

shorted_link=shortener.tinyurl.short(link)

print(shorted_link)
