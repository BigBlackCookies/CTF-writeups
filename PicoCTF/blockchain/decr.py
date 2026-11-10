#!/usr/bin/env python3
"""
decr_fixed.py

Usage:
  python3 decr_fixed.py [enc_flag.txt]

Expects a text file containing lines like:
  Key: b'...'
  Encrypted Blockchain: b'...'
(the byte-literals may be long / span display-wrapped lines)

This script extracts the exact byte-literals and decrypts them using the
same XOR-with-SHA256(key) per-16-byte-block scheme used in the original.
It then safely unpads and prints the decrypted content and any picoCTF flag found.
"""

import sys, ast, hashlib, re

def xor_bytes(a: bytes, b: bytes) -> bytes:
    return bytes(x ^ y for x, y in zip(a, b))

def safe_unpad(data: bytes) -> bytes:
    if not data:
        return data
    pad_len = data[-1]
    if 1 <= pad_len <= 16 and data.endswith(bytes([pad_len]) * pad_len):
        return data[:-pad_len]
    return data

def decrypt_ciphertext(encrypted: bytes, key_bytes: bytes) -> bytes:
    key_hash = hashlib.sha256(key_bytes).digest()
    decrypted = b''
    block_size = 16
    for i in range(0, len(encrypted), block_size):
        block = encrypted[i:i+block_size]
        decrypted_block = xor_bytes(block, key_hash[:len(block)])
        decrypted += decrypted_block
    return decrypted

def parse_file(path: str):
    txt = open(path, "r", encoding="utf-8", errors="replace").read()

    # Find the positions of the markers
    kpos = txt.find("Key:")
    epos = txt.find("Encrypted Blockchain:")

    if kpos == -1 or epos == -1:
        raise SystemExit("File must contain 'Key:' and 'Encrypted Blockchain:' markers")

    # Extract the substring that should contain the key literal (between Key: and Encrypted Blockchain:)
    key_sub = txt[kpos + len("Key:"):epos].strip()
    enc_sub = txt[epos + len("Encrypted Blockchain:"):].strip()

    # Remove any leading/trailing text that isn't part of the literal.
    # At this point key_sub should start with b' or b"
    # and enc_sub should start with b' or b"
    # Use ast.literal_eval which safely parses Python literals.
    try:
        key_bytes = ast.literal_eval(key_sub)
    except Exception as ex:
        raise SystemExit(f"Failed to parse Key literal: {ex}")

    try:
        encrypted_bytes = ast.literal_eval(enc_sub)
    except Exception as ex:
        raise SystemExit(f"Failed to parse Encrypted Blockchain literal: {ex}")

    if not isinstance(key_bytes, (bytes, bytearray)) or not isinstance(encrypted_bytes, (bytes, bytearray)):
        raise SystemExit("Parsed values are not byte literals")

    return bytes(key_bytes), bytes(encrypted_bytes)

def extract_flag(txt: str):
    m = re.search(r"picoCTF\{.*?\}", txt)
    return m.group(0) if m else None

def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "enc_flag"
    key_bytes, encrypted_bytes = parse_file(path)

    decrypted = decrypt_ciphertext(encrypted_bytes, key_bytes)
    unpadded = safe_unpad(decrypted)
    text = unpadded.decode("utf-8", errors="replace")

    print("---- Decrypted text (first 2000 chars) ----")
    print(text[:2000])
    print("---- End ----\n")

    flag = extract_flag(text)
    if flag:
        print("[+] Found flag:", flag)
    else:
        print("[-] No picoCTF{...} found. If output looks wrong, ensure the input file is exactly the file produced by the encrypt script.")

if __name__ == "__main__":
    main()
