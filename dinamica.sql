drop schema test cascade;
create schema test;

DROP TABLE IF EXISTS test.CAMPO CASCADE;
CREATE TABLE test."CAMPO" (
   Cod_Campo VARCHAR(10) PRIMARY KEY,
   Nome_Campo VARCHAR (50) UNIQUE NOT NULL
);

DROP TABLE IF EXISTS test.SEQUENCIA;
CREATE TABLE test."SEQUENCIA" (
   Cod_Sequencia VARCHAR(10) PRIMARY KEY,
   Nome_Sequencia VARCHAR (50) UNIQUE NOT NULL
);

DROP TABLE IF EXISTS test.CAMPO_SEQUENCIA;
CREATE TABLE test."CAMPO_SEQUENCIA" (
   Cod_Campo VARCHAR(10) references test."CAMPO"(Cod_Campo),
   Cod_Sequencia VARCHAR(10) references test."SEQUENCIA"(Cod_Sequencia),
   primary key (Cod_Campo, Cod_Sequencia)
);

DROP TABLE IF EXISTS test.CHAVE_CONTAS;
CREATE TABLE test."CHAVE_CONTAS" (
   Cod_ChaveContas VARCHAR(10) PRIMARY KEY,
   Desc_ChaveContas VARCHAR(50) UNIQUE NOT NULL
);

DROP TABLE IF EXISTS test.TIPO_VALOR;
CREATE TABLE test."TIPO_VALOR" (
   Cod_TipoValor VARCHAR(10) PRIMARY KEY,
   Desc_TipoValor VARCHAR(50) UNIQUE NOT NULL
);

DROP TABLE IF EXISTS test.CAMADA;
CREATE TABLE test."CAMADA" (
   Cod_Camada VARCHAR(10) PRIMARY KEY,
   Nome_Camada VARCHAR(50) NOT null,
   TIPO_BASE_VENDAS VARCHAR(1) not null
);






INSERT INTO test."CAMPO" (cod_campo, nome_campo) VALUES('CP000', 'CODTERCHV');
INSERT INTO test."CAMPO" (cod_campo, nome_campo) VALUES('CP001', 'CODCNL');
INSERT INTO test."SEQUENCIA" (cod_sequencia, nome_sequencia) VALUES('SQ000', 'CODTERCHV/CODCNL');
INSERT INTO test."CAMPO_SEQUENCIA" (cod_campo, cod_sequencia) VALUES('CP000', 'SQ000');
INSERT INTO test."CAMPO_SEQUENCIA" (cod_campo, cod_sequencia) VALUES('CP001', 'SQ000');
INSERT INTO test."CHAVE_CONTAS" (cod_chavecontas, desc_chavecontas) VALUES('CC000', 'Chave 1');
INSERT INTO test."CHAVE_CONTAS" (cod_chavecontas, desc_chavecontas) VALUES('CC001', 'Chave 2');
INSERT INTO test."CHAVE_CONTAS" (cod_chavecontas, desc_chavecontas) VALUES('CC002', 'Chave 3');
INSERT INTO test."TIPO_VALOR" (cod_tipovalor, desc_tipovalor) VALUES('TV000', 'PERCENTUAL');
INSERT INTO test."TIPO_VALOR" (cod_tipovalor, desc_tipovalor) VALUES('TV001', 'VALOR');
INSERT INTO test."TIPO_VALOR" (cod_tipovalor, desc_tipovalor) VALUES('TV002', 'CALCULADO');
INSERT INTO test."CAMADA" (cod_camada, nome_camada, tipo_base_vendas) VALUES('CC000', 'CMV', 'B');
INSERT INTO test."CAMADA" (cod_camada, nome_camada, tipo_base_vendas) VALUES('CC001', 'MARGEM', 'B');
INSERT INTO test."CAMADA" (cod_camada, nome_camada, tipo_base_vendas) VALUES('CC002', 'VERBA', 'B');
INSERT INTO test."CAMADA" (cod_camada, nome_camada, tipo_base_vendas) VALUES('CC003', 'OPERACIONAL', 'B');
INSERT INTO test."CAMADA" (cod_camada, nome_camada, tipo_base_vendas) VALUES('CC004', 'REGULATORIO', 'B');
INSERT INTO test."CAMADA" (cod_camada, nome_camada, tipo_base_vendas) VALUES('CC006', 'ADICIONAL', 'B');
INSERT INTO test."CAMADA" (cod_camada, nome_camada, tipo_base_vendas) VALUES('CC007', 'PRECO_BASE', 'V');
INSERT INTO test."CAMADA" (cod_camada, nome_camada, tipo_base_vendas) VALUES('CC008', 'MARGEM', 'V');
INSERT INTO test."CAMADA" (cod_camada, nome_camada, tipo_base_vendas) VALUES('CC009', 'OPERACIONAL', 'V');
INSERT INTO test."CAMADA" (cod_camada, nome_camada, tipo_base_vendas) VALUES('CC010', 'FINANCEIRO', 'V');
INSERT INTO test."CAMADA" (cod_camada, nome_camada, tipo_base_vendas) VALUES('CC011', 'DESCONTO', 'V');