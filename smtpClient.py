from socket import *

def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\nMy message"
    endmsg = "\r\n.\r\n"

    # Create socket called clientSocket and establish a TCP connection with mailserver and port
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailserver, port))

    recv = clientSocket.recv(1024).decode()
    if recv[:3] != '220':
        print('220 reply not received from server.')

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    if recv1[:3] != '250':
        print('250 reply not received from server.')

    # Send MAIL FROM command and handle server response.
    mailFrom = 'MAIL FROM:<jk8063@nyu.edu>\r\n'  # Replace with your email
    clientSocket.send(mailFrom.encode())
    recv2 = clientSocket.recv(1024).decode()
    if recv2[:3] != '250':
        print('250 reply not received from server.')

    # Send RCPT TO command and handle server response.
    rcptTo = 'RCPT TO:<receiver2024@gmail.com>\r\n'  # Replace with recipient email
    clientSocket.send(rcptTo.encode())
    recv3 = clientSocket.recv(1024).decode()
    if recv3[:3] != '250':
        print('250 reply not received from server.')

    # Send DATA command and handle server response.
    dataCommand = 'DATA\r\n'
    clientSocket.send(dataCommand.encode())
    recv4 = clientSocket.recv(1024).decode()
    if recv4[:3] != '354':
        print('354 reply not received from server.')

    # Send message data.
    clientSocket.send(msg.encode())

    # Message ends with a single period, send message end and handle server response.
    clientSocket.send(endmsg.encode())
    recv5 = clientSocket.recv(1024).decode()
    if recv5[:3] != '250':
        print('250 reply not received from server.')

    # Send QUIT command and handle server response.
    quitCommand = 'QUIT\r\n'
    clientSocket.send(quitCommand.encode())
    recv6 = clientSocket.recv(1024).decode()
    if recv6[:3] != '221':
        print('221 reply not received from server.')

    clientSocket.close()


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')
