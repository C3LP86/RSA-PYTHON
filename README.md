# RSA-PYTHON

# 🔐 Implémentation de RSA en Python

Ce projet implémente le chiffrement **RSA** en Python, avec des fonctionnalités de :
- 🔑 **Génération de clés RSA** (publique et privée)
- 🔒 **Chiffrement et déchiffrement** d'un message
- ✍️ **Signature numérique et vérification**
- 🛡 **Protection contre la falsification des messages**

## 🚀 Comment l'utiliser ?

1. **Installation** (Python 3 requis)
   ```bash
   git clone https://github.com/VotreNomUtilisateur/RSA-PYTHON.git
   cd RSA-PYTHON
   python3 rsa.py
   ```

2. **Installation** (Python 3 requis)
   ```bash
   🔑 Clé publique : (e=65537, n=...)
   🔐 Clé privée : (d=..., n=...)
   🧩 Taille de n : 2048 bits

   🔒 Message chiffré : 128938127391283
   ✅ Succès : Le message original est retrouvé.
   🔑 Message déchiffré : Hello World !

   ✍️ Signature générée : 728371982739182
   ✅ Signature valide : le message est authentique.
   ❌ Signature invalide : le message a été altéré !
   ```

# ⚠️ Note

Ce projet est éducatif. Pour des applications réelles, utilisez PyCryptodome ou OpenSSL.
