from restaurante import Restaurante

restaurante_praca = Restaurante('praça gourmet', 'gourmert')
restaurante_mexicano = Restaurante('Mexican Food', 'mexicana')
restaurante_japones = Restaurante('sushi japa', 'japonesa')

restaurante_mexicano.alternar_estado()


restaurante_praca.receber_avaliacao('gui', 5)
restaurante_praca.receber_avaliacao('gabi', 4)
restaurante_praca.receber_avaliacao('dudu', 2)


def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()