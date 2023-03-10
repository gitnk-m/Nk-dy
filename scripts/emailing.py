import smtplib, ssl
from email.message import EmailMessage

def mailing(name, email, msg,one,two,three,four):
    port = 465

    sender = 'justadummynk@gmail.com'
    password = 'wddkwxbirpedmvga'

    msg = EmailMessage()
    msg['Subject'] ='HTML Mail Service'
    msg['From'] = sender
    msg['To'] = 'justadummynk@gmail.com'
    msg.set_content('....Turn on HTML Mail....')

    msg.add_alternative(f'''\
        <!doctype html>
        <html lang="en">
            <body>
                <table>
                    <tr>
                        <th>Name</th>
                        <td>{name}</td>
                    </tr>
                    <tr>
                        <th>Email</th>
                        <td>{email}</td>
                    </tr>
                    <tr>
                        <th>One</th>
                        <td>{one}</td>
                    </tr>
                    <tr>
                        <th>Two</th>
                        <td>{two}</td>
                    </tr>
                    <tr>
                        <th>Three</th>
                        <td>{three}</td>
                    </tr>
                    <tr>
                        <th>Four</th>
                        <td>{four}</td>
                    </tr>
                </table>
            </body>
        </html>''', subtype='html')
    

    with smtplib.SMTP_SSL("smtp.gmail.com", port) as server:
        server.login(sender, password)
        server.send_message(msg)
