from cryptography.hazmat.primitives.serialization import pkcs12
from cryptography.hazmat.primitives import serialization

with open("cert.pfx", "rb") as f:
    pfx_data = f.read()

private_key, certificate, additional_certificates = pkcs12.load_key_and_certificates(
    pfx_data,
    b"131213Ma@"
)

with open("cert.pem", "wb") as f:
    f.write(certificate.public_bytes(serialization.Encoding.PEM))

with open("key.pem", "wb") as f:
    f.write(
        private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption(),
        )
    )