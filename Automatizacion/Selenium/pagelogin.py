from page import Page

class PageLogin(Page):
    def __init__(self, url) -> None:
        super().__init__(url)

    def hacer_login(self, usuario, contrasena):
        self.__buscar_elemento_id__("id_username").send_keys(usuario)
        self.__buscar_elemento_id__("id_password").send_keys(contrasena)
        self.__buscar_elemento_xpath__('//*[@id="login-form"]/div[3]/input').click()
        self.__esperar__(10)

    def cerrar_sesion(self):
        self.__buscar_elemento_link__("CERRAR SESIÓN").click()

    def devolver_titulo(self):
        return self.__devolver_titulo__()