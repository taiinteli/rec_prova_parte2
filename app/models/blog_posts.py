class BlogPost:
    def __init__(id, self, usuario, review, serie_filme, estrelas):
        self.id = '1'
        self.usuario = 'nome_usuario'
        self.review = 'este filme foi supimpa'
        self.serie_filme = 'pokemon a vingança de mewteo'
        self.estrelas = '5'

    def __str__(self) -> str:
        return f'{self.id} - {self.usuario} - {self.review} - {self.serie_filme} - {self.estrelas}'
    
    def toJson(self):
        return {'id': self.id, 'usuario': self.usuario, 'review': self.review, 'serie_filme': self.serie.filme, 'estrelas': self.estrelas}
    
