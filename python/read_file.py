import re


def count_valid_emails(file_path):
    email_regex_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

    email_count = 0

    with open(file_path, 'r') as file:
        for line in file:
            emails = re.findall(email_regex_pattern, line)
            email_count += len(emails)

    return email_count


file_path = 'emails.txt'
print(f"Valid emails: {count_valid_emails(file_path)}")
