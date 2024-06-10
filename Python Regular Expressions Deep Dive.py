import re

text = "Emails: user1@domain.com, user2@exclude.com, user3@domain.com"
# Extract all email addresses first
emails = re.findall(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", text)
# Filter out the emails that are from 'exclude.com'
filtered_emails = [email for email in emails if not email.endswith('@exclude.com')]
print(filtered_emails)
