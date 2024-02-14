from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from customer.utils import get_user


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        current_user = get_user(user)
        user_type = current_user._meta.object_name
        try:
            subscription_type = current_user.subscription_type
            if not subscription_type:
                raise Exception("no sub type")
        except:
            subscription_type = ""
        token = super().get_token(user)
        token["subscription_type"] = subscription_type
        token["user_type"] = user_type
        return token
