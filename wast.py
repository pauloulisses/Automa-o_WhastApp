import pywhatkit as kit  # Biblioteca para enviar mensagens no WhatsApp
import pyautogui as auto  # Biblioteca para automação de teclas e cliques
import time  # Biblioteca para manipular tempo e pausas

# Função para enviar mensagens no WhatsApp
def enviar_msg(numero, mensagem):
    try:
        print(f'Enviando mensagem para {numero}...')  # Exibe uma mensagem no terminal

        # Envia a mensagem instantaneamente para o número informado
        kit.sendwhatmsg_instantly(numero, mensagem, wait_time=15, tab_close=True)
    
        time.sleep(10)  # Aguarda 10 segundos para garantir o envio
    
        auto.press('enter')  # Pressiona 'Enter' para confirmar o envio da mensagem
        print(f'Mensagem enviada com sucesso para {numero}!')  # Exibe uma mensagem de sucesso

    except Exception as e:
        
        print(f'Erro ao enviar a mensagem para {numero}: {e}')  # Captura e exibe qualquer erro

# Verifica se o script está sendo executado diretamente
if __name__ == '__main__':
    lista_numeros = [  # Lista com os números de telefone para envio das mensagens
        "+558922222222",
        "+558911111111",
    ]

    mensagem = """
    Cuida em estudar 📚👨‍🎓
    treinando meu robo do zap
    """  # Mensagem que será enviada

    print('Iniciando o envio de mensagens')  # Mensagem informando o início do processo

    for numero in lista_numeros:  # Loop para percorrer a lista de números
        enviar_msg(numero, mensagem)  # Chama a função de envio para cada número
        time.sleep(5)  # Aguarda 5 segundos antes de enviar para o próximo número
