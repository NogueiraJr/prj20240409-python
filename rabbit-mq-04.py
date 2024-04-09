from amqpstorm import Connection

# Estabelece a conexão com o RabbitMQ
connection = Connection('localhost', 'guest', 'guest', port = 15672)
channel = connection.channel()

# Declara a fila
channel.queue.declare('minha_fila')

# Publica uma mensagem
channel.basic.publish('',
                      'minha_fila',
                      'Olá, RabbitMQ!')

print(" [x] Mensagem enviada")

# Registra o consumidor na fila
for message in channel.basic.consume('minha_fila'):
    print(" [x] Mensagem recebida:", message.body.decode())
    message.ack()

# Fecha a conexão
connection.close()
