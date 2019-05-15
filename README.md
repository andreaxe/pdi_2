# Processamento de pares de identificadores (PDI 2)

Pretende-se criar um algorítmo para classificar hierarquicamente a informação a partir de registos compostos por pares 
de identificadores.Para este trabalho, deverá considerar a informação disponível em duas tabelas de uma dada base de 
dados: 

1. tabela com os pares de identificadores; 
2. tabela com o significado/tópico correspondente a cada identificador. 

Em cada registo da tabela de identificadores, o identificador que aparece em primeiro é um ramo do identificador que
 aparece em segundo lugar. 

O algorítmo a conceber, deverá permitir estruturar a informação de modo a que esta se apresente, visulamente, 
sob a forma de uma hierarquia, taxonomia, ou organigrama.

O trabalho contempla quatro componentes: (i) concetualização do algorítmo; 
1. testes de validação; 
2. representação gráfica 
3. elaboração do relatório técnico.
 
Os objetivos a atingir com o trabalho são: 

1. processar a informação num dado dataset com base em pares de identificadores; 
2.ordenar e representar a informação tendo como referência o conceito de hierarquia, taxonomia, ou organigrama; 
3. sistematizar o processo por forma a generalizar para casos similares.

### Exemplo:

- Na pasta *plots* encontram-se imagens das árvores de dependências geradas. 

![image](https://user-images.githubusercontent.com/9929973/57588637-eb594980-750e-11e9-88f5-d4e1f88e92eb.png)

# Deploy do projecto

### Criação da instância MYSQL

Se necessitar de criar uma base se dados MySQL, encontra-se um ficheiro docker-compose.yml disponivel na raíz 
do projecto. Abrir o terminal 

1. $ docker-compose up -d 

### Usar uma base de dados existente

1. No ficheiro main.py encontra-se disponivel a informação para acesso à base de dados. Se preferir usa uma base de dados
existente deverá actualizar a informação disponibilizada por defeito.
![image](https://user-images.githubusercontent.com/9929973/57795732-9c91f680-773e-11e9-825e-576c9ce10969.png)

2. **NOTA:** Após a actualização da informação de acesso à BD deverá assegurar que o bloco de código responsável por 
gerar um novo dataset (*main.py*) se encontra comentado, caso contrário a BD que indicou será restaurada com informação gerada
pelo algoritmo.

    ![image](https://user-images.githubusercontent.com/9929973/57795944-20e47980-773f-11e9-9062-63f559cb91f0.png)
    
### Dependências do projecto

Para correr o software deverá ter instalado o **Python 3.6** e usar o instalador de pacotes **PIP** para instalação
das dependências presentes no ficheiro *"requirements.txt"*.

A instalação das dependências poderá ser efectuada a partir da pasta do projecto executando o seguinte comando:

* $ pip install requirements.txt

**NOTA** Poderá ocorrer algum erro na instalação da bilbioteca *"pygraphviz"* por falta de dependências da bilbiotecas C. O problema pode ser resolvido através da instalação das mesmas:

* $ sudo apt-get install graphviz libgraphviz-dev pkg-config

A alternativa poderá ser usar o miniconda para criação de um ambiente virtual e instalação das dependências e da biblioteca em falha.

Em caso de dúvida contactar: andregarxia@gmail.com