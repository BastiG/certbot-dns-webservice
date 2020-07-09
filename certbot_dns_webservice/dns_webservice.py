"""Webservice DNS Authenticator."""
import logging

import zope.interface

from requests import get as requests_get

from certbot import errors
from certbot import interfaces
from certbot.plugins import dns_common

logger = logging.getLogger(__name__)

@zope.interface.implementer(interfaces.IAuthenticator)
@zope.interface.provider(interfaces.IPluginFactory)
class Authenticator(dns_common.DNSAuthenticator):
    """Webservice DNS Authenticator
    This Authenticator uses a webservice interface to DNS update to fulfill a dns-01 challenge.
    """

    description = ('Obtain certificates using a webservice interface to DNS update')

    def __init__(self, *args, **kwargs):
        super(Authenticator, self).__init__(*args, **kwargs)

    @classmethod
    def add_parser_arguments(cls, add):  # pylint: disable=arguments-differ
        super(Authenticator, cls).add_parser_arguments(add, default_propagation_seconds=0)
        add('url', help='Webservice URL.')
        add('credentials', help='Webservice credentials.')

    def _setup_credentials(self):
        return

    def more_info(self):  # pylint: disable=missing-docstring,no-self-use
        return 'This plugin uses a webservice interface to DNS update to respond to a dns-01 challenge.'

    def _perform(self, domain, validation_name, validation):
        url = self.conf('url') + '?hostname={}&txt={}'.format(validation_name, validation)
        username, password = self.conf('credentials').split(':')

        requests_get(url, auth=(username, password))

    def _cleanup(self, domain, validation_name, validation):
        url = self.conf('url') + '?hostname={}&txt='.format(validation_name)
        username, password = self.conf('credentials').split(':')

        requests_get(url, auth=(username, password))
