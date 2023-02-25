import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "7165358")

API_HASH = os.environ.get("API_HASH", "304228f1dc7b9c86ef1c8d83cdc5da85")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6144893657:AAFtyY6jWx_-m7dYwNZgrAPfFmZhZIsVZ7I") 

FORCE_SUB = os.environ.get("FORCE_SUB", "") 

DB_NAME = os.environ.get("DB_NAME","kuski support")     

DB_URL = os.environ.get("DB_URL","https://t.me/+Tr51Cs7pcNdjNDUx")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://telegra.ph/file/19467bbc490900f8a29ba.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '5347606696').split()]

PORT = os.environ.get('PORT', '8080')
