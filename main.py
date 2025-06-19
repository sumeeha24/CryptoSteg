from crypto import encrypt_message, decrypt_message
from steg import hide_data_in_image, extract_data_from_image

if __name__ == '__main__':
    print("1. Hide Message\n2. Extract Message")
    choice = input("Choose an option: ")

    if choice == '1':
        msg = input("Enter message to hide: ")
        pwd = input("Enter password: ")
        encrypted = encrypt_message(msg, pwd)
        hide_data_in_image('sample_image.png', encrypted, 'stego_image.png')
        print("Message hidden in stego_image.png")

    elif choice == '2':
        pwd = input("Enter password: ")
        encrypted = extract_data_from_image('stego_image.png')
        try:
            decrypted = decrypt_message(encrypted, pwd)
            print("Decrypted Message:", decrypted.decode())
        except:
            print("Decryption failed. Incorrect password or corrupted image.")
