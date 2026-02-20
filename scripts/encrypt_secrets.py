#!/usr/bin/env python3
"""Encrypt secrets for the Ghost Team skill store.

Usage:
  python3 encrypt_secrets.py <secrets.json> <output.enc.json>

Reads GHOSTTEAM_MASTER_KEY from environment or ~/.secrets/ghostteam_master_key
"""
import json, sys, os, base64, hashlib
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

def get_master_key():
    key = os.environ.get("GHOSTTEAM_MASTER_KEY")
    if not key:
        paths = [
            os.path.expanduser("~/.openclaw/workspace/.secrets/ghostteam_master_key"),
            os.path.expanduser("~/.secrets/ghostteam_master_key"),
        ]
        for p in paths:
            if os.path.exists(p):
                key = open(p).read().strip()
                break
    if not key:
        print("Error: GHOSTTEAM_MASTER_KEY not found", file=sys.stderr)
        sys.exit(1)
    return hashlib.sha256(key.encode()).digest()

def encrypt_value(key_bytes, plaintext):
    aesgcm = AESGCM(key_bytes)
    nonce = os.urandom(12)
    ct = aesgcm.encrypt(nonce, plaintext.encode(), None)
    return base64.b64encode(nonce + ct).decode()

def main():
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <secrets.json> <output.enc.json>")
        sys.exit(1)

    key = get_master_key()
    secrets = json.load(open(sys.argv[1]))
    encrypted = {}
    for k, v in secrets.items():
        encrypted[k] = encrypt_value(key, v)
        print(f"  Encrypted: {k}")

    with open(sys.argv[2], "w") as f:
        json.dump(encrypted, f, indent=2)
    print(f"Written to {sys.argv[2]}")

if __name__ == "__main__":
    main()
