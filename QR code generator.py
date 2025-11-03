import webbrowser

def url_encode(text):
    return ''.join('%{:02X}'.format(ord(c)) if not c.isalnum() else c for c in text)

def generate_qr_code_url(data):
    encoded_data = url_encode(data)
    return f"https://api.qrserver.com/v1/create-qr-code/?size=300x300&data={encoded_data}&format=png&ecc=L&version=2"

def main():
    user_input = input("Please enter the text or URL: ")
    if len(user_input.encode('utf-8')) > 34:
        print("Error: Max 34 bytes in binary mode (1 character = 1 byte, 1 emoji = 4 bytes).")
        return

    qr_url = generate_qr_code_url(user_input)
    print("Opening QR Code in your browser...")
    webbrowser.open(qr_url)

main()