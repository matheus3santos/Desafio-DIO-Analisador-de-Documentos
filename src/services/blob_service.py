import os
from azure.storage.blob import BlobServiceClient
import streamlit as st
from utils.Config import Config


def upload_blob(file, file_name):
    try:
        # Criando o cliente BlobService a partir da string de conexão
        blob_service_client = BlobServiceClient.from_connection_string(Config.AZURE_STORAGE_CONNECTION_STRING)
        
        # Corrigindo o acesso ao container, se for um atributo, remova os parênteses
        container_name = Config.CONTAINER_NAME  # Remova os parênteses se for um atributo
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=file_name)
        
        # Enviando o arquivo para o blob, sobrescrevendo se necessário
        blob_client.upload_blob(file, overwrite=True)
        
        # Retornando a URL do blob
        return blob_client.url

    except Exception as ex:
        # Escrevendo mensagem de erro no Streamlit
        st.write(f'Falha ao enviar o arquivo {ex} para o Azure Blob Storage')
        return None
