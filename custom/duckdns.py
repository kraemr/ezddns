import requests as req
import os

def update_ip_addresses(ipv4,ipv6,hostname,token):
	url = f"https://www.duckdns.org/update?domains={hostname}&token={token}&ip={ipv4}&ipv6={ipv6}&verbose=true"
	print(url)
	res = req.get(url)
	print(res)
	print(res.text)
