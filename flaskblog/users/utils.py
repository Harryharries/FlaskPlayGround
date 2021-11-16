import os
import secrets
from PIL import Image
from flaskblog import mail
from flask import current_app
from flask_mail import Message



def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    f_name, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, 'static/profile_pics', picture_fn)
    form_picture.save(picture_path)

    output_size = (125,125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)

    i.save(picture_path)

    return picture_fn


def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password Reset Request', sender='a1021604754@gmail.com',recipients=[user.email])
    msg.body = ''' Toreset your password, :
    {url_for('reset_token', token=token, _external=True)}

    test!!!
    '''
    mail.send(msg)