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

### Criação da instância MYSQL

Encontra-se um ficheiro docker-compose.yml disponivel na raíz do projecto. Abrir o terminal 

1. docker-compose up