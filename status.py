# # import imaplib
# # import email
# # import html2text
# # import re
# # from datetime import datetime
# #
# # user = 'vinitha.s@vrdella.com'
# # password = 'udbb zntf hhwe fbxl'
# #
# # imap_url = 'imap.gmail.com'
# #
# # # Connection with GMAIL using SSL
# # my_mail = imaplib.IMAP4_SSL(imap_url)
# #
# # # Log in using your credentials
# # my_mail.login(user, password)
# #
# # my_mail.select('Baxster')
# #
# # # key = 'FROM'
# # # value = 'jobs_della@vrdella.com'
# # _, data = my_mail.search(None, 'UNSEEN')
# #
# # mail_id_list = data[0].split()  # IDs of all emails that we want to fetch
# #
# # # formatted_result = {
# # #     "job_start_date": None,
# # #     "job_end_date": None,
# # #     "Requisition ID": None,
# # #     "Requisition Title": None,
# # #     "Client": "Baxter",
# # #     "job_bill_rate": None,
# # #     "Description": None,
# # #     "job_status": None,
# # #     "Business Unit": None,
# # #     "Location": None,
# # # }
# #
# # msgs = []  # empty list to capture all messages
# # # Iterate through messages and extract data into the msgs list
# # for num in mail_id_list:
# #     typ, data = my_mail.fetch(num, '(RFC822)')  # RFC822 returns the whole message (BODY fetches just body)
# #     msgs.append(data)
# #
# #     # Create an instance of html2text
# #     html_converter = html2text.HTML2Text()
# #
# #     for msg in msgs[::-1]:
# #         for response_part in msg:
# #             if type(response_part) is tuple:
# #                 my_msg = email.message_from_bytes(response_part[1])
# #
# #                 # print("_________________________________________")
# #                 # print("subj:", my_msg['subject'])
# #                 # print("from:", my_msg['from'])
# #                 # print("body:")
# #                 lii = []
# #                 for part in my_msg.walk():
# #                     # print(part.get_content_type())
# #                     if part.get_content_type() == 'text/plain':
# #                         pri = part.get_payload()
# #                     elif part.get_content_type() == 'text/html':
# #                         # Convert HTML to plain text using html2text
# #                         html_content = part.get_payload(decode=True).decode()
# #                         plain_text = html_converter.handle(html_content)
# #                         formatted_result = {}
# #
# #                         formatted_result['client'] = 'Baxter'
# #
# #                         if "Requisition ID" in plain_text:
# #                             value = plain_text.split("Requisition ID")[1].strip('\n')
# #                             value = value.strip().split('\n')[0]
# #                             formatted_result["clientjobid"] = value
# #
# #                         if "Requisition Title" in plain_text:
# #                             value = plain_text.split("Requisition Title")[1].strip('\n')
# #                             value = value.strip().split('\n')[0]
# #                             formatted_result["job_title"] = value
# #
# #                         if "Description" in plain_text:
# #                             value = plain_text.split("Description")[1].strip('\n')
# #                             description_lines = [line.strip() for line in value.split('\n') if line.strip()]
# #                             description_lines = description_lines[:8]
# #
# #                             if "Site" in plain_text:
# #                                 site_value = plain_text.split("Site")[1].strip('\n')
# #                                 site_value = site_value.strip().split('\n')[0]
# #                                 description_lines.append("Site:" + site_value)
# #
# #                             if "Business Unit Code" in plain_text:
# #                                 bu_code_value = plain_text.split("Business Unit Code")[1].strip('\n')
# #                                 bu_code_value = bu_code_value.strip().split('\n')[0]
# #                                 description_lines.append("Business Unit Code:" + bu_code_value)
# #
# #                             if "Site Code" in plain_text:
# #                                 site_code_value = plain_text.split("Site Code")[1].strip('\n')
# #                                 site_code_value = site_code_value.strip().split('\n')[0]
# #                                 description_lines.append("Site Code:" + site_code_value)
# #
# #                             if "Coordinator" in plain_text:
# #                                 coordinator_value = plain_text.split("Coordinator")[1].strip('\n')
# #                                 coordinator_value = coordinator_value.strip().split('\n')[0]
# #                                 description_lines.append("Coordinator:" + coordinator_value)
# #
# #                             for line in description_lines:
# #                                 if line.startswith("Pay Rate:") or line.startswith("Pay rate:"):
# #
# #                                     value = re.search(r'\d+(\.\d+)?', value)
# #                                     value = float(value.group())
# #                                     formatted_result["job_bill_rate"] = value
# #
# #                                     # Join all lines back into the "Description" field
# #                                     formatted_result["job_description"] = '\n'.join(description_lines)
# #
# #                                     if "Requisition Start Date" in plain_text:
# #                                         start = plain_text.split("Requisition Start Date")[1].strip('\n')
# #                                         start = start.strip().split('\n')[0].rstrip()
# #                                         start = datetime.strptime(start, "%Y-%m-%d").date()
# #                                         formatted_result["job_start_date"] = start
# #                                     if "Requisition End Date" in plain_text:
# #                                         end = plain_text.split("Requisition End Date")[1].strip('\n')
# #                                         end = end.strip().split('\n')[0].rstrip()
# #                                         end = datetime.strptime(end, "%Y-%m-%d").date()
# #                                         formatted_result["job_end_date"] = end
# #
# #                                     b = datetime.now().date()
# #                                     if start <= b and end >= b:
# #                                         formatted_result['job_status'] = 'Pending'
# #                                     else:
# #                                         formatted_result['job_status'] = 'Closed'
# #
# #                                     if "Business Unit" in plain_text:
# #                                         value = plain_text.split("Business Unit")[1].strip('\n')
# #                                         value = value.strip().split('\n')[0]
# #                                         formatted_result["business_unit"] = value
# #
# #                                     if "Location" in plain_text:
# #                                         value = plain_text.split("Location")[1].strip('\n')
# #                                         value = value.strip().split('\n')[0]
# #                                         formatted_result["Location"] = value
# #                                     # print(formatted_result)
# #
# #                                     lii.append(formatted_result)
# #
# #                 print(lii)
#
#
# import imaplib
# import email
# import html2text
# import re
# from datetime import datetime
#
# import mysql.connector
#
# conn = mysql.connector.connect(
#     host="127.0.0.1",
#     user="root",
#     password="Vrdella!6",
#     database="task",
# )
# cursor = conn.cursor()
# username='vinitha.s@vrdella.com',
# password='udbb zntf hhwe fbxl'
# imap_url = 'imap.gmail.com'
#
# # Connection with GMAIL using SSL
# my_mail = imaplib.IMAP4_SSL(imap_url)
#
# # Log in using your credentials
# my_mail.login(username, password)
#
# my_mail.select('Baxster')
# li = []
#
# _, data = my_mail.search(None, 'UNSEEN')
# inbox_item_list = data[0].split()
# email_list = []
#
# for item in inbox_item_list:
#     typ, data = my_mail.fetch(item, '(RFC822)')
#     for msg in data:
#         for response_part in msg:
#             if type(response_part) is tuple:
#                 my_msg = email.message_from_bytes(response_part[1])
#                 sub = msg['subject']
#     import re
#
#     for part in msg.walk():
#         if part.get_content_maintype() == 'multipart':
#             continue
#         if part.get_content_type() == "text/html":
#             html_content = part.get_payload(decode=True).decode(part.get_content_charset(), 'ignore')
#             plain_text_content = html2text.html2text(html_content)
#             if "Requisition ID" in plain_text_content:
#                 value = plain_text_content.split("Requisition ID")[1].strip('\n')
#                 value = value.split("---")[0].strip()
#                 id = value
#             if 'halted' in sub:
#                 status = 'halted'
#             if 'closed' in sub:
#                 status = 'closed'
#             if "Reason" in plain_text_content:
#                 value = plain_text_content.split("Reason")[1].strip('\n')
#                 value = value.strip().split('\n')[0].rstrip()
#                 comment = value
#
#             bool_value = "SELECT EXISTS(SELECT * FROM email_fetch WHERE clientjobid = %s)"
#             cursor.execute(bool_value, (id,))
#             result = cursor.fetchone()[0]
#             if result == 1:
#                 sql = "UPDATE email_fetch SET status = '{}' WHERE clientjobid= '{}'".format(status, id)
#                 cursor.execute(sql)
#                 sql1 = "UPDATE email_fetch SET comment = '{}' WHERE clientjobid= '{}'".format(comment, id)
#                 cursor.execute(sql1)
#                 conn.commit()
#
# import imaplib
# import email
# import html2text
# import re
# from datetime import datetime
#
#
# def fetch_emails(username, password):
#     imap_url = 'imap.gmail.com'
#
#     # Connection with GMAIL using SSL
#     my_mail = imaplib.IMAP4_SSL(imap_url)
#
#     # Log in using your credentials
#     my_mail.login(username, password)
#
#     my_mail.select('Baxster')
#     li = []
#
#     _, data = my_mail.search(None, 'UNSEEN')
#     mail_id_list = data[0].split()  # IDs of all emails that we want to fetch
#
#     # Iterate through messages and extract data into the msgs list
#     for num in mail_id_list:
#         typ, data = my_mail.fetch(num, '(RFC822)')  # RFC822 returns the whole message (BODY fetches just body)
#         # msg_data = data[0][1]  # Extract message data
#         li.append(data)  # Append message data to the list
#
#     return li
#
#
# def logic(li):
#     lii = []
#     # Rest of your logic here...
#     # Create an instance of html2text
#     html_converter = html2text.HTML2Text()
#     # Append message data to the list
#     for msg in li[::-1]:
#         for response_part in msg:
#             if type(response_part) is tuple:
#                 my_msg = email.message_from_bytes(response_part[1])
#
#                 # print("_________________________________________")
#                 # print("subj:", my_msg['subject'])
#                 # print("from:", my_msg['from'])
#                 # print("body:")
#
#                 for part in my_msg.walk():
#                     # print(part.get_content_type())
#                     if part.get_content_type() == 'text/plain':
#                         pri = part.get_payload()
#                     elif part.get_content_type() == 'text/html':
#                         # Convert HTML to plain text using html2text
#                         html_content = part.get_payload(decode=True).decode()
#                         plain_text = html_converter.handle(html_content)
#                         formatted_result = {}
#
#                         formatted_result['client'] = 'Baxter'
#
#                         if "Requisition ID" in plain_text:
#                             value = plain_text.split("Requisition ID")[1].strip('\n')
#                             value = value.strip().split('\n')[0]
#                             formatted_result["clientjobid"] = value
#
#                         if "Requisition Title" in plain_text:
#                             value = plain_text.split("Requisition Title")[1].strip('\n')
#                             value = value.strip().split('\n')[0]
#                             formatted_result["job_title"] = value
#
#                         if "Description" in plain_text:
#                             value = plain_text.split("Description")[1].strip('\n')
#                             description_lines = [line.strip() for line in value.split('\n') if line.strip()]
#                             description_lines = description_lines[:8]
#
#                             if "Site" in plain_text:
#                                 site_value = plain_text.split("Site")[1].strip('\n')
#                                 site_value = site_value.strip().split('\n')[0]
#                                 description_lines.append("Site:" + site_value)
#
#                             if "Business Unit Code" in plain_text:
#                                 bu_code_value = plain_text.split("Business Unit Code")[1].strip('\n')
#                                 bu_code_value = bu_code_value.strip().split('\n')[0]
#                                 description_lines.append("Business Unit Code:" + bu_code_value)
#
#                             if "Site Code" in plain_text:
#                                 site_code_value = plain_text.split("Site Code")[1].strip('\n')
#                                 site_code_value = site_code_value.strip().split('\n')[0]
#                                 description_lines.append("Site Code:" + site_code_value)
#
#                             if "Coordinator" in plain_text:
#                                 coordinator_value = plain_text.split("Coordinator")[1].strip('\n')
#                                 coordinator_value = coordinator_value.strip().split('\n')[0]
#                                 description_lines.append("Coordinator:" + coordinator_value)
#
#                             for line in description_lines:
#                                 if line.startswith("Pay Rate:") or line.startswith("Pay rate:"):
#
#                                     value = re.search(r'\d+(\.\d+)?', value)
#                                     value = float(value.group())
#                                     formatted_result["job_bill_rate"] = value
#
#                                     # Join all lines back into the "Description" field
#                                     formatted_result["job_description"] = '\n'.join(description_lines)
#
#                                     if "Requisition Start Date" in plain_text:
#                                         start = plain_text.split("Requisition Start Date")[1].strip('\n')
#                                         start = start.strip().split('\n')[0].rstrip()
#                                         start = datetime.strptime(start, "%Y-%m-%d").date()
#                                         formatted_result["job_start_date"] = start
#                                     if "Requisition End Date" in plain_text:
#                                         end = plain_text.split("Requisition End Date")[1].strip('\n')
#                                         end = end.strip().split('\n')[0].rstrip()
#                                         end = datetime.strptime(end, "%Y-%m-%d").date()
#                                         formatted_result["job_end_date"] = end
#
#                                     b = datetime.now().date()
#                                     if start <= b and end >= b:
#                                         formatted_result['job_status'] = 'Pending'
#                                     else:
#                                         formatted_result['job_status'] = 'Closed'
#
#                                     if "Business Unit" in plain_text:
#                                         value = plain_text.split("Business Unit")[1].strip('\n')
#                                         value = value.strip().split('\n')[0]
#                                         formatted_result["business_unit"] = value
#
#                                     if "Location" in plain_text:
#                                         value = plain_text.split("Location")[1].strip('\n')
#                                         value = value.strip().split('\n')[0]
#                                         formatted_result["location"] = value
#                                     # print(formatted_result)
#
#                         lii.append(formatted_result)
#     return lii
#
#     # Rest of your code...
#
#
# email_data_list = fetch_emails('vinitha.s@vrdella.com', 'udbb zntf hhwe fbxl')
# # for msg_data in email_data_list:
# #     result = logic(msg_data)
# l = logic(email_data_list)
# print(l)
#
# import mysql.connector
#
# # Connect to your MySQL database
# conn = mysql.connector.connect(
#     host="127.0.0.1",
#     user="root",
#     password="vrdella!6",
#     database="json1",
# )
#
# cursor = conn.cursor()
# sql = """
#     INSERT INTO email (clientjobid, job_title, location, job_start_date, job_end_date, business_unit, job_bill_rate, job_description, job_status, client)
#     VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
#     """
# for record in l:
#     values = (
#             record.get("clientjobid"),  # Use get with a default value of None
#             record.get("job_title"),
#             record.get("location"),  # Use get with a default value of None
#             str(record.get("job_start_date")),  # Use get with a default value of None
#             str(record.get("job_end_date")),  # Use get with a default value of None
#             record.get("business_unit"),  # Use get with a default value of None
#             record.get("job_bill_rate"),  # Use get with a default value of None
#             record.get("job_description"),  # Use get with a default value of None
#             record.get("job_status"),  # Use get with a default value of None
#             record.get("client")  # Use get with a default value of None
#         )
#
#     # Execute the SQL INSERT statement
#     cursor.execute(sql, values)
#
# # Commit the changes to the database
# conn.commit()
#
# # Close the cursor and database connection
# cursor.close()
# conn.close()

# sql = """
#     INSERT INTO email-fetch (clientjobid, job_title, location, job_start_date, job_end_date, business_unit, job_bill_rate, job_description, job_status, client)
#     VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
#     """
# for record in l:
#     values = (
#         record["clientjobid"],
#         record["job_title"],
#         record["location"],
#         str(record["job_start_date"]),
#         str(record["job_end_date"]),
#         record["business_unit"],
#         record["job_bill_rate"],
#         record["job_description"],
#         record["job_status"],
#         record["client"]
#     )
# values = (
#     record.get("clientjobid", None),  # Use get with a default value of None
#     record.get("job_title", None),
#     record.get("location", None),  # Use get with a default value of None
#     str(record.get("job_start_date", None)),  # Use get with a default value of None
#     str(record.get("job_end_date", None)),  # Use get with a default value of None
#     record.get("business_unit", None),  # Use get with a default value of None
#     record.get("job_bill_rate", None),  # Use get with a default value of None
#     record.get("job_description", None),  # Use get with a default value of None
#     record.get("job_status", None),  # Use get with a default value of None
#     record.get("client", None)  # Use get with a default value of None
# )
# cursor.execute(sql, values)
#
# # Commit the changes to the database
# conn.commit()
#
# # Close the cursor and database connection
# cursor.close()
# conn.close()

# import imaplib
# import email
# import html2text
# import re
# from datetime import datetime
#
# imap_url = 'imap.gmail.com'
# username = 'vinitha.s@vrdella.com'
# password = 'udbb zntf hhwe fbxl'
#
# # Connection with GMAIL using SSL
# my_mail = imaplib.IMAP4_SSL(imap_url)
#
# # Log in using your credentials
# my_mail.login(username, password)
#
# my_mail.select('Baxster')
# li = []
#
# _, data = my_mail.search(None, 'UNSEEN')
# mail_id_list = data[0].split()  # IDs of all emails that we want to fetch
#
# # Rest of your logic here...
# # Create an instance of html2text
# html_converter = html2text.HTML2Text()
# # Append message data to the list
# for num in mail_id_list:
#     typ, data = my_mail.fetch(num, '(RFC822)')  # RFC822 returns the whole message (BODY fetches just body)
#     # msg_data = data[0][1]  # Extract message data
#     li.append(data)  # Append message data to the list
#
# # Iterate through messages and extract data into the msgs list
# for msg_data in li[::-1]:
#     formatted_result = {}  # Initialize the dictionary for each email
#     for response_part in msg_data:
#         if isinstance(response_part, tuple):
#             my_msg = email.message_from_bytes(response_part[1])
#             lii = []
#             # Check if 'halted' or 'closed' is in the subject and set job_status accordingly
#             if 'halted' in my_msg['subject']:
#                 formatted_result['job_status'] = 'halted'
#             elif 'closed' in my_msg['subject']:
#                 formatted_result['job_status'] = 'closed'
#
#             for part in my_msg.walk():
#                 if part.get_content_type() == 'text/html':
#                     html_content = part.get_payload(decode=True).decode()
#                     plain_text = html_converter.handle(html_content)
#
#                     if "Requisition ID" in plain_text:
#                         value = plain_text.split("Requisition ID")[1].strip('\n')
#                         value = value.strip().split('\n')[0]
#                         formatted_result["clientjobid"] = value
#
#                     if "Reason" in plain_text:
#                         value = plain_text.split("Reason")[1].strip('\n')
#                         value = value.strip().split('\n')[0].rstrip()
#                         formatted_result['comment'] = value
#
#             # Print or store the result for each email
#             # lii.append(formatted_result)
#             print(formatted_result)
#           # print(lii)
#
#             import mysql.connector
#
#             # Connect to your MySQL database
#             conn = mysql.connector.connect(
#                 host="127.0.0.1",
#                 user="root",
#                 password="vrdella!6",
#                 database="json1",
#             )
#
#             cursor = conn.cursor()
#
#             for record in formatted_result:
#                 # Check if the clientjobid exists in the database
#                 check_query = "SELECT clientjobid FROM email WHERE clientjobid = %s"
#                 cursor.execute(check_query, (record["clientjobid"],))
#                 existing_record = cursor.fetchone()
#
#                 if existing_record:
#                     # If the record exists, update it
#                     update_query = """
#                         UPDATE email
#                         SET
#                             job_title = %s,
#                             Location = %s,
#                             job_start_date = %s,
#                             job_end_date = %s,
#                             business_unit = %s,
#                             job_bill_rate = %s,
#                             job_description = %s,
#                             client = %s
#                         WHERE clientjobid = %s,
#                         WHERE job_status = %s,
#                         WHERE  comment = %s,
#                     """
#                     values = (
#                         record["job_title"],
#                         record["Location"],
#                         str(record["job_start_date"]),
#                         str(record["job_end_date"]),
#                         record["business_unit"],
#                         record["job_bill_rate"],
#                         record["job_description"],
#                         record["client"],
#                         record["clientjobid"],
#                         record["job_status"],
#                         record['comment'],
#                     )
#                     cursor.execute(update_query, values)
#                 else:
#                     # If the record doesn't exist, insert a new one
#                     insert_query = """
#                         INSERT INTO email (clientjobid, job_title, Location, job_start_date, job_end_date, business_unit, job_bill_rate, job_description, job_status, client,comment)
#                         VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s)
#                     """
#                     values = (
#                         record["clientjobid"],
#                         record["job_title"],
#                         record["Location"],
#                         str(record["job_start_date"]),
#                         str(record["job_end_date"]),
#                         record["business_unit"],
#                         record["job_bill_rate"],
#                         record["job_description"],
#                         record["job_status"],
#                         record['comment'],
#                         record["client"],
#                     )
#                     cursor.execute(insert_query, values)
#
#             # Commit the changes to the database
#             conn.commit()
#
#             # Close the cursor and database connection
#             cursor.close()
#             conn.close()

import imaplib
import email
import html2text
import re
from datetime import datetime
import mysql.connector

imap_url = 'imap.gmail.com'
username = 'vinitha.s@vrdella.com'
password = 'udbb zntf hhwe fbxl'

# Connection with GMAIL using SSL
my_mail = imaplib.IMAP4_SSL(imap_url)

# Log in using your credentials
my_mail.login(username, password)

my_mail.select('Baxster')
li = []

_, data = my_mail.search(None, 'UNSEEN')
mail_id_list = data[0].split()  # IDs of all emails that we want to fetch

# Rest of your logic here...
# Create an instance of html2text
html_converter = html2text.HTML2Text()
# Append message data to the list
for num in mail_id_list:
    typ, data = my_mail.fetch(num, '(RFC822)')  # RFC822 returns the whole message (BODY fetches just body)
    # msg_data = data[0][1]  # Extract message data
    li.append(data)  # Append message data to the list

# Initialize a list to store formatted results
formatted_results = []

# Iterate through messages and extract data into the msgs list
for msg_data in li[::-1]:
    formatted_result = {}  # Initialize the dictionary for each email

    for response_part in msg_data:
        if isinstance(response_part, tuple):
            my_msg = email.message_from_bytes(response_part[1])
            lii = []
            # Check if 'halted' or 'closed' is in the subject and set job_status accordingly
            if 'halted' in my_msg['subject']:
                formatted_result['job_status'] = 'halted'
            elif 'closed' in my_msg['subject']:
                formatted_result['job_status'] = 'closed'

            for part in my_msg.walk():
                if part.get_content_type() == 'text/html':
                    html_content = part.get_payload(decode=True).decode()
                    plain_text = html_converter.handle(html_content)

                    if "Requisition ID" in plain_text:
                        value = plain_text.split("Requisition ID")[1].strip('\n')
                        value = value.strip().split('\n')[0]
                        formatted_result["clientjobid"] = value

                    if "Reason" in plain_text:
                        value = plain_text.split("Reason")[1].strip('\n')
                        value = value.strip().split('\n')[0].rstrip()
                        formatted_result['comment'] = value

            # Append the formatted result to the list
            formatted_results.append(formatted_result)

# Connect to your MySQL database
conn = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="vrdella!6",
    database="json1",
)

cursor = conn.cursor()
# ... (previous code)

# ... (previous code)

# ... (previous code)

for record in formatted_results:
    # Check if the clientjobid exists in the database
    check_query = "SELECT clientjobid FROM email WHERE clientjobid = %s"
    cursor.execute(check_query, (record["clientjobid"],))
    existing_record = cursor.fetchone()

    # Initialize a dictionary with default values of None
    defaults = {
        "job_title": None,
        "Location": None,
        "job_start_date": None,
        "job_end_date": None,
        "business_unit": None,
        "job_bill_rate": None,
        "job_description": None,
        "client": None,
        "job_status": None,
        "comment": None,
    }

    if existing_record:
        # If the record exists, update it
        update_query = """
            UPDATE email
            SET
                job_title = %s,
                Location = %s,
                job_start_date = %s,
                job_end_date = %s,
                business_unit = %s,
                job_bill_rate = %s,
                job_description = %s,
                client = %s,
                job_status = %s,
                comment = %s
            WHERE clientjobid = %s
        """
        values = (
            record.get("job_title", defaults["job_title"]),
            record.get("Location", defaults["Location"]),
            str(record.get("job_start_date", defaults["job_start_date"])) if record.get("job_start_date") else None,
            str(record.get("job_end_date", defaults["job_end_date"])) if record.get("job_end_date") else None,
            record.get("business_unit", defaults["business_unit"]),
            record.get("job_bill_rate", defaults["job_bill_rate"]),
            record.get("job_description", defaults["job_description"]),
            record.get("client", defaults["client"]),
            record.get("job_status", defaults["job_status"]),
            record.get("comment", defaults["comment"]),
            record["clientjobid"],
        )
        cursor.execute(update_query, values)
    else:
        # If the record doesn't exist, insert a new one
        insert_query = """
            INSERT INTO email (clientjobid, job_title, Location, job_start_date, job_end_date, business_unit, job_bill_rate, job_description, job_status, client, comment)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        values = (
            record["clientjobid"],
            record.get("job_title", defaults["job_title"]),
            record.get("Location", defaults["Location"]),
            str(record.get("job_start_date", defaults["job_start_date"])) if record.get("job_start_date") else None,
            str(record.get("job_end_date", defaults["job_end_date"])) if record.get("job_end_date") else None,
            record.get("business_unit", defaults["business_unit"]),
            record.get("job_bill_rate", defaults["job_bill_rate"]),
            record.get("job_description", defaults["job_description"]),
            record.get("job_status", defaults["job_status"]),
            record.get("comment", defaults["comment"]),
            record.get("client", defaults["client"]),
        )
        cursor.execute(insert_query, values)

conn.commit()

cursor.close()
conn.close()

# ... (remaining code)

#
# for record in formatted_results:
#     # Check if the clientjobid exists in the database
#     check_query = "SELECT clientjobid FROM email WHERE clientjobid = %s"
#     cursor.execute(check_query, (record["clientjobid"],))
#     existing_record = cursor.fetchone()
#
#     if existing_record:
#         # If the record exists, update it
#         update_query = """
#             UPDATE email
#             SET
#                 job_title = %s,
#                 Location = %s,
#                 job_start_date = %s,
#                 job_end_date = %s,
#                 business_unit = %s,
#                 job_bill_rate = %s,
#                 job_description = %s,
#                 client = %s,
#                 job_status = %s,
#                 comment = %s
#             WHERE clientjobid = %s
#         """
#         values = (
#             record["job_title"],
#             record["Location"],
#             str(record["job_start_date"]),
#             str(record["job_end_date"]),
#             record["business_unit"],
#             record["job_bill_rate"],
#             record["job_description"],
#             record["client"],
#             record["job_status"],
#             record['comment'],
#             record["clientjobid"],
#         )
#         cursor.execute(update_query, values)
#     else:
#         # If the record doesn't exist, insert a new one
#         insert_query = """
#             INSERT INTO email (clientjobid, job_title, Location, job_start_date, job_end_date, business_unit, job_bill_rate, job_description, job_status, client, comment)
#             VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
#         """
#         values = (
#             record["clientjobid"],
#             record["job_title"],
#             record["Location"],
#             str(record["job_start_date"]),
#             str(record["job_end_date"]),
#             record["business_unit"],
#             record["job_bill_rate"],
#             record["job_description"],
#             record["job_status"],
#             record['comment'],
#             record["client"],
#         )
#         cursor.execute(insert_query, values)

# Commit the changes to the database
# conn.commit()
#
# # Close the cursor and database connection
# cursor.close()
# conn.close()
