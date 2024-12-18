import qrcode

def generate_qr_code(url, filename='qr_code.png'):
    # Create a QR Code instance
    qr = qrcode.QRCode(
        version=1,  # controls the size of the QR Code
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # controls the error correction used for the QR Code
        box_size=10,  # controls how many pixels each “box” of the QR code is
        border=4,  # controls how many boxes thick the border should be
    )
    
    # Add the URL to the QR Code
    qr.add_data(url)
    qr.make(fit=True)

    # Create an image from the QR Code instance
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the image to a file
    img.save(filename)
    print(f"QR Code generated and saved as {filename}")

if __name__ == "__main__":
    # Prompt the user for a URL
    url = input("Enter the URL to generate a QR code:https://www.blackbox.ai/chat/expert-python ")
    generate_qr_code(url)