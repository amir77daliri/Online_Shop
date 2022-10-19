import time
import uuid
import redis
from kavenegar import *
import random
from decouple import config

redis = redis.Redis(host='127.0.0.1', port=6379)


def _generate_code():
    random_code = random.randint(1000, 99999)
    return random_code


def add_code_to_redis(phone_number):
    code = _generate_code()
    redis.set(name=f'register-{phone_number}', value=code, ex=180)
    return code


def get_code_from_redis(phone_number):
    code = redis.get(name=f'register-{phone_number}')
    return code


def delete_code_from_redis(phone_number):
    redis.delete(f'register-{phone_number}')


def send_otp_code(phone_number):
    code = add_code_to_redis(phone_number)
    try:
        api = KavenegarAPI(config('KAVENEGAR_KEY'))
        params = {
            'sender': '',
            'receptor': phone_number,
            'message': f'{code} کد تایید شما:'
        }
        response = api.sms_send(params)
    except APIException as e:
        print(e)
    except HTTPException as e:
        print(e)
    return True
