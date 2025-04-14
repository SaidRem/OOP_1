import csv
import re
from collections import OrderedDict
from pprint import pprint


def get_contacts_list(file_name):
    with open(file_name, encoding='utf-8') as f:
        rows = csv.reader(f, delimiter=',')
        contacts_list = list(rows)
    return contacts_list


def format_phone_num(contact_list):
    pat = re.compile(
        r'(?:8|\+7)\s*\(?(\d{3})\)?[\s-]*'
        r'(\d{3})[\s-]*'
        r'(\d{2})[\s-]*'
        r'(\d{2})'
        r'(?:\s*\(?(доб\.?)\s*(\d+)\)?)?'
    )

    for row in contact_list[1:]:
        phone = row[5]
        if phone:
            match = pat.search(phone)
            if match:
                row[5] = f'+7({match.group(1)}){match.group(2)}-{match.group(3)}-{match.group(4)}'
                if match.group(5) and match.group(6):
                    row[5] += f' доб.{match.group(6)}'


def format_names(contact_list):
    for row in contact_list[1:]:
        full_name = ' '.join(row[:3]).strip()
        name_parts = full_name.split()

        if len(name_parts) == 3:
            row[0], row[1], row[2] = name_parts
        elif len(name_parts) == 2:
            row[0], row[1] = name_parts
            row[2] = ''
        elif len(name_parts) == 1:
            row[0] = name_parts[0]
            row[1], row[2] = '', ''
        else:
            row[0], row[1], row[2] = '', '', ''


def merge_data(contact_list):
    header = contact_list[0]
    merged = OrderedDict()

    for row in contact_list[1:]:
        key = (row[0], row[1])

        if key not in merged:
            merged[key] = row
        else:
            existing = merged[key]
            for i in range(len(existing)):
                if not existing[i] and row[i]:
                    existing[i] = row[i]

    return [header] + list(merged.values())


if __name__ == '__main__':
    contacts_list = get_contacts_list(r'phonebook_raw.csv')
    format_names(contacts_list)
    format_phone_num(contacts_list)
    result = merge_data(contacts_list)

    with open('phonebook.csv', 'w', encoding='utf-8', newline='') as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(result)
