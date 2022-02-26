import time
from selenium import webdriver
import os
from selenium.webdriver.common.action_chains import ActionChains #para usar scroll into view
import pyautogui
import autoit
from selenium.webdriver.common.keys import Keys



def calendario (dia, mes):

    dia = int(dia)
    mes = int(mes)
    ano = 2021

    if mes == 1 or 3 or 5 or 7 or 8 or 10 or 12:

        if dia == 31:

            dia = 1
            mes = mes + 1

        else:
            dia = dia + 1

    elif mes == 2:

        if dia == 28:
            dia = 1
            mes = mes + 1

        else:
            dia = dia + 1

    else:
        if dia == 30:

            dia = 1
            mes = mes + 1

        else:
            dia = dia + 1

    if mes == 13:

        mes = 1
        ano = ano + 1

    return (dia, mes, ano)







#tomo el directorio actual para abrir el driver
directorioActual = os.getcwd()
driver = webdriver.Chrome(directorioActual + "\chromedriver_win32\chromedriver.exe")
actions = ActionChains(driver)




                                                            #INICIO DRIVER E INGRESO A WEBSITE

#voy a la pag de carreras
driver.get("https://business.facebook.com/creatorstudio/home")    #abro pagina de creator studio




                                                            #ME LOGEO EN FACEBOOK
time.sleep(4)
login = driver.find_element_by_xpath("//div/div/div[@class='l61y9joe j8otv06s ippphs35 a1itoznt qwtvmjv2 kiex77na lgsfgr3h mcogi7i5 ih1xi9zn a53abz89']") #clickeo el logeo
login.click()

username = "servicio.imp3d@gmail.com"
usuario = driver.find_element_by_xpath("//div[@id='email_container']/input[@id='email']")
usuario.send_keys(username)

password ="Basquet1"
contra = driver.find_element_by_xpath("//input[@id='pass']")
contra.send_keys(password)

iniciar = driver.find_element_by_xpath("//button[@id='loginbutton']")
iniciar.click()




                                                        #ME VOY A INSTAGRAM
insta = driver.find_element_by_xpath("//div[@id='media_manager_chrome_bar_instagram_icon']")
insta.click()




                                                    #COMIENZO A CREAR PUBLICACIONES
#fijo dia de hoy
diaPubli = input("Dia de inicio de publicacion: ")
mesPubli = input("Mes de inicio de publicacion: ")
anoPubli = input("Año de inicio de publicacion: ")
i = int(input("i = ?: "))
horario = "9"
rta = input("crear nueva publicacion?: ").upper()
while  rta != "NO":

    crear = driver.find_element_by_xpath("//div[@class='_7_8d']/div[@class='k6xjwoyg lus27l5m']/div[@class='rwb8dzxj tb4cuiq2 kojzg8i3 yukb02kx duy2mlcu d6kd9m94']")
    crear.click()
    time.sleep(1)
    feed = driver.find_element_by_xpath("//div/strong[text()='Feed de Instagram']")
    feed.click()
    time.sleep(5)
    cuenta = driver.find_element_by_xpath("//div[text()='running.argentina']")
    cuenta.click()
    #ahi cree una nueva entrada de publicacion




    #ABRO TXT PARA COMPLETAR LA INFO
    txt = open("upload/" + str(i) + ".txt", "r")
    time.sleep(1.5)




    #agrego texto a publicacion
    texto = driver.find_element_by_xpath("//div[text()='Escribe el texto...']/../../..")
    texto.click()
    info = txt.read()
    texto.send_keys(info)




    #agrego ubicacion
    ubicacion = driver.find_element_by_xpath("//span/label/input[@type='text'][@style='letter-spacing: normal; color: rgb(29, 33, 41); font-size: 12px; font-family: Arial, sans-serif; line-height: 16px;']") #donde poner la ubicacion
    txt.close()#tengo que cerrar el archivo para poder volver a leer
    txt = open("upload/" + str(i) + ".txt", "r")
    txt.readline()
    txt.readline()
    donde = txt.readline().rstrip("\n")
    donde = donde.replace('DONDE: ', '')
    ubicacion.click()
    ubicacion.send_keys(donde)
    time.sleep(2)
    driver.find_element_by_xpath("//div/div/span[text()='Tu publicación']").click()





    #FOTO DE PUBLICACION
    foto = driver.find_element_by_xpath("//div/div[@aria-haspopup='true']/div/span[text()='Agregar contenido']")
    foto.click()
    time.sleep(1)
    archivo = driver.find_element_by_xpath("//div/a/div[text()='De los archivos subidos']/..")
    archivo.click()
    #controlo archivo de guardado
    time.sleep(3)
    autoit.win_wait_active("Abrir")#nombre de guardado
    ruta = r'C:\Users\gianp\PycharmProjects\Carreras\upload\'' + str(i) + '.jpg' #tengo que hacer esto por culpa del backslash
    ruta = ruta.replace("'", "")
    autoit.control_set_text("Abrir", "Edit1", ruta)
    autoit.control_click("Abrir", "Button1")
    time.sleep(1)






    #consigo instagram:
    txt.close()
    w = "INSTAGRAM: "  # For Python 3: use input() instead
    with open("upload/" + str(i) + ".txt", "r") as f:
        found = False
        for line in f:
            if w in line:  # Key line: check if `w` is in the line.
                insta = line
                insta = insta.replace("INSTAGRAM: ", "")
                # ETIQUETAR EN INSTA
                etiqueta = driver.find_element_by_xpath("//div[@class='_8s0r']/div[@title='Etiquetar archivo multimedia']/i/../..")
                etiqueta.click()
                imagen = driver.find_element_by_xpath("//div[@id='mediaManagerInstagramComposerMediaTagging']")
                time.sleep(1.5)
                imagen.click()
                ingreso_insta = driver.find_element_by_xpath("//input[@placeholder='Type instagram username']")
                ingreso_insta.send_keys(insta)
                time.sleep(1.5)
                ingreso_insta.send_keys(Keys.ENTER)
                guardar = driver.find_element_by_xpath("//div/div/span/div/div/div[text()='Guardar']")
                guardar.click()

                found = True
        if not found:
            print('No se puede etiquetar')





    #PUBLICAR EN FACEBOOK
    boton = driver.find_element_by_xpath("//div/span/div/div/button[@type='button']")
    boton.click()




    #PROGRAMAR EN INSTA
    time.sleep(2)
    flecha_extra = driver.find_element_by_xpath("//div/button[@style='letter-spacing: normal; color: rgb(255, 255, 255); font-size: 13px; font-weight: bold; font-family: Arial, sans-serif; line-height: 34px; text-align: center; background-color: rgb(24, 119, 242); border-color: rgb(24, 119, 242); height: 36px; padding-left: 10px; padding-right: 10px; background-clip: padding-box;']")
    flecha_extra.click()
    programar = driver.find_element_by_xpath("//div/span[text()='Programar']/preceding-sibling::div")
    programar.click()





    # chequeo + o - para pasar 12 hs
    horas = driver.find_elements_by_xpath("//div/div[@aria-atomic='true'][@aria-live='polite'][@role='group']/div/div/div//input[@role='spinbutton']")
    horas[1].click()
    horas[1].send_keys('00')
    horas[0].click()
    horas[0].send_keys(horario)
    fechaPubli = driver.find_element_by_xpath("//label/input[@type='text'][@placeholder='dd/mm/aaaa']")
    fechaPubli.click()
    fechaPubli.send_keys(str(diaPubli) + "/" + str(mesPubli) + "/" + str(anoPubli))
    if horario == "9":

        horario = "21"
    else:
        diaPubli, mesPubli, anoPubli = calendario(diaPubli, mesPubli)
        horario = "9"


    programar = driver.find_element_by_xpath("//div/div[text()='Programar']").click()
    time.sleep(6)




    i = i + 1
    rta = "SI"







    #AGREGAR PUBLICACION PROGRAMADA PARA FACEBOOK TAMBIEN
    #SELECCIONAR EL INSTA CUANDO LO BUSCA EN EL BUSCADOR
    #SELECCIONAR ALGUN TIPO DE UBICACION