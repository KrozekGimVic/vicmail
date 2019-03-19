from bottle import route, run, template, request, static_file

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

run(host='localhost', reloader=True, port=8080)