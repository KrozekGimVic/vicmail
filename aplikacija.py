import smtplib
from bottle import route, run, template, request, static_file
from email.message import EmailMessage

@route('/')
def index():
    return template('index')

@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='static/')

@route('/greet/')
def pozdrav():
    firstname = request.query.fname
    lastname = request.query.lname
    if not lastname:
        sporocilo = ''
    elif not firstname:
        sporocilo = 'družina ' + lastname
    else: 
        sporocilo = firstname + ' ' + lastname
    return template('greet', firstname=firstname, lastname=lastname, hello_msg=sporocilo)

@route('/send/')
def posta():
    return template('send_mail', message='', to='', subject='')

@route('/send/', method='POST')
def posta():
    to = request.forms.get('email')
    title = request.forms.get('naslov')
    text = request.forms.get('sporocilo')
    if not to or not text:
        return template('send_mail', message=text, to=to, subject=title)
    msg = EmailMessage()
    msg.set_content(text)
    msg['Subject'] = title
    msg['To'] = to
    msg['From'] = 'vicsender@gimvic.org'
    server = smtplib.SMTP('smtp.telemach.net')
    server.send_message(msg)
    server.quit()
    return 'Sporocilo uspesno poslano!'

run(host='localhost', reloader=True, port=8080)