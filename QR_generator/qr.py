import qrcode

data = input("Enter text or URL to generate QR code: ").strip()

if not data:
    print("Input cannot be empty!")
else:
    filename = input("Enter file name (without .png): ").strip()
    if not filename:
        filename = "qr_code"

    img = qrcode.make(data)
    img.save(f"{filename}.png")

    print(f"QR Code generated successfully as {filename}.png")
