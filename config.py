import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "7165358")

API_HASH = os.environ.get("API_HASH", "304228f1dc7b9c86ef1c8d83cdc5da85")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6205814370:AAERmsYWH4UPcKBpKZ5Jl7-j6VTR2Hj0Zls") 

FORCE_SUB = os.environ.get("FORCE_SUB", "Anime_complex") 

DB_NAME = os.environ.get("DB_NAME","kuski")     

DB_URL = os.environ.get("DB_URL","mongodb+srv://Legend54:<Legend54>@cluster0.ux9gf.mongodb.net/?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://telegra.ph/file/19467bbc490900f8a29ba.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '6014086787').split()]

PORT = os.environ.get('PORT', '8080')
