from OSINT-CIPHER-SRY.core import *
from OSINT-CIPHER-SRY.localuseragent import *


async def youtube(email, client, out):
    name = "youtube"
    domain = "youtube.com"
    method = "register"
    frequent_rate_limit = False

    try:
        headers = {
            'User-Agent': random_user_agent(),
            'Content-Type': 'application/json'
        }
        
        req = await client.post(
            "https://accounts.google.com/_/signup/webusernameavailability",
            params={
                "Email": email
            },
            headers=headers
        )
        
        if "true" in req.text.lower() or "taken" in req.text.lower():
            out.append({"name": name, "domain": domain, "method": method, "frequent_rate_limit": frequent_rate_limit,
                        "rateLimit": False,
                        "exists": True,
                        "emailrecovery": None,
                        "phoneNumber": None,
                        "others": None})
        else:
            out.append({"name": name, "domain": domain, "method": method, "frequent_rate_limit": frequent_rate_limit,
                        "rateLimit": False,
                        "exists": False,
                        "emailrecovery": None,
                        "phoneNumber": None,
                        "others": None})
    except Exception:
        out.append({"name": name, "domain": domain, "method": method, "frequent_rate_limit": frequent_rate_limit,
                    "rateLimit": True,
                    "exists": False,
                    "emailrecovery": None,
                    "phoneNumber": None,
                    "others": None})