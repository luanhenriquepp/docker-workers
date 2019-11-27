import redis
import json
from time import sleep
from random import randint
import os

if __name__ == '__main__':
    redis_host = os.getenv('REDIS_HOST', 'queue')
    redis_port = os.getenv('REDIS_PORT', 6379)
    redis_db = os.getenv('REDIS_DB', 0)    r = redis.Redis(host=redis_host, port=redis_port, db=redis_db)
    print('Aguardando mensagens.....')
    while True:
        mensagem = json.loads(r.blpop('sender')[1])
        
        # Simulando envio de e-mail....
        print('Mudando a mensagem:', mensagem['assunto'])
        sleep(randint(15, 45))
        print('Mensagem', mensagem['assunto'], 'enviada')