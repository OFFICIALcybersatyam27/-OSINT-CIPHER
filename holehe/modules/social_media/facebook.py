from OSINT-CIPHER-SRY.core import *
from OSINT-CIPHER-SRY.localuseragent import *


async def facebook(email, client, out):
    name = "facebook"
    domain = "facebook.com"
    method = "register"
    frequent_rate_limit = False

    try:
        headers = {
            'User-Agent': random_user_agent(),
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.5',
            'Referer': 'https://www.facebook.com/',
            'Content-Type': 'application/x-www-form-urlencoded',
        }
        
        req = await client.post(
            "https://www.facebook.com/ajax/reg/checkmail/",
            data={
                'email': email
            },
            headers=headers
        )
        
        response_text = req.text
        
        if '"email_already_used"' in response_text or '"taken"' in response_text:
            out.append({"name": 