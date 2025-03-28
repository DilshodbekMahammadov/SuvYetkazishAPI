from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer
from .models import *

class SuvSerializer(ModelSerializer):
    class Meta:
        model = Suv
        fields = '__all__'

    def validate_miqdor(value):
        max_miqdor = 19
        if value > max_miqdor:
            raise ValidationError ('Bunday katta litrlarda suv sotilmaydi!')

class MijozSerializer(ModelSerializer):
    class Meta:
        model = Mijoz
        fields = '__all__'



class AdministratorSerializer(ModelSerializer):
    class Meta:
        model = Administrator
        fields = ('id','username','password', 'ism', 'ish_vaqti')

    extra_kwargs = {
        'password': {'write_only': True}
    }

    def validate_yosh(value):
        min_yosh = 19
        if value < min_yosh:
            raise ValidationError ('Yoshingiz mos kelmaydi!')

class BuyurtmaSerializer(ModelSerializer):
    class Meta:
        model = Buyurtma
        fields = '__all__'

    def validate_qarz(value):
        max_qarz = 500000
        if value > max_qarz:
            raise ValidationError('Qarzingiz juda ko’p, buyurtma qilolmaysiz!')

class HaydovchiSerializer(ModelSerializer):
    class Meta:
        model = Haydovchi
        fields = '__all__'