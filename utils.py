import hashlib
from models import User

def get_gravatar_hash(email, size=80, default="identicon"):
    email = email.strip().lower()
    email_hash = hashlib.md5(email.encode("utf-8")).hexdigest()
    url = f"https://www.gravatar.com/avatar/{email_hash}?s={size}&d={default}"
    return url