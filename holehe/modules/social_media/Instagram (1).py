from OSINT-CIPHER-SRY.core import *
from OSINT-CIPHER-SRY.localuseragent import *


async def instagram(email, client, out):
    name = "instagram"
    domain = "instagram.com"
    method = "register"
    frequent_rate_limit = True

    try:
        headers = {
            'User-Agent': random_user_agent(),
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.5',
            'X-Requested-With': 'XMLHttpRequest',
            'Content-Type': 'application/x-www-form-urlencoded',
        }
        
        data = {
            'email': email
        }
        
        req = await client.post(
            "https://www.instagram.com/accounts/web_create_ajax/attempt/",
            data=data,
            headers=headers
        )
        
        response = req.json()
        
        if response.get("email_is_taken") or response.get("account_created") == False:
            out.append({"name": name, "domain": domain, "method": method, "frequent_rate_limit": frequent_rate_limit,
                        "rateLimit": False,
                        "exists": True,
                        "emailrecovery": None,
                        "phoneNumber": None,
                        "others": None})
        elif "errors" in response and "email" in response["errors"]:
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