from os import environ

# Telegram Account Api Id And Api Hash
API_ID = int(environ.get("API_ID", "29257881"))
API_HASH = environ.get("API_HASH", "3dd9f4e0716871e4b507f9411fd1ee8b")

# Your Main Bot Token 
BOT_TOKEN = environ.get("BOT_TOKEN", "")

# Owner ID For Broadcasting 
OWNER_ID = int(environ.get("OWNER_ID", "7891840370")) # Owner Id or Admin Id

# Give Your Force Subscribe Channel Id Below And Make Bot Admin With Full Right.
F_SUB = environ.get("F_SUB", "1002269263619")

# Mongodb Database Uri For User Data Store 
MONGO_DB_URI = environ.get("MONGO_DB_URI", "mongodb+srv://jodhpurijaipal:<VcnO04jGoxVjbjeJ>@cluster0.7viuwzj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

# Port To Run Web Application 
PORT = int(environ.get('PORT', 8080))
