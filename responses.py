import requests
import json

def get_response(message: str) -> str:
  p_message = message.lower()

  if p_message == 'hola':
    return 'Saludos!'

  if p_message == 'help':
    return '''`!hola  --  para recibir un cordial saludo
!crypto  --  añade tras un espacio las siglas de la cryptomonenda que quieras saber si precio actual (ejemplo: "!crypto btc" para el precio del Bitcoin)
`'''

  if p_message.startswith('crypto'):
    coin_name = p_message.split(' ')[-1].upper()
    response = requests.get('https://data.binance.com/api/v3/avgPrice', params = {'symbol' : f'{coin_name}USDT'}).text
    jason_text = json.loads(response)
    if 'price' in jason_text:
      price = jason_text["price"]
      return (f'{coin_name} tiene un valor de {float(price):.2f}$')
    return (f"No he encontrado tu moneda.")    

  return (f"No entiendo lo que quieres decir con '{p_message}'. Prueba a escribir '!help'")