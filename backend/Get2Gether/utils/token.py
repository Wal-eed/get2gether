import jwt
from Get2Gether import SECRET_KEY 
from Get2Gether.utils.colourisation import printColoured
from typing import Dict

def generate_token(user_data: Dict[str, str]) -> str:
    """
        Generates a unique JSON web token based on the input user data.

        Args:
            user_data (dict): of shape { 
                    user_id: str,
                    email: str
                }

        Returns:
            str: the JWT web token 
    """
    payload = {
        "user_id": user_data["user_id"],
        "email": user_data["email"],
    }
    web_token = jwt.encode(payload, "TEMP SECRET", algorithm="HS256")     # TODO: Add env secret
    return web_token
