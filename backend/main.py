from fastapi import FastAPI, Depends
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
from fastapi.security import OAuth2AuthorizationCodeBearer
from msal import ConfidentialClientApplication
import os

app = FastAPI()

# Azure Key Vault and Azure Entra ID configuration
KEY_VAULT_NAME = os.getenv("KEY_VAULT_NAME")
KV_URI = f"https://{KEY_VAULT_NAME}.vault.azure.net"
TENANT_ID = os.getenv("AZURE_TENANT_ID")
CLIENT_ID = os.getenv("AZURE_CLIENT_ID")
CLIENT_SECRET = os.getenv("AZURE_CLIENT_SECRET")

# Initialize the Azure Identity and Key Vault clients
credential = DefaultAzureCredential()
client = SecretClient(vault_url=KV_URI, credential=credential)

# OAuth2 configuration
oauth2_scheme = OAuth2AuthorizationCodeBearer(
    authorizationUrl=f"https://login.microsoftonline.com/{TENANT_ID}/oauth2/v2.0/authorize",
    tokenUrl=f"https://login.microsoftonline.com/{TENANT_ID}/oauth2/v2.0/token",
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET
)

# MSAL configuration
app_msal = ConfidentialClientApplication(
    client_id=CLIENT_ID,
    authority=f"https://login.microsoftonline.com/{TENANT_ID}",
    client_credential=CLIENT_SECRET
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/secret")
def read_secret(secret_name: str, token: str = Depends(oauth2_scheme)):
    # Get the secret from Azure Key Vault
    secret = client.get_secret(secret_name)
    return {"secret_value": secret.value}
