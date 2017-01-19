import webbrowser
import json
from urllib.request import urlopen

print("find old web site")
site = input("type url: ")
era = input("when (yyyymmdd): ")
url = "http://archive.org/wayback/available?url=%s&timestamp=%s" % (site, era)
response = urlopen(url)
contents = response.read()
text = contents.decode("utf-8")
data = json.loads(text)
try:
  old_site = data["archived_snapshots"]["closest"]["url"]
  print("found: ", old_site)
  print("check browser now")
  webbrowser.open(old_site)
except:
  print("sorry")
