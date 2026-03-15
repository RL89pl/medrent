import base64
import requests
from django.conf import settings


def _emaillabs_post(data):
    app_key = settings.EMAILLABS_APP_KEY + ':' + settings.EMAILLABS_SECRET_KEY
    auth_header = 'Basic ' + str(base64.b64encode(app_key.encode('utf-8')), 'utf-8')
    try:
        r = requests.post(
            'https://api.emaillabs.net.pl/api/new_sendmail',
            headers={'Authorization': auth_header},
            data=data,
            timeout=10,
        )
        return r
    except Exception:
        pass


def send_contact_notification(message):
    """Wysyła powiadomienie do admina o nowej wiadomości kontaktowej."""
    from .models import SiteSettings
    site = SiteSettings.get()
    admin_email = site.contact_email

    product_info = f'<p><b>Produkt:</b> {message.product.name}</p>' if message.product else ''

    html = f"""
    <div style="font-family:sans-serif;max-width:600px;margin:0 auto;padding:24px">
      <h2 style="color:#1fa896;margin-bottom:16px">Nowa wiadomość kontaktowa – LUMA</h2>
      <p><b>Imię i nazwisko:</b> {message.name}</p>
      <p><b>Email:</b> {message.email}</p>
      <p><b>Telefon:</b> {message.phone or '—'}</p>
      {product_info}
      <p style="margin-top:16px"><b>Wiadomość:</b></p>
      <p style="background:#f5f8f8;padding:12px;border-radius:6px">{message.message}</p>
      <p style="color:#888;font-size:12px;margin-top:24px">
        Wiadomość z formularza kontaktowego na stronie LUMA.
      </p>
    </div>
    """

    _emaillabs_post({
        f'to[{admin_email}]': '',
        'smtp_account': settings.EMAILLABS_SMTP,
        'subject': f'Nowa wiadomość: {message.name}',
        'html': html,
        'from': admin_email,
        'from_name': 'LUMA – formularz kontaktowy',
    })
