import re
import csv
from operator import itemgetter

def error_stats(log_file):

    error_pattern = r" ticky: ERROR ([\w ']*) "

    error_details = {}

    with open(log_file, 'r') as file:
        for line in file.readlines():
            result = re.search(error_pattern, line)
            if result:
                if result[1] not in error_details:
                    error_details[result[1]] = 1
                else:
                    error_details[result[1]] += 1

    return sorted(error_details.items(), key=itemgetter(1), reverse=True)

def user_stats(log_file):

    user_pattern = r": ([A-Z]+).*\(([\w\.]+)\)"
    user_details = {}

    with open(log_file, 'r') as file:
        for line in file.readlines():
            result = re.search(user_pattern, line)
            if result:
                msg, user = result[1], result[2]
                #print(user, msg)
                if user not in user_details:
                    user_details[user] = [0, 0]
                if user in user_details and msg == 'INFO':
                    user_details[user][0] += 1
                elif user in user_details and  msg == 'ERROR':
                    user_details[user][1] += 1

    per_user = sorted(user_details.items(), key=itemgetter(0))

    return per_user

def generate_reports(error_details, user_details):

    error_details.insert(0, ("Error", "Count"))
    fields = ("Username", "INFO", "ERROR")

    #print(error_details, user_details)
    with open('error_message.csv', 'w') as report:
        csv_writer = csv.writer(report)
        csv_writer.writerows(error_details)

    with open('user_statistics.csv', 'w') as report:
        csv_writer = csv.DictWriter(report, fieldnames=fields)
        for user, details in user_details:
            #print(user, details)
            csv_writer.writerow({"Username":user, "INFO":details[0], "ERROR":details[1]})

log_file = 'syslog.log'

error_details = error_stats(log_file)
user_details = user_stats(log_file)
generate_reports(error_details, user_details)
