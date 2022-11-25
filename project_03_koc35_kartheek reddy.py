email_id = input("Enter an email address: ").strip()
if "@" in email_id:
    username = email_id[:email_id.index('@')]
    domain = email_id[email_id.index('@')+1:]
    print("Username: " + username)
    print("Domain: " + domain)
else:
    print("Invalid Email address")
