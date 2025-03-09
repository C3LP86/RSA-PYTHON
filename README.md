# RSA-PYTHON

# 🔐 Implémentation de RSA en Python

Ce projet implémente le chiffrement **RSA** en Python, avec les fonctionnalités suivantes :
- 🔑 **Génération de clés RSA** (publique et privée)
- 🔒 **Chiffrement et déchiffrement** de messages
- ✍️ **Signature numérique et vérification**
- 🛡 **Protection contre la falsification des messages**

## 📌 Comment fonctionne RSA ?

RSA repose sur des principes mathématiques solides en utilisant des **nombres premiers** et l’**arithmétique modulaire**.

| **Symbole** | **Définition** |
|------------|--------------|
| **\( p, q \)** | Deux grands **nombres premiers** générés aléatoirement. |
| **\( n \)** | Le **modulus**, utilisé pour le chiffrement et la signature. \( n = p * q \). |
| **\( φ(n) \)** | **Fonction d’Euler**, utilisée pour calculer \( d \). \( φ(n) = (p - 1) * (q - 1) \). |
| **\( e \)** | **Exposant public**, souvent fixé à **65537**. |
| **\( d \)** | **Exposant privé**, inverse modulaire de \( e \) mod \( φ(n) \). C'est la clé secrète. |

### 🔐 **Formules utilisées dans RSA :**

- **Chiffrement :**  
  \( C = M^e \mod n \)
- **Déchiffrement :**  
  \( M = C^d \mod n \)
- **Signature numérique :**  
  \( S = H(M)^d \mod n \)
- **Vérification de la signature :**  
  \( V = S^e \mod n \)

## 📥 Installation

1. **Cloner le projet :**
   ```bash
   git clone https://github.com/VotreNomUtilisateur/RSA-Python.git
   cd RSA-Python
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
