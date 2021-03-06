# -*- coding: utf-8 -*-

from .addon import ADDON_MAPPING
from .certificate import CERTIFICATE_MAPPING
from .cloud_user import CLOUD_USER_MAPPING
from .database import DATABASE_MAPPING
from .domain import DOMAIN_MAPPING
from .domain_configuration import DOMAIN_CONFIGURATION_MAPPING
from .domain_record import DOMAIN_RECORD_MAPPING
from .email import EMAIL_MAPPING
from .email_account import EMAIL_ACCOUNT_MAPPING
from .email_account_autoreply import EMAIL_ACCOUNT_AUTOREPLY_MAPPING
from .email_group import EMAIL_GROUP_MAPPING
from .migration import MIGRATION_MAPPING
from .website import WEBSITE_MAPPING
from .website_cron import WEBSITE_CRON_MAPPING

RESOURCE_MAPPING = {}
RESOURCE_MAPPING.update(ADDON_MAPPING)
RESOURCE_MAPPING.update(CERTIFICATE_MAPPING)
RESOURCE_MAPPING.update(CLOUD_USER_MAPPING)
RESOURCE_MAPPING.update(DATABASE_MAPPING)
RESOURCE_MAPPING.update(DOMAIN_MAPPING)
RESOURCE_MAPPING.update(DOMAIN_CONFIGURATION_MAPPING)
RESOURCE_MAPPING.update(DOMAIN_RECORD_MAPPING)
RESOURCE_MAPPING.update(EMAIL_MAPPING)
RESOURCE_MAPPING.update(EMAIL_ACCOUNT_MAPPING)
RESOURCE_MAPPING.update(EMAIL_ACCOUNT_AUTOREPLY_MAPPING)
RESOURCE_MAPPING.update(EMAIL_GROUP_MAPPING)
RESOURCE_MAPPING.update(MIGRATION_MAPPING)
RESOURCE_MAPPING.update(WEBSITE_MAPPING)
RESOURCE_MAPPING.update(WEBSITE_CRON_MAPPING)
