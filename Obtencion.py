import time
from selenium import webdriver
import os
from selenium.webdriver.common.action_chains import ActionChains #para usar scroll into view
import pyautogui
import autoit




                                                                            #INICIO DRIVER E INGRESO A WEBSITE
#tomo el directorio actual para abrir el driver
directorioActual = os.getcwd()
driver = webdriver.Chrome(directorioActual + "\chromedriver_win32\chromedriver.exe")
actions = ActionChains(driver)

#voy a la pag de carreras
driver.get("https://www.corredorpromedio.com/carreras/argentina/")    #abro pagina de carreras




i = int(input("desde que numero comienzo a enumerar?: ")) #establesco un contador
respuesta = input("Quiero publicar una carrera: ").upper()
                                                                            #CREO ARCHIVO
while respuesta != "NO":

    file = open("upload/" + str(i) + ".txt", "w")  # creo el archivo en concreto
    driver.switch_to.window(driver.window_handles[1])#cambio a la ventana con la carrera abierta

    # titulo:
    titulo = driver.find_element_by_xpath("//div/h1[@class='mec-single-title']")
    ActionChains(driver).move_to_element(titulo).perform()  # la ubico en centro de pag para imagen
    titulo = titulo.text
    file.write(titulo.upper())    #ingreso primero el titulo todo en mayusculas
    file.write('\n')

    # fecha:
    fecha = driver.find_element_by_xpath("//abbr[@class='mec-events-abbr']/span[@class='mec-start-date-label']")
    fecha = fecha.text
    file.write("CUANDO: " + fecha)
    file.write('\n')

    # ubicacion:
    ubic = driver.find_element_by_xpath("//address[@class='mec-events-address']/span[@class='mec-address']")
    ubic = ubic.text
    file.write("DONDE: " + ubic)
    file.write('\n')

    #distancia:
    try:
        distancia = driver.find_element_by_xpath("//div[@class='mec-single-event-description mec-events-content']/ul[@style='text-align: justify;']/li")
        distancia = distancia.text
    except:
        distancia = "Contacta a los organizadores para la informacion exacta!"
    file.write("DISTANCIA: " + distancia)
    file.write("\n")

    # instagram:
    try:
        insta = driver.find_element_by_xpath(
            "//img[@src='https://www.corredorpromedio.com/wp-content/uploads/2016/08/instagram_rs.png']/following-sibling::a")
        insta = insta.text
        file.write("INSTAGRAM: " + insta)
        file.write("\n")
    except:
        pass



    #mas info:
    try:
        file.write("CONTACTO: ")
        telefono = driver.find_element_by_xpath("//dd[@class='mec-organizer-tel']/a").get_attribute("text")
        file.write("\n" + telefono)
    except:
        pass

    try:
        correo = driver.find_element_by_xpath("//dd[@class='mec-organizer-email']/a").get_attribute("text")
        file.write("\n" + correo)
    except:
        pass

    try:
        web = driver.find_element_by_xpath("//dd[@class='mec-organizer-url']/span/a").get_attribute("text")
        file.write("\n" + web)
    except:
        pass

    file.write("-" + "\n" + "-" + "\n" + "-" + "\n" + "-" + "\n" + "-" + "\n")
    file.write("#run #running #runningmotivation #runners #runninglife #argentina #runninglife #runningargentina #corredor #corredores #placer #deporte #sport #happiness")



    file.close()




    #imagen:
    time.sleep(1)
    image = driver.find_element_by_xpath("//img[@class='attachment-full size-full wp-post-image']")    #encuentro img
    ActionChains(driver).context_click(image).perform()    #boton derecho
    pyautogui.keyDown('shift')    #presiono teclas para "guardar como" y espero
    pyautogui.press("d")
    pyautogui.keyUp('shift')
    time.sleep(2)



                                                    #ARRANCO A CONTROLAR EL ARCHIVO "GUARDAR COMO"

    directorioActual = directorioActual.replace("\\", "/")    #actualizo escritura por compatibilidad
    autoit.win_wait_active("Guardar como")    #activo autoit, controlador de pestaña de guardado




    time.sleep(1)
    #primero voy al folder correcto
    autoit.control_set_text("Guardar como", "Edit1", r"C:\Users\gianp\PycharmProjects\Carreras\upload")
    autoit.control_click("Guardar como", "Button2")
    time.sleep(1)
    #luego ingreso nombre de archivo
    autoit.control_set_text("Guardar como", "Edit1", str(i) + ".jpg")
    autoit.control_click("Guardar como", "Button2")




                                            #ELIMINO LA PAGINA CON LA CARRERA

    driver.close()
    i = i + 1
    respuesta = input("Quiero publicar otra carrera: ").upper()




#ABRIR TODAS LAS CARRERAS DE UNA Y QUE LAS RECORRA Y GUARDE EN ORDEN CORRECTO
