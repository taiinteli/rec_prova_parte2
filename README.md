

# prova_rec_parte2

A tividade se refere à segunda parte da prova de recuperação do módulo 10 de de Engenharia da Computação. Ela é composta por um sistema em Docker Compose contendo um backend em FastAPI, com uma API de posts de blog armazenada em um arquivo e um gateway em nginx para redirecionamento através do localhost na porta 80, quando a rota inicia com o prefixo "/blog" para ser possível a postagem dos usuário cadastrar reviwes sobre filmes e séries de TV. 

A API que usei como base foi baseada no exemplo de Flask disponibilizado no github como exemplo nas aulas (https://github.com/Murilo-ZC/M10-Inteli-Eng-Comp/tree/main) e contém maturidade de Richardson de nível 2. Ela inclui rotas para ver todos os posts, ver um post por ID, criar o nome do usuário, review, a indicação do filme e a quantidade de estrelas. Além disso, ela loga o acesso às rotas a partir do nível WARNING, em arquivos na pasta logs, na raiz do projeto.



## Como executar

Veja se o docker já está baixado em seu sistema, clone o repositório e excute:

```bash
docker compose up
```

Endereço: `http://localhost/blog`.

Os arquivos estarão separados por timestamp de 1 em um 1 dia, como descrito no enunciado e verificado na fonte: https://docs.python.org/3/library/logging.handlers.html#timedrotatingfilehandler. 
