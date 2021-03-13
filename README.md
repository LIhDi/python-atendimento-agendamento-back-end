# ATENDIMENTO AGENDAMENTO 

- [ATENDIMENTO AGENDAMENTO](#atendimento-agendamento)
    - [Instalação](#instala%c3%a7%c3%a3o)
    - [Configuração](#configura%c3%a7%c3%a3o)
    - [API HTTP Service](#api-http-service)
      - [Executando a API HTTP](#executando-a-api-http)
      - [Documentação da API](#documenta%c3%a7%c3%a3o-da-api)
    - [Teste](#teste)
    - [Padrão de código](#padr%c3%a3o-de-c%c3%b3digo)


### Instalação
```sh
mkvirtualenv -p python3 <venvname>
make install
make install-dev
```


---------------------------------------

### Configuração
```sh
make docker_start_db
make migration
``` 

Posteriomente:
```sh
make docker_stop_db
make downgrade
``` 

---------------------------------------

### API HTTP Service

#### Executando a API HTTP
```sh
make run
``` 

#### Documentação da API
[http://localhost:8000/swagger/index.html](http://localhost:8000/swagger/index.html)

------------------------------------------


### Teste

- Adotamos o `pytest` como biblioteca de testes.
```sh
make test-all
make coverage
```
- Para executar apenas testes unitários
```sh
make unit-test
```
- Para executar apenas testes de integração

```sh
 make integration-test
```

------------------------------------------

### Padrão de código

Para ver o que deve ser modificado
```sh
make format-show
```

Para modificar automaticamente
```sh
make format
```
 
 
 
