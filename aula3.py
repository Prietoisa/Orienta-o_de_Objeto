# def item(*continua):
#     for objeto in continua:
#         print(objeto)

# item('item1, item2, item3, item4')

def salada_de_frutas(**dicio_de_argumento):
    fruta = dicio_de_argumento.get('fruta')
    if fruta is not None:
        print(f'Você terá que pegar esta fruta:{fruta}')

salada_de_frutas(fruta='1 maça', acompanhamento='3 bananas', acompanhamento2='5 morangos')