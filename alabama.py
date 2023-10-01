import imaplib
import email
import html2text


def Email(username, password):
    imap_url = 'imap.gmail.com'

    # Connection with GMAIL using SSL
    my_mail = imaplib.IMAP4_SSL(imap_url)

    # Log in using your credentials
    my_mail.login(username, password)

    my_mail.select('Alabama')

    li = []  # List to store email data

    # Iterate through unseen emails
    _, data = my_mail.search(None, 'UNSEEN')
    mail_id_list = data[0].split()  # IDs of all unseen emails



    # Iterate through unseen emails and extract data
    for num in mail_id_list:
        typ, data = my_mail.fetch(num, '(RFC822)')
        msg_data = data[0][1]  # Extract message data
        li.append(msg_data)  # Append message data to the list

    return li


def logic(msg_data):
    # Initialize the result dictionary for this email
    formatted_result = {}
    html_converter = html2text.HTML2Text()
    my_msg = email.message_from_bytes(msg_data)

    if 'closed' in my_msg['subject']:
        formatted_result['Status'] = "closed"
    if 'Hold' in my_msg['subject']:
        formatted_result['Status'] = 'Hold'

    if "Requisition #" in my_msg['subject']:
        value = my_msg['subject'].split("Requisition #")[1].strip('\n')
        value = value.strip().split('\n')[0].split()[0]
        formatted_result['Requisition ID'] = value

    for part in my_msg.walk():
        if part.get_content_type() == 'text/plain':
            plain_text = part.get_payload()
        if part.get_content_type() == 'text/html':
            html_content = part.get_payload(decode=True).decode()
            plain_text = html_converter.handle(html_content)
            if "The following" in plain_text:
                value = plain_text.split("The following")[1]
                value = value.split('.')[0]
                formatted_result["comment"] = value

    return formatted_result


email_data_list = Email('vinitha.s@vrdella.com', 'udbb zntf hhwe fbxl')
for msg_data in email_data_list:
    result = logic(msg_data)
    print(result)
