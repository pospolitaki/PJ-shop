import requests

from allauth.socialaccount.providers.oauth2.views import (
    OAuth2Adapter,
    OAuth2CallbackView,
    OAuth2LoginView,
)

from .provider import DropboxOAuth2Provider


class DropboxOAuth2Adapter(OAuth2Adapter):
    provider_id = DropboxOAuth2Provider.id
    access_token_url = 'https://api.dropbox.com/oauth2/token'
    authorize_url = 'https://www.dropbox.com/oauth2/authorize'
    profile_url = 'https://api.dropbox.com/2/users/get_current_account'
    redirect_uri_protocol = 'https'

    def complete_login(self, request, app, token, **kwargs):
        extra_data = requests.post(self.profile_url, headers={
            'Authorization': 'Bearer %s' % (token.token, )
        })

        # This only here because of weird response from the test suite
        if isinstance(extra_data, list):
            extra_data = extra_data[0]

        return self.get_provider().sociallogin_from_response(
            request,
            extra_data.json()
        )


oauth_login = OAuth2LoginView.adapter_view(DropboxOAuth2Adapter)
oauth_callback = OAuth2CallbackView.adapter_view(DropboxOAuth2Adapter)
