#!/bin/bash
set -e
mkdir -p kafka-certs
cd kafka-certs

# 1. Gerar CA
openssl genrsa -out ca.key 4096
openssl req -x509 -new -key ca.key -sha256 -days 365 -out ca.pem -subj "/CN=Kafka-CA"

# 2. Gerar chave + CSR do broker
openssl genrsa -out broker.key 4096
openssl req -new -key broker.key -out broker.csr -subj "/CN=localhost"

# 3. Assinar certificado do broker
openssl x509 -req -in broker.csr -CA ca.pem -CAkey ca.key -CAcreateserial -out broker.crt -days 365 -sha256

# 4. Criar broker.pem (cert + key juntos)
cat broker.crt broker.key > broker.pem
