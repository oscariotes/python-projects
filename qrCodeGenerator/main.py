import qrcode

class QRCode:
    def __init__(self, data):
        self.data = data
        
        self.qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        
            
        self.qr.add_data(self.data)
        self.qr.make(fit=True)
        self.qr.make_image(fill_color="black", back_color="white")  # Use 'self.qr' instead of 'qr'
        self.img.save("qrcode.png")
        print("QR code created successfully.")

def main():
    user_input = input("Enter data to encode: ")
    qr = QRCode(user_input)


if __name__ == "__main__":
    main()