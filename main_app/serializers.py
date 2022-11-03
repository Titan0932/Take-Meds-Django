from rest_framework import serializers
from main_app.models import EnterMeds,EnterInfo

class UserMeds(serializers.ModelSerializer):

    message=serializers.SerializerMethodField()

    class Meta:
        model=EnterMeds

        fields=['uid', 'medName', 'amount', 'inStore','remarks','active']
        read_only_fields=['uid']


class UserInfo(serializers.ModelSerializer):

    """ message=serializers.SerializerMethodField() """

    class Meta:
        model=EnterInfo

        fields='__all__'

        permissions = (
            ("home", "myMeds"),
            ("profile"),
        )

    def validate_password(self, p1,p2):
        if p1!=p2:
            return 'Passwords do not Match!!'

        return False
       
        

        