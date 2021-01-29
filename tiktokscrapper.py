from TikTokApi import TikTokApi
import os

os.system("Title TikTok Username Scraper @socialmediaboosterlb")
api = TikTokApi.get_instance()
 
def scrapUsername(results,keyword):
    a= api.search_for_users(keyword,count=results)
    s = str(a).split("{'user")
    with open('my_dump.txt', 'a+',encoding='utf-8') as f:
        filtered = ""
        for users in s:
            splitter = users.split(", '")
            counter =0
            for spliti in splitter:
                if spliti.startswith("uniqueId") or spliti.startswith("followerCount"):
                    counter= counter+1
                    filtered= filtered + spliti
                    if counter == 2:
                        fileted = filtered +("\n ")
        filtered = filtered.replace("uniqueId': '","\n")
        filtered = filtered.replace("'followerCount':","")
        f.write(filtered)


print("""
  _______ _ _ _______    _      _    _                                             _____                                
 |__   __(_) |__   __|  | |    | |  | |                                           / ____|                               
    | |   _| | __ | ___ | | __ | |  | |___  ___ _ __ _ __   __ _ _ __ ___   ___  | (___   ___ _ __ __ _ _ __   ___ _ __ 
    | |  | | |/ / |/ _ \| |/ / | |  | / __|/ _ \ '__| '_ \ / _` | '_ ` _ \ / _ \  \___ \ / __| '__/ _` | '_ \ / _ \ '__|
    | |  | |   <| | (_) |   <  | |__| \__ \  __/ |  | | | | (_| | | | | | |  __/  ____) | (__| | | (_| | |_) |  __/ |   
    |_|  |_|_|\_\_|\___/|_|\_\  \____/|___/\___|_|  |_| |_|\__,_|_| |_| |_|\___| |_____/ \___|_|  \__,_| .__/ \___|_|   
                                                                                                       | |              
                 CREDITS INSTAGRAM: socialmediaboosterlb TELEGRAM: socialmediaboosterlb                |_|              
""")

results = int(input("how many usernames per keyword extracted?"))
with open('keywords.txt', 'r') as r:
    keywords = r.readlines()

for keyword in keywords:
    print("scraping...", keyword)
    scrapUsername(results,keyword)
    print("scraped...", keyword)