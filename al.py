import imaplib
import email
import html2text
import re
from datetime import datetime

user = 'vinitha.s@vrdella.com'
password = 'udbb zntf hhwe fbxl'

imap_url = 'imap.gmail.com'

# Connection with GMAIL using SSL
my_mail = imaplib.IMAP4_SSL(imap_url)

# Log in using your credentials
my_mail.login(user, password)

my_mail.select('Alabama')

# key = 'FROM'
# value = 'jobs_della@vrdella.com'
_, data = my_mail.search(None, 'UNSEEN')

mail_id_list = data[0].split()  # IDs of all emails that we want to fetch

li = []
msgs = []  # empty list to capture all messages
# Iterate through messages and extract data into the msgs list
for num in mail_id_list:
    typ, data = my_mail.fetch(num, '(RFC822)')  # RFC822 returns the whole message (BODY fetches just body)
    msgs.append(data)

# Create an instance of html2text
html_converter = html2text.HTML2Text()

for msg in msgs[::-1]:
    for response_part in msg:
        if type(response_part) is tuple:
            my_msg = email.message_from_bytes(response_part[1])
            formatted_result = {}
            # print("_________________________________________")
            # print("subj:", my_msg['subject'])
            # print("from:", my_msg['from'])
            # print("body:")
            if 'closed' in my_msg['subject']:
                formatted_result['Status'] = "closed"
            if 'Hold' in my_msg['subject']:
                formatted_result['Status'] = 'Hold'

            if "Requisition #" in my_msg['subject']:
                value = my_msg['subject'].split("Requisition #")[1].strip('\n')
                value = value.strip().split('\n')[0].split()[0]
                formatted_result['Requisition ID'] = value

            for part in my_msg.walk():
                # print(part.get_content_type())
                if part.get_content_type() == 'text/plain':
                    plain_text = part.get_payload()
                elif part.get_content_type() == 'text/html':
                    # Convert HTML to plain text using html2text
                    html_content = part.get_payload(decode=True).decode()
                    plain_text = html_converter.handle(html_content)
                    # match = re.search(r'Requisition\s*#?\s*:\s*(\d+)', plain_text)
                    # if match:
                    #         formatted_result["Requisition ID"] = match.group(1)
                    if "The following" in plain_text:
                        value = plain_text.split("The following")[1].strip('\n')
                        value = value.strip().split('.')[0]
                        formatted_result["comment"] = value

            li.append(formatted_result)
print(li)
