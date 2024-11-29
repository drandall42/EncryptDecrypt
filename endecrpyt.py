import argparse
from crypto_utils import (
    generate_key,
    encrypt_message,
    decrypt_message,
    encrypt_file,
    decrypt_file,
)


# Set up the argument parser
CryptoArg = argparse.ArgumentParser(
    description="Encrypt or decrypt messages/files using the cryptography module."
)

# Subcommands: Encrypt and Decrypt
subparsers = CryptoArg.add_subparsers(dest="command", required=True, help="Sub-command to run")

# Encrypt arguments
encrypt_parser = subparsers.add_parser("encrypt", help="Encrypt a message or file")
encrypt_parser.add_argument(
    "-message",
    type=str,
    help="The plaintext message to encrypt"
)
encrypt_parser.add_argument(
    "-file",
    type=str,
    help="Path to the file to encrypt"
)
encrypt_parser.add_argument(
    "-key",
    type=str,
    help="Encryption key (optional, will be generated if not provided)"
)
encrypt_parser.add_argument(
    "-key_output",
    type=str,
    help="File to save the encryption key (optional)"
)
encrypt_parser.add_argument(
    "-output",
    type=str,
    required=True,
    help="File to save the encrypted output"
)

# Decrypt arguments
decrypt_parser = subparsers.add_parser("decrypt", help="Decrypt a message or file")
decrypt_parser.add_argument(
    "-file",
    type=str,
    required=True,
    help="Path to the encrypted file"
)
decrypt_parser.add_argument(
    "-key",
    type=str,
    required=True,
    help="Decryption key"
)
decrypt_parser.add_argument(
    "-output",
    type=str,
    help="File to save the decrypted output"
)

# Parse arguments
args = CryptoArg.parse_args()


# Encryption logic
if args.command == "encrypt":
    if not (args.message or args.file):
        print("Error: You must provide either -message or -file for encryption.")
    else:
        # Generate a key if not provided
        key = args.key.encode() if args.key else generate_key()

        # Encrypt the input
        if args.message:
            encrypted_data = encrypt_message(key, args.message)
        else:
            encrypted_data = encrypt_file(key, args.file)

        # Save the encrypted data
        with open(args.output, "wb") as file:
            file.write(encrypted_data)
        print(f"Encrypted data saved to {args.output}")

        # Save the key if requested
        if args.key_output:
            with open(args.key_output, "w") as key_file:
                key_file.write(key.decode())
            print(f"Encryption key saved to {args.key_output}")
        else:
            print(f"Generated Key: {key.decode()} (Save this key for decryption)")

# Decryption logic
elif args.command == "decrypt":
    try:
        # Decrypt the file
        decrypted_data = decrypt_file(args.key.encode(), args.file)

        if args.output:
            # Save decrypted content to a file
            with open(args.output, "wb") as file:
                file.write(decrypted_data)
            print(f"Decrypted content saved to {args.output}")
        else:
            # Print the decrypted content
            print("Decrypted content:")
            print(decrypted_data.decode())
    except Exception as e:
        print(f"Error during decryption: {e}")
