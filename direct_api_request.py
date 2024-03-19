from datetime import datetime
import requests

now = datetime.now()
timestamp = datetime.timestamp(now)

# payload = [
# {
#     "domain": ".instagram.com",
#     "expirationDate": 1725116029.854257,
#     "hostOnly": False,
#     "httpOnly": False,
#     "name": "csrftoken",
#     "path": "/",
#     "sameSite": "unspecified",
#     "secure": True,
#     "session": False,
#     "storeId": "0",
#     "value": "PHuVAz4SA4tUE8wCI4Qil9bt9plqd63x",
#     "id": 1
# },
# {
#     "domain": ".instagram.com",
#     "expirationDate": 1723657027.899564,
#     "hostOnly": False,
#     "httpOnly": True,
#     "name": "datr",
#     "path": "/",
#     "sameSite": "no_restriction",
#     "secure": True,
#     "session": False,
#     "storeId": "0",
#     "value": "Q53PZcnqxxU4Bbdq8xncNPyP",
#     "id": 2
# },
# {
#     "domain": ".instagram.com",
#     "expirationDate": 1709840476,
#     "hostOnly": False,
#     "httpOnly": False,
#     "name": "dpr",
#     "path": "/",
#     "sameSite": "no_restriction",
#     "secure": True,
#     "session": False,
#     "storeId": "0",
#     "value": "2",
#     "id": 3
# },
# {
#     "domain": ".instagram.com",
#     "expirationDate": 1717340029.854519,
#     "hostOnly": False,
#     "httpOnly": False,
#     "name": "ds_user_id",
#     "path": "/",
#     "sameSite": "unspecified",
#     "secure": True,
#     "session": False,
#     "storeId": "0",
#     "value": "61893573893",
#     "id": 4
# },
# {
#     "domain": ".instagram.com",
#     "expirationDate": 1709837239,
#     "hostOnly": False,
#     "httpOnly": False,
#     "name": "locale",
#     "path": "/",
#     "sameSite": "unspecified",
#     "secure": True,
#     "session": False,
#     "storeId": "0",
#     "value": "en_US",
#     "id": 5
# },
# {
#     "domain": ".instagram.com",
#     "expirationDate": 1723657027.906824,
#     "hostOnly": False,
#     "httpOnly": False,
#     "name": "mid",
#     "path": "/",
#     "sameSite": "unspecified",
#     "secure": True,
#     "session": False,
#     "storeId": "0",
#     "value": "Zc-dQwAEAAECKhUw1OipH8ltuN5J",
#     "id": 6
# },
# {
#     "domain": ".instagram.com",
#     "expirationDate": 1723657029.479855,
#     "hostOnly": False,
#     "httpOnly": True,
#     "name": "ps_l",
#     "path": "/",
#     "sameSite": "lax",
#     "secure": True,
#     "session": False,
#     "storeId": "0",
#     "value": "0",
#     "id": 7
# },
# {
#     "domain": ".instagram.com",
#     "expirationDate": 1723657029.479945,
#     "hostOnly": False,
#     "httpOnly": True,
#     "name": "ps_n",
#     "path": "/",
#     "sameSite": "no_restriction",
#     "secure": True,
#     "session": False,
#     "storeId": "0",
#     "value": "0",
#     "id": 8
# },
# {
#     "domain": ".instagram.com",
#     "hostOnly": False,
#     "httpOnly": True,
#     "name": "rur",
#     "path": "/",
#     "sameSite": "lax",
#     "secure": True,
#     "session": True,
#     "storeId": "0",
#     "value": "\"NCG\\05461893573893\\0541741100029:01f7a9c69dd544733f53ef7ff1c15c3ec1ad93fa799e8d65fb74dbfe83b1eaca5deff5b8\"",
#     "id": 9
# },
# {
#     "domain": ".instagram.com",
#     "expirationDate": 1725114516.557313,
#     "hostOnly": False,
#     "httpOnly": True,
#     "name": "sessionid",
#     "path": "/",
#     "sameSite": "unspecified",
#     "secure": True,
#     "session": False,
#     "storeId": "0",
#     "value": "61893573893%3AsOzoTUnKBI2Ptx%3A12%3AAYeSW4XTCRAB5tLFvWabKTUh-Qqx3Xjb18ox5ygGSw",
#     "id": 10
# },
# {
#     "domain": ".instagram.com",
#     "expirationDate": 1710163053.395025,
#     "hostOnly": False,
#     "httpOnly": True,
#     "name": "shbid",
#     "path": "/",
#     "sameSite": "unspecified",
#     "secure": True,
#     "session": False,
#     "storeId": "0",
#     "value": "\"7180\\05443691118949\\0541741094253:01f73bbf8aa3c82e09f0c2026f80f2dfcc75f150010e3f5ae75384cae94a04f669d50a91\"",
#     "id": 11
# },
# {
#     "domain": ".instagram.com",
#     "expirationDate": 1710163053.395102,
#     "hostOnly": False,
#     "httpOnly": True,
#     "name": "shbts",
#     "path": "/",
#     "sameSite": "unspecified",
#     "secure": True,
#     "session": False,
#     "storeId": "0",
#     "value": "\"1709558253\\05443691118949\\0541741094253:01f793ad18dec402df270119e2b11e81ee601177b07dce1a44655ff3f4215bceb6841a1e\"",
#     "id": 12
# },
# {
#     "domain": "www.instagram.com",
#     "expirationDate": 1710167179.500599,
#     "hostOnly": True,
#     "httpOnly": False,
#     "name": "ig_did",
#     "path": "/",
#     "sameSite": "unspecified",
#     "secure": True,
#     "session": False,
#     "storeId": "0",
#     "value": "0C826C21-17C3-444A-ABB7-EBABD37214D7",
#     "id": 13
# }
# ]

payload = {
    "domain": ".instagram.com",
    "expirationDate": 1725114516.557313,
    "hostOnly": False,
    "httpOnly": True,
    "name": "sessionid",
    "path": "/",
    "sameSite": "unspecified",
    "secure": True,
    "session": False,
    "storeId": "0",
    "value": "61893573893%3AsOzoTUnKBI2Ptx%3A12%3AAYeSW4XTCRAB5tLFvWabKTUh-Qqx3Xjb18ox5ygGSw",
    "id": 10
}

proxies = {
    'http': 'brd-customer-hl_62d2102f-zone-residential:r882rza32olo@brd.superproxy.io:22225'
}

response = requests.get("https://www.instagram.com/graphql/query/?query_id=17852405266163336&variables=%7B%22id%22%3A%22<graphql.user.id>%22%2C%22first%22%3A12%2C%22after%22%3A%22<graphql.user.edge_owner_to_timeline.page_info.end_cursor>%22%7D", proxies=proxies)
test = response.json()
print("response: ", response.json())
with open(f"direct_api_request_{timestamp}.json", "w") as f:
    f.write(str(test))
