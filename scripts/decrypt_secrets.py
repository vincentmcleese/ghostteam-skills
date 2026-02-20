#!/usr/bin/env python3
"""Decrypt secrets for agent use.

Usage:
  python3 decrypt_secrets.py <secrets.enc.json> [key1 key2 ...]

If keys specified, only decrypts those. Otherwise decrypts all.
Reads GHOSTTEAM_MASTER_KEY from environment or ~/.secrets/ghostteam_master_key
Outputs JSON to stdout.
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

def decrypt_value(key_bytes, ciphertext_b64):
    raw = base64.b64decode(ciphertext_b64)
    nonce, ct = raw[:12], raw[12:]
    aesgcm = AESGCM(key_bytes)
    return aesgcm.decrypt(nonce, ct, None).decode()

def main():
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <secrets.enc.json> [key1 key2 ...]")
        sys.exit(1)

    key = get_master_key()
    encrypted = json.load(open(sys.argv[1]))
    filter_keys = sys.argv[2:] if len(sys.argv) > 2 else list(encrypted.keys())

    result = {}
    for k in filter_keys:
        if k in encrypted:
            result[k] = decrypt_value(key, encrypted[k])

    json.dump(result, sys.stdout, indent=2)
    print()

if __name__ == "__main__":
    main()
