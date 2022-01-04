import string
import random
import query
import psycopg2

def connection():

    connection_str = "host=0.0.0.0 port=5438 dbname=flask_crud_db user=davi password=davi"  # noqa: E501
    return psycopg2.connect(connection_str)

def popula_banco():
    base = string.digits + "abcdefABCDEF"
    for i in range(5000):
        a, b, c, d = '', '', '', ''
        for _ in range(20):
            a += random.choice(base)
            b += random.choice(base)
            c += random.choice(base)
            d += random.choice(base)
        descricaocompleta = a
        descricaoreduzida = b
        unidade = 'UN'
        precovenda = random.uniform(0, 5000)
        estoque = random.randint(0,5000)
        codigobarras = random.uniform(0, 5000)
        mercadologico1 = str(random.randint(0,5000))
        descricaomercadologico = d

        query.insert_in_client_table(connection(), descricaocompleta, estoque, unidade, descricaoreduzida)
    print('é isso.')

popula_banco()

