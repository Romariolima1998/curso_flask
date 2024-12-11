from flask import Flask, render_template
from flask_mail import Mail, Message

config = {
    'MAIL_SERVER':'smtp.ethereal.email',
    'MAIL_PORT':587,
    'MAIL_USE_TLS':True,
    'MAIL_DEBUG':True,
    'MAIL_USERNAME':'brandyn.schneider4@ethereal.email',
    'MAIL_PASSWORD':'TJJd6gfRV4EDSqnkbN',
    'MAIL_DEFAULT_SENDER':'brandyn.schneider4@ethereal.email',

}

app = Flask(__name__)
app.config.update(config)
mail = Mail(app)


@app.route('/sendmail')
def sendmail():
    message = Message(subject='Bem vindo',
                       sender=config.get('MAIL_DEFAULT_SENDER'),
                         recipients=['romariolima1006@gmail.com', 'nedra.connelly23@ethereal.email'],
                         html=render_template('email.html') )
    
    mail.send(message)
    return 'email enviado com sucesso'

if __name__ == '__main__':
    app.run(debug=True, port=8000)