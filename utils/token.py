import jwt
from datetime import datetime, timedelta
from trello import settings

from rest_framework_simplejwt.tokens import RefreshToken

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

def create_access_token(user_id):
    # Define the expiration time for the token
    expiration_time = datetime.utcnow() + timedelta(hours=1)

    # Define the payload data for the token
    payload = {
        "sub": str(user_id),
        "exp": expiration_time
    }
    
    # Generate the token
    access_token = jwt.encode(payload,  settings.SECRET_KEY, algorithm='HS256')

    return access_token
