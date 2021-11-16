import requests
from bs4 import BeautifulSoup

url = "https://free-proxy-list.net/"  # proxy providing website
req = requests.get(url)
print(f"RESPONSE FROM WEBSITE {req}")

soup = BeautifulSoup(req.text, "html.parser")
table = soup.find("table")
all_rows = table.find_all("tr")


def getip(n):
    tr = table.find_all('tr')[n]
    ip = tr.find_all("td")[0].get_text()
    port = tr.find_all("td")[1].get_text()
    return f"{ip}:{port}"


txt = ""
for i in range(101):
    # print("finding")
    if i == 0:
        continue
    if i == 1:
        txt = txt + f"{getip(i)}"
    else:
        txt = txt + f"\n{getip(i)}"

print("text file is written")

with open("proxy.txt", "w+") as f:
    f.write(txt)
    # print("following code is written")

with open("proxy.txt", "r") as t:
    text = t.read()
    # print(f"\n\n\n\n###############\n{text}\n##################\n\n\n\n")
    ans = text.split("\n")

print(f"WE HAVE ADDED {len(ans)} PROXIES TO PROXIES.TXT")
