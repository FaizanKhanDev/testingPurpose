from django.urls import reverse_lazy

ACCOUNT_AUTHENTICATION_METHOD = "username_email"

ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = reverse_lazy("index")

ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = reverse_lazy(
    "index"
)

ACCOUNT_EMAIL_MAX_LENGTH = 40

ACCOUNT_EMAIL_REQUIRED = True

ACCOUNT_EMAIL_VERIFICATION = ["none", "mandatory", "optional"][1]

ACCOUNT_LOGIN_ATTEMPTS_LIMIT = 3

ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT = 900  # 15 minutes

ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True

ACCOUNT_LOGOUT_ON_PASSWORD_CHANGE = True

ACCOUNT_LOGOUT_REDIRECT_URL = reverse_lazy("index")

ACCOUNT_PRESERVE_USERNAME_CASING = False

ACCOUNT_SESSION_REMEMBER = True

ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = True

ACCOUNT_SIGNUP_REDIRECT_URL = reverse_lazy("index")

ACCOUNT_UNIQUE_EMAIL = True

ACCOUNT_USERNAME_MIN_LENGTH = 5

ACCOUNT_USERNAME_REQUIRED = False

ACCOUNT_USER_MODEL_USERNAME_FIELD = "username"

# https://django-allauth.readthedocs.io/en/latest/configuration.html
ACCOUNT_ADAPTER = "Users.adapters.AccountAdapter"
# https://django-allauth.readthedocs.io/en/latest/configuration.html
SOCIALACCOUNT_ADAPTER = "Users.adapters.SocialAccountAdapter"
# https://django-allauth.readthedocs.io/en/latest/forms.html
# SOCIALACCOUNT_FORMS = {"signup": "Users.forms.UserSocialSignupForm"}
SOCIALACCOUNT_AUTO_SIGNUP = True
SOCIALACCOUNT_EMAIL_VERIFICATION = ACCOUNT_EMAIL_VERIFICATION[0]

SITE_ID = 1

# Provider specific settings
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        },
        'OAUTH_PKCE_ENABLED': True,

    },

    'facebook': {
        'METHOD': 'oauth2',
        'SDK_URL': '//connect.facebook.net/{locale}/sdk.js',
        'SCOPE': ['email', 'public_profile'],
        'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
        'INIT_PARAMS': {'cookie': True},
        'FIELDS': [
            'id',
            'first_name',
            'last_name',
            'middle_name',
            'name',
            'name_format',
            'picture',
            'short_name'
        ],
        'EXCHANGE_TOKEN': True,
        'LOCALE_FUNC': 'en_US',
        'VERIFIED_EMAIL': True,
        'VERSION': 'v13.0',
        'GRAPH_API_URL': 'https://graph.facebook.com/v13.0',
}
}


def ACCOUNT_USER_DISPLAY(user):
    """
    Override the default All auth display
    """
    return user.get_full_name() or user.email
