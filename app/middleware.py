import os
from fastapi import Request, HTTPException

WHITELISTED_IPS = os.getenv("WHITELISTED_IPS", "").split(',')


async def ip_whitelist_middleware(request: Request, call_next):
    client_ip = request.client.host
    if client_ip not in WHITELISTED_IPS:
        raise HTTPException(
            status_code=403, detail="Forbidden: IP not allowed")
    response = await call_next(request)
    return response
