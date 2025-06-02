import streamlit as st
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
from msal import ConfidentialClientApplication
import os

# Azure Key Vault and Azure Entra ID configuration
KEY_VAULT_NAME = os.getenv("KEY_VAULT_NAME")
KV_URI = f"https://{KEY_VAULT_NAME}.vault.azure.net"
TENANT_ID = os.getenv("AZURE_TENANT_ID")
CLIENT_ID = os.getenv("AZURE_CLIENT_ID")
CLIENT_SECRET = os.getenv("AZURE_CLIENT_SECRET")

# Initialize the Azure Identity and Key Vault clients
credential = DefaultAzureCredential()
client = SecretClient(vault_url=KV_URI, credential=credential)

# MSAL configuration
app_msal = ConfidentialClientApplication(
    client_id=CLIENT_ID,
    authority=f"https://login.microsoftonline.com/{TENANT_ID}",
    client_credential=CLIENT_SECRET
)

st.title("Frontend com Streamlit")
st.write("Autenticação via Azure Entra ID e acesso ao Azure Key Vault")

# Função para obter segredo do Key Vault
def get_secret(secret_name):
    secret = client.get_secret(secret_name)
    return secret.value

# Interface do usuário para obter segredo
secret_name = st.text_input("Nome do segredo")
if st.button("Obter segredo"):
    secret_value = get_secret(secret_name)
    st.write(f"Valor do segredo: {secret_value}")
