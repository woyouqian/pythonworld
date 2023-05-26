class Testproduct1(object):

    def test_param(self, env_fixture):
        print("it is testing param now 1...")
        books = env_fixture['life']
        for book in books:
            print(book['name'], end='\t\t')
            print(book['author'])

