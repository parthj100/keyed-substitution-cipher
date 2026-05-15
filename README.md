# Keyed Substitution Cipher

A single-file HTML tool for encrypting and decrypting text with a keyed substitution cipher.

## Usage

**Browser:** open `Keyed Substitution Cipher.html` in any modern browser. No build step, no dependencies.

**Python CLI:**

```sh
python3 cipher.py CIPHER "Hello World"      # Bejjm Wmqjh
python3 cipher.py -d CIPHER "Bejjm Wmqjh"   # Hello World
echo "Hello World" | python3 cipher.py CIPHER
```

Or import it:

```python
from cipher import encrypt, decrypt
encrypt("Hello World", "CIPHER")  # 'Bejjm Wmqjh'
```

## How it works

The key (deduplicated, letters only) becomes the start of the cipher alphabet; the remaining A–Z letters fill the rest in order. Each plaintext letter maps to the cipher letter directly below it.

Example with key `CIPHER`:

```
Plain:  A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
Cipher: C I P H E R A B D F G J K L M N O Q S T U V W X Y Z
```

- Non-letters pass through unchanged
- Case is preserved
- Encrypt/decrypt toggle with a single click
- Swap input/output to round-trip

## Features

- Live alphabet mapping visualization (key portion highlighted)
- Encrypt and decrypt modes
- Swap, copy, and clear actions
- Light and dark mode (follows system)
