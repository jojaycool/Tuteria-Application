import time

from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template import Context
from django.template.loader import get_template
from django.utils.html import strip_tags


def send_email(subject, content, recipients, cc=[], files=[]):
    """
    Wraps django send_mail which attaches an html version of the email.
    """
    if settings.GUINNESS_NCW['is_testing']:
        testing_notice = (
            "<p>This is for testing purposes. This email would be sent to: %s</p>"
        ) % str(", ".join(recipients))
        content["text"] = testing_notice + content["text"]
        content["html"] = testing_notice + content["html"]
        recipients = settings.GUINNESS_NCW["email_recipients"]["testing"]

    message = EmailMultiAlternatives(
        subject, content["text"], settings.DEFAULT_FROM_EMAIL, recipients,
        headers={"Unique-ID": time.time()}, cc=cc
    )
    message.attach_alternative(content["html"], "text/html")
    for attachment in files:
        message.attach(*attachment)
    message.send()


def prepare_email_content(template_name, data):
    """
    A function which tries to generalise sending of models.
    """
    template = get_template(template_name)
    context = Context({"data": data})
    html_content = template.render(context)

    return {
        "html": html_content,
        "text": strip_tags(html_content)
    }
