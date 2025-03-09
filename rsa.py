"""
RSA Implementation en Python 🔐
--------------------------------
✅ Génération des clés RSA (publique et privée)
✅ Chiffrement et déchiffrement de messages
✅ Signature numérique et vérification
✅ Protection contre la falsification des messages

⚠️ Ce projet est à des fins éducatives seulement.
💡 Pour une utilisation en production, utilisez une librairie éprouvée comme PyCryptodome.
"""

# 📌 Importation des librairies nécessaires
import math
import random
import hashlib
from sympy import isprime


# 📌 Génération d'un grand nombre premier
def generate_large_prime(bits=1024):
    """ Génère un nombre premier sécurisé de `bits` bits """
    while True:
        num = random.getrandbits(bits)
        if isprime(num):
            return num


# 📌 Algorithme d’Euclide étendu pour l'inverse modulaire
def extended_gcd(a, b):
    """ Retourne le PGCD et les coefficients de Bézout """
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y


def mod_inverse(e, φn):
    """ Trouve l'inverse modulaire de e modulo φ(n) """
    gcd, x, _ = extended_gcd(e, φn)
    if gcd != 1:
        raise ValueError("⚠️ e et φ(n) ne sont pas premiers entre eux, choisir un autre e.")
    return x % φn


# 📌 Génération des clés RSA
def KeyGeneration():
    """ Génère une paire de clés RSA (publique et privée) """
    p = generate_large_prime(1024)
    q = generate_large_prime(1024)
    n = p * q
    φn = (p - 1) * (q - 1)
    e = 65537  # Valeur standard pour RSA

    # Vérifications
    assert isprime(p), "p n'est pas premier !"
    assert isprime(q), "q n'est pas premier !"
    assert p != q, "p et q doivent être différents !"

    if math.gcd(e, φn) != 1:
        raise ValueError("e n'est pas premier avec φ(n), choisir un autre e.")

    d = mod_inverse(e, φn)

    print(f"🔑 Clé publique : (e={e}, n={n})")
    print(f"🔐 Clé privée : (d={d}, n={n})")
    print(f"🧩 Taille de n : {n.bit_length()} bits\n")

    return n, e, d


# 📌 Transformation Texte ↔ Nombre entier
def text_to_int(text):
    """ Convertit un texte en entier pour le chiffrement RSA """
    return int.from_bytes(text.encode(), 'big')


def int_to_text(integer):
    """ Convertit un entier en texte après déchiffrement """
    try:
        return integer.to_bytes((integer.bit_length() + 7) // 8, 'big').decode()
    except UnicodeDecodeError:
        return "⚠️ Erreur : Résultat déchiffré invalide"


# 📌 Chiffrement avec RSA
def Encryption(message, e, n):
    """ Chiffre un message avec la clé publique """
    message_int = text_to_int(message)
    encrypted = pow(message_int, e, n)
    print(f"🔒 Message chiffré : {encrypted}\n")
    return encrypted


# 📌 Déchiffrement avec RSA
def Decryption(encrypted, d, n, original_message):
    """ Déchiffre un message avec la clé privée """
    decrypted_int = pow(encrypted, d, n)
    decrypted_message = int_to_text(decrypted_int)

    if decrypted_message != original_message:
        print("⚠️ Le message déchiffré est différent de l'original !\n")
    else:
        print("✅ Succès : Le message original est retrouvé.")

    print(f"🔑 Message déchiffré : {decrypted_message}\n")
    return decrypted_message


# 📌 Fonction de hachage SHA-256 pour la signature numérique
def hash_message(message):
    """ Retourne le hash SHA-256 du message """
    return int.from_bytes(hashlib.sha256(message.encode()).digest(), 'big')


# 📌 Signature numérique RSA
def SignMessage(message, d, n):
    """ Signe un hash du message avec la clé privée """
    message_hash = hash_message(message)
    signature = pow(message_hash, d, n)
    print(f"✍️ Signature générée : {signature}")
    return signature


# 📌 Vérification de la signature RSA
def VerifySignature(signature, e, n, original_message):
    """ Vérifie une signature en comparant le hash du message """
    verified_hash = pow(signature, e, n)
    original_hash = hash_message(original_message)

    if verified_hash == original_hash:
        print("✅ Signature valide : le message est authentique.")
    else:
        print("❌ Signature invalide : le message a été altéré !")


# 🚀 Exécution du programme principal
def main():
    """ Exécute toutes les étapes du programme """
    # 🛠 Génération des clés RSA
    n, e, d = KeyGeneration()

    # 📜 Message de test
    message = "Hello World !"

    # 🔒 Chiffrement
    encrypted_message = Encryption(message, e, n)

    # 🔓 Déchiffrement
    decrypted_message = Decryption(encrypted_message, d, n, message)

    # ✍️ Signature
    signature = SignMessage(message, d, n)

    # ✅ Vérification de la signature
    VerifySignature(signature, e, n, message)

    # 🚨 Test d'attaque : Vérification d'une signature modifiée
    VerifySignature(signature, e, n, "Fake Message")


if __name__ == "__main__":
    main()