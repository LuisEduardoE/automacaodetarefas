import pyautogui  # type: ignore
import pygetwindow as gw  # type: ignore
import time

def abrir_promob():
    """Abre o programa Promob ERP Suspentech."""
    pyautogui.doubleClick(x=45, y=209)
    
    time.sleep(18)  # Aumentei o tempo pra esperar o promob carregar tudo

def login_promob(usuario, senha):
    """Realiza o login no Promob ERP."""
    pyautogui.click(x=964, y=614)
    pyautogui.write(usuario)
    time.sleep(1.5)
    pyautogui.press('Enter')
    time.sleep(1)
    pyautogui.write(senha)
    pyautogui.press('Enter')
    time.sleep(5)

def maximizar_janela(titulo):
    """Maximiza a janela se não estiver maximizada."""
    window = gw.getWindowsWithTitle(titulo)
    if window:
        win = window[0]
        if not win.isMaximized:
            pyautogui.hotkey('win', 'up')  # Maximiza a janela
            win.activate()
            time.sleep(5)
    else:
        print(f'Janela "{titulo}" não encontrada.')

def minimizar_janela(titulo):
    """Minimiza a janela se estiver aberta."""
    window = gw.getWindowsWithTitle(titulo)
    if window:
        win = window[0]
        win.minimize()  # Minimiza a janela
        time.sleep(2)
    else:
        print(f'Janela "{titulo}" não encontrada para minimizar.')

def clicar_coordenadas(x, y, delay=3):
    """Clica nas coordenadas especificadas."""
    pyautogui.click(x=x, y=y)
    time.sleep(delay)

def main():
    # Configurações
    usuario = '*******' #Digite o usuario
    senha = '*******' #Digite a senha 
    
    # Abrir o Promob
    abrir_promob()

    # Login no Promob
    login_promob(usuario, senha)
    time.sleep(7)

    #Maximizar a janela do Promob
    maximizar_janela('Promob - SUSPENTECH INDUSTRIA DE COMPONENTES AUTOMOTIVOS LTDA')

    # Espera para garantir que a janela esteja carregada
    time.sleep(7)  # Aumentar o tempo de espera antes de minimizar

    # Ações no programa
    clicar_coordenadas(747, 514)  # clicar no geral
    clicar_coordenadas(870, 593)  # clicar no processo de etiqueta
     #Minimizar a janela do Promob
    time.sleep(3)
    minimizar_janela('Promob - SUSPENTECH INDUSTRIA DE COMPONENTES AUTOMOTIVOS LTDA')

    # Maximizar a janela específica
    time.sleep(18)
    maximizar_janela('Específicos - SUSPENTECH INDUSTRIA DE COMPONENTES AUTOMOTIVOS LTDA')
    time.sleep(5.5)
    # Abrir favoritos
    clicar_coordenadas(161, 34)  # clicar no primeiro dos favoritos
    clicar_coordenadas(195, 53)  # na primeira sessao
    clicar_coordenadas(161, 34)  # clicar novamente nos favoritos
    clicar_coordenadas(195, 78)  # na segunda sessao
    
if __name__ == "__main__":
    main()
