# Ecommerce Api

## Orientações
 Exemplo:Docker: Criando a Docker Image com o Python e Flask
 * [Windows](https://ebasso.net/wiki/index.php?title=Docker:_Criando_a_Docker_Image_com_o_Python_e_Flask)
 
```
## Pré requisitos:
Para executar esta aplicação você deve ter o Docker instalado.
* [Windows](https://docs.docker.com/windows/started)
* [OS X](https://docs.docker.com/mac/started/)
* [Linux](https://docs.docker.com/linux/started/)

## Uso:
Clone este repositório
```shell
$ git clone https://github.com/JenniferFariasRodrigues/ecommerce_api
```
Navegue para o diretório clonado
```shell
$ cd ecommerce_api
```
Monte o container
```shell
$ docker image build -t ecommerce_api .
```
Execute o container em segundo plano
```shell
$ docker run -p 5001:5000 -d ecommerce_api
```

Para verificar o resultado acesse o endereço http://localhost:5001
```