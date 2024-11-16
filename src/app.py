import streamlit as st
from services.blob_service import upload_blob
from services.credit_card_service import analize_credit_card


def configure_interface():
    
    st.title('Upload de Arquivos DIO - Desafio - Azure - Fake Docs')
    uploaded_file = st.file_uploader("Escolha um arquivo CSV", type=['png','jpg','jpeg'])
    
    if uploaded_file is not None:
         fileName = uploaded_file.name
         # Enviar para o blob storage
         blob_url = upload_blob(uploaded_file, fileName)
         
         if blob_url:
             st.write(f'Arquivo {fileName} enviado com sucesso para o Azure Blob Storage')
             credi_card_info = analize_credit_card(blob_url)
             show_image_and_validation(blob_url, credi_card_info)
             
         else:
             st.write(f'Falha ao enviar o arquivo {fileName} para o Azure Blob Storage')
             
def show_image_and_validation(blob_url, credit_card_info):
    
    st.image(blob_url, caption='Imagem enviada')
    st.write('Resultado da validação')
    
    if credit_card_info and credit_card_info['card_name']:
        st.markdown(f'<h1 style="color:green;">Cartão de crédito válido</h1>', unsafe_allow_html=True)
        st.write(f'Nome do Titular: {credit_card_info["card_name"]}')
        st.write(f'Banco Emissor: {credit_card_info["bank_name"]}')
        st.write(f'Data de validade: {credit_card_info["expiry_date"]}')
        
    else:
        st.markdown(f'<h1 style="color:red;">Cartão de crédito inválido</h1>', unsafe_allow_html=True)
        st.write('Não foi possível identificar as informações do cartão de crédito')
    
if __name__ == '__main__':
    configure_interface()