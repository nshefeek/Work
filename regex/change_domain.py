import csv
import re

def contains_domain(address, domain):

    domain_pattern = r"[\w.-]+@"+domain+'$'
    if re.match(domain_pattern, address):
        return True
    return False

def replace_domain(address, old_domain, new_domain):
    address = re.sub(old_domain, new_domain, address)
    return address

def main():

    old_domain, new_domain = 'abc.edu', 'xyz.edu'
    csv_file_name = 'user_email.csv'
    with open(csv_file_name, 'r') as f:
        csv_reader = csv.reader(f)
        user_data = list(csv_reader)

    user_email_list = []
    for user in user_data:
        user_email_list.append(user[1].strip())

    old_email_list = []
    new_email_list = []

    for email in user_email_list:
        if contains_domain(email, old_domain):
            replaced_email = replace_domain(email, old_domain, new_domain)
            new_email_list.append(replaced_email)
        else:
            new_email_list.append(email)

    print(user_email_list, new_email_list)


if __name__ == "__main__":
    main()



