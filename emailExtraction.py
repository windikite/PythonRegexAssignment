import re

text = "Emails: user1@domain.com, user2@exclude.com, user3@domain.com, https://user4@exclude.com"
scoured_text = ""
blacklisted_domains = ["exclude"]
for domain in blacklisted_domains:
    string = r"\b[A-Za-z0-9._%+-]+@" + re.escape(domain) + r"\.[A-Z|a-z]{2,}\b"
    scoured_text = re.sub(string, " ", text)
emails = re.findall(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", scoured_text)
print(emails)
