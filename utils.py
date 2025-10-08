import hashlib
import markdown

def get_gravatar_hash(email, size=30, default="identicon"):
    email = email.strip().lower()
    email_hash = hashlib.md5(email.encode("utf-8")).hexdigest()
    url = f"https://www.gravatar.com/avatar/{email_hash}?s={size}&d={default}"
    return url

def sanitize_text(text: str) -> str:
    sanText = text
    sanText = sanText.replace("<script>", "")
    sanText = sanText.replace("</script>", "")
    return sanText

def to_markdown(text: str) -> str:
    sanText = sanitize_text(text)
    return markdown.markdown(sanText)