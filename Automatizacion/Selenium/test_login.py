import time
import unittest
from pagelogin import PageLogin

class InicioSesion(unittest.TestCase):
    URL ="http://127.0.0.1:8000/admin/login/?next=/admin/"

    def setUp(self) -> None:
        self.driver = PageLogin(self.URL)

    def test_inicio_sesion(self):
        """ Evalua que inicie sesión en la aplicación """
        self.driver.hacer_login("useradminlogin", "user1q2w3e4r5t6y")
        time.sleep(5)

    def tearDown(self) -> None:
        self.driver.cerrar_sesion()
        self.driver.__finalizar__()

if __name__ == '__main__':
    unittest.main()
