'''
Created on 04 Mar 2013

@author: michael
'''
from django.conf import settings
from django.contrib.sites.models import Site
from django.utils import timezone  # noqa
from django.utils.http import int_to_base36
from django.contrib.auth.tokens import default_token_generator
from django.template.loader import render_to_string

from unobase import utils as unobase_utils
from guinnessnigeria import utils


def email_account_activation(registration_profile_id, site_id):
    from authentication import models as auth_models
    registration_profile = auth_models.ProjectRegistrationProfile.objects.get(
        pk=registration_profile_id)
    site = Site.objects.get(pk=site_id)

    ctx_dict = {'user': registration_profile.user,
                'activation_key': registration_profile.activation_key,
                'expiration_days': settings.ACCOUNT_ACTIVATION_DAYS,
                'site': site,
                'app_name': settings.APP_NAME}

    # Email subject *must not* contain newlines
    subject = ''.join(render_to_string(
        'registration/activation_email_subject.txt', ctx_dict).splitlines())

    text_content = render_to_string('registration/activation_email.txt',
                                    ctx_dict)

    unobase_utils.send_mail(
        'registration/activation_email.html',
        ctx_dict,
        subject,
        text_content,
        settings.DEFAULT_FROM_EMAIL,
        [registration_profile.user.email, ]
    )


def email_successful_account_activation(user_id):
    from authentication.user import models as auth_user_models
    user = auth_user_models.User.objects.get(pk=user_id)

    ctx_dict = unobase_utils.get_email_context(user)

    ctx_dict.update({'uid': int_to_base36(user.id),
                     'token': default_token_generator.make_token(user)})

    subject = unobase_utils.get_email_subject(
        'guinnessnigeria/email/subjects/successful_account_activation_subject.txt',
        ctx_dict
    )

    text_content = unobase_utils.get_email_text_content(
        'guinnessnigeria/email/txt/successful_account_activation.txt',
        ctx_dict
    )

    unobase_utils.send_mail(
        'guinnessnigeria/email/html/successful_account_activation.html',
        ctx_dict,
        subject,
        text_content,
        settings.DEFAULT_FROM_EMAIL,
        [user.email, ],
        user=user
    )


def email_contact_message(from_email, name, contact_number, subject, message):
    content = utils.prepare_email_content(
        template_name='email/contact_message.html',
        data={
            'email': from_email,
            'name': name,
            'contact_number': contact_number,
            'subject': subject,
            'message': message
        }
    )

    utils.send_email(
            '[Guinness NCW]: ' + subject,
            content,
            settings.GUINNESS_NCW['email_recipients']['contact_form'],
            cc=[],
            files=[],
    )
