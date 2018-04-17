import poplib
from email.parser import Parser
from email.header import Header, decode_header
from email.utils import parseaddr
from urllib.parse import unquote
import base64


def decode_str(s):
    value, charset = decode_header(s)[0]
    if charset:
        value = value.decode(charset)
    return value


def guess_charset(msg):
    charset = msg.get_charset()
    if charset is None:
        content_type = msg.get('Content-Type', '').lower()
        pos = content_type.find('charset=')
        if pos >= 0:
            charset = content_type[pos + 8:].strip()
    return charset


def get_email_headers(msg):
    headers = {}
    for header in ['From', 'To', 'Subject', 'Date']:
        value = msg.get(header, '')
        if value:
            if header == 'Date':
                headers['Data'] = value
            if header == 'Subject':
                subject = decode_str(value)
                headers['subject'] = subject
            else:
                hdr, addr = parseaddr(value)
                name = decode_str(hdr)
                value = u'%s <%s>' % (name, addr)
                if header == 'From':
                    from_address = value
                    headers['from'] = from_address
                else:
                    to_address = value
                    headers['to'] = to_address
    content_type = msg.get_content_type()
    print('Head content type: %s' % content_type)
    return headers


def process_filename(filename):
    filename_splited = filename.split(b'?')
    charset = str(filename_splited[1].lower())[2:-1]
    method = str(filename_splited[2].lower())[2:-1]
    filename_encoded = str(filename_splited[3])[2:-1]
    if method == 'q':
        filename_encoded = filename_encoded.replace('=', '%')
        real_filename = unquote(filename_encoded)
    else:
        real_filename = base64.b64decode(filename_encoded)
    if isinstance(real_filename, str):
        return real_filename
    return real_filename.decode(charset)


def get_email_content(message, base_save_path):
    j = 0
    content = ''
    attachment_files = []
    for part in message.walk():
        j = j + 1
        filename = part.get_filename()
        contentType = part.get_content_type()
        if filename:
            h = Header(filename)
            dh = decode_header(h)
            filename = dh[0][0]
            if dh[0][1]:
                filename = str(filename, dh[0][1])
                filename = filename.encode('utf-8')
            data = part.get_payload(decode=True)
            # print(filename)
            filename = process_filename(filename)
            att_file = open(base_save_path + filename, 'wb')
            attachment_files.append(filename)
            att_file.write(data)
            att_file.close()
        elif contentType == 'text/plain' or contentType == 'text/html':
            data = part.get_payload(decode=True)
            charset = guess_charset(part)
            if charset:
                charset = charset.strip().split(';')[0]
                # print('Charset: %s' % charset)
                data = data.decode(charset)
            content = data
    return content, attachment_files


# Setting mail_address, password, pop3 server, ssl_port and attachment save path
mail_addr = 'xxx@yyy.com'
password = 'xx'
pop3_server = 'yyy.com'
ssl_port = 995
base_save_path = 'your_save_path'
debug_level = 0

# Setting the information of server
server = poplib.POP3_SSL(pop3_server, ssl_port)
server.set_debuglevel(debug_level)
print(server.getwelcome().decode('utf-8'))

# Login
server.user(mail_addr)
server.pass_(password)

# stat() returns the number of mails and space
print('Messages: %s. Size: %s' % server.stat())
# list() returns all ids of the mails
resp, mails, octets = server.list()
# print(mails)

# Get the newest (last) mail
index = len(mails)
resp, lines, octets = server.retr(index)

# Get the raw text of mail
msg_content = b'\r\n'.join(lines).decode('utf-8')
# Parse the mail
msg = Parser().parsestr(msg_content)
msg_headers = get_email_headers(msg)
print(msg_headers)
# Download the attachments
content, attachment_files = get_email_content(msg, base_save_path)
print(content)

# Quit the mailbox
server.quit()
