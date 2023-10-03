import imaplib
import email
import html2text
import re
from datetime import datetime


def fetch_emails(username, password):
    imap_url = 'imap.gmail.com'

    # Connection with GMAIL using SSL
    my_mail = imaplib.IMAP4_SSL(imap_url)

    # Log in using your credentials
    my_mail.login(username, password)

    my_mail.select('Baxster')
    li = []

    _, data = my_mail.search(None, 'UNSEEN')
    mail_id_list = data[0].split()  # IDs of all emails that we want to fetch

    # Iterate through messages and extract data into the msgs list
    for num in mail_id_list:
        typ, data = my_mail.fetch(num, '(RFC822)')  # RFC822 returns the whole message (BODY fetches just body)
        msg_data = data[0][1]  # Extract message data
        li.append(msg_data)  # Append message data to the list

    return li


def logic(msg_data):
    # Rest of your logic here...
    # Create an instance of html2text
    html_converter = html2text.HTML2Text()
    # Append message data to the list
    formatted_result = {}

    my_msg = email.message_from_bytes(msg_data)

    # print("_________________________________________")
    # print("subj:", my_msg['subject'])
    # print("from:", my_msg['from'])
    # print("body:")

    for part in my_msg.walk():
        # print(part.get_content_type())
        if part.get_content_type() == 'text/plain':
            pri = part.get_payload()
        elif part.get_content_type() == 'text/html':
            # Convert HTML to plain text using html2text
            html_content = part.get_payload(decode=True).decode()
            plain_text = html_converter.handle(html_content)

            if "Requisition ID" in plain_text:
                value = plain_text.split("Requisition ID")[1].strip('\n')
                value = value.split("---")[0].strip()
                formatted_result["Requisition ID"] = value

            if "Requisition Title" in plain_text:
                value = plain_text.split("Requisition Title")[1].strip('\n')
                value = value.strip().split('\n')[0]
                formatted_result["Requisition Title"] = value

            if "Description" in plain_text:
                value = plain_text.split("Description")[1].strip('\n')
                description_lines = [line.strip() for line in value.split('\n') if line.strip()]
                description_lines = description_lines[:8]

                if "Site" in plain_text:
                    site_value = plain_text.split("Site")[1].strip('\n')
                    site_value = site_value.strip().split('\n')[0]
                    description_lines.append("Site:" + site_value)

                if "Business Unit Code" in plain_text:
                    bu_code_value = plain_text.split("Business Unit Code")[1].strip('\n')
                    bu_code_value = bu_code_value.strip().split('\n')[0]
                    description_lines.append("Business Unit Code:" + bu_code_value)

                if "Site Code" in plain_text:
                    site_code_value = plain_text.split("Site Code")[1].strip('\n')
                    site_code_value = site_code_value.strip().split('\n')[0]
                    description_lines.append("Site Code:" + site_code_value)

                if "Coordinator" in plain_text:
                    coordinator_value = plain_text.split("Coordinator")[1].strip('\n')
                    coordinator_value = coordinator_value.strip().split('\n')[0]
                    description_lines.append("Coordinator:" + coordinator_value)

                for line in description_lines:
                    if line.startswith("Pay Rate:") or line.startswith("Pay rate:"):

                        value = re.search(r'\d+(\.\d+)?', value)
                        value = float(value.group())
                        formatted_result["job_bill_rate"] = value

                        # Join all lines back into the "Description" field
                        formatted_result["Description"] = '\n'.join(description_lines)

                        if "Requisition Start Date" in plain_text:
                            start = plain_text.split("Requisition Start Date")[1].strip('\n')
                            start = start.strip().split('\n')[0].rstrip()
                            start = datetime.strptime(start, "%Y-%m-%d").date()
                            formatted_result["job_start_date"] = start
                        if "Requisition End Date" in plain_text:
                            end = plain_text.split("Requisition End Date")[1].strip('\n')
                            end = end.strip().split('\n')[0].rstrip()
                            end = datetime.strptime(end, "%Y-%m-%d").date()
                            formatted_result["job_end_date"] = end

                        b = datetime.now().date()
                        if start <= b and end >= b:
                            formatted_result['job_status'] = 'Pending'
                        else:
                            formatted_result['job_status'] = 'Closedd'

                        if "Business Unit" in plain_text:
                            value = plain_text.split("Business Unit")[1].strip('\n')
                            value = value.strip().split('\n')[0]
                            formatted_result["Business Unit"] = value

                        if "Location" in plain_text:
                            value = plain_text.split("Location")[1].strip('\n')
                            value = value.strip().split('\n')[0]
                            formatted_result["Location"] = value

    return formatted_result


email_data_list = fetch_emails('vinitha.s@vrdella.com', 'udbb zntf hhwe fbxl')
for msg_data in email_data_list:
    result = logic(msg_data)
    print(result)