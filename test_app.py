import unittest
from application import application


class TestHeroesAPI(unittest.TestCase):

    def setUp(self):
        # Cliente de pruebas de Flask: simula peticiones HTTP sin levantar servidor
        self.client = application.test_client()

    def test_listar_heroes(self):
        respuesta = self.client.get("/")
        self.assertEqual(respuesta.status_code, 200)
        self.assertGreater(len(respuesta.get_json()), 0)

    def test_obtener_heroe(self):
        respuesta = self.client.get("/0")
        self.assertEqual(respuesta.status_code, 200)
        self.assertEqual(respuesta.get_json()["name"], "A-Bomb")


if __name__ == "__main__":
    unittest.main()