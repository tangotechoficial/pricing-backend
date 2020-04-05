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
   id VARCHAR(20) unique primary key,
   Cod_Campo VARCHAR(10) references test."CAMPO"(Cod_Campo),
   Cod_Sequencia VARCHAR(10) references test."SEQUENCIA"(Cod_Sequencia)
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

DROP TABLE IF EXISTS test.CONDICAO;
CREATE TABLE test."CONDICAO" (
   Cod_Condicao VARCHAR(10) PRIMARY KEY,
   Desc_Condicao VARCHAR(30) NOT NULL,
   Cod_Camada VARCHAR(10) references test."CAMADA"(cod_camada) NOT NULL,
   Cod_ChaveContas VARCHAR(10) references test."CHAVE_CONTAS"(cod_chavecontas) NOT NULL,
   Cod_TipoValor VARCHAR(10) references test."TIPO_VALOR"(cod_tipovalor) NOT NULL,
   Escala_Qtde INTEGER NOT NULL,
   POS_NEG CHAR(1) NOT NULL,
   TIP_BASE_VENDAS CHAR(1) NOT NULL,
   MANDATORIA INTEGER NOT NULL,
   ESTATISTICA INTEGER NOT NULL
);

DROP TABLE IF EXISTS test.SEQUENCIA_CONDICAO;
CREATE TABLE test."SEQUENCIA_CONDICAO" (
   id VARCHAR(20) unique primary key,
   Cod_Sequencia VARCHAR(10) references test."SEQUENCIA"(Cod_Sequencia),
   Cod_Condicao VARCHAR(10) references test."CONDICAO"(Cod_Condicao)
);

DROP TABLE IF EXISTS test.ESQUEMA_DE_CALCULO;
CREATE TABLE test."ESQUEMA_DE_CALCULO" (
   Cod_Esquema_Calculo VARCHAR(10) PRIMARY KEY,
   TIPO_BASE_VENDAS VARCHAR(1) not null
);

DROP TABLE IF EXISTS test.CONDICAO_CAMADA_ESQUEMA;
CREATE TABLE test."CONDICAO_CAMADA_ESQUEMA" (
   id VARCHAR(30) unique primary key,
   Cod_Esquema_Calculo VARCHAR(10) NOT null references test."ESQUEMA_DE_CALCULO"(Cod_Esquema_Calculo),
   Cod_Condicao VARCHAR(10) NOT null references test."CONDICAO"(Cod_Condicao),
   Cod_Camada VARCHAR(10) NOT null references test."CAMADA"(Cod_Camada)
);

INSERT INTO test."CAMPO" (cod_campo, nome_campo) VALUES('CP000', 'CODTERCHV');
INSERT INTO test."CAMPO" (cod_campo, nome_campo) VALUES('CP001', 'CODCNL');
INSERT INTO test."SEQUENCIA" (cod_sequencia, nome_sequencia) VALUES('SQ000', 'CODTERCHV/CODCNL');
INSERT INTO test."CAMPO_SEQUENCIA" (id, cod_campo, cod_sequencia) VALUES('SQ000CP000', 'CP000', 'SQ000');
INSERT INTO test."CAMPO_SEQUENCIA" (id, cod_campo, cod_sequencia) VALUES('SQ000CP001', 'CP001', 'SQ000');
INSERT INTO test."CHAVE_CONTAS" (cod_chavecontas, desc_chavecontas) VALUES('CC000', 'Chave 1');
INSERT INTO test."CHAVE_CONTAS" (cod_chavecontas, desc_chavecontas) VALUES('CC001', 'Chave 2');
INSERT INTO test."CHAVE_CONTAS" (cod_chavecontas, desc_chavecontas) VALUES('CC002', 'Chave 3');
INSERT INTO test."TIPO_VALOR" (cod_tipovalor, desc_tipovalor) VALUES('TV000', 'PERCENTUAL');
INSERT INTO test."TIPO_VALOR" (cod_tipovalor, desc_tipovalor) VALUES('TV001', 'VALOR');
INSERT INTO test."TIPO_VALOR" (cod_tipovalor, desc_tipovalor) VALUES('TV002', 'CALCULADO');
INSERT INTO test."CAMADA" (cod_camada, nome_camada, tipo_base_vendas) VALUES('CA000', 'CMV', 'B');
INSERT INTO test."CAMADA" (cod_camada, nome_camada, tipo_base_vendas) VALUES('CA001', 'MARGEM', 'B');
INSERT INTO test."CAMADA" (cod_camada, nome_camada, tipo_base_vendas) VALUES('CA002', 'VERBA', 'B');
INSERT INTO test."CAMADA" (cod_camada, nome_camada, tipo_base_vendas) VALUES('CA003', 'OPERACIONAL', 'B');
INSERT INTO test."CAMADA" (cod_camada, nome_camada, tipo_base_vendas) VALUES('CA004', 'REGULATORIO', 'B');
INSERT INTO test."CAMADA" (cod_camada, nome_camada, tipo_base_vendas) VALUES('CA006', 'ADICIONAL', 'B');
INSERT INTO test."CAMADA" (cod_camada, nome_camada, tipo_base_vendas) VALUES('CA007', 'PRECO_BASE', 'V');
INSERT INTO test."CAMADA" (cod_camada, nome_camada, tipo_base_vendas) VALUES('CA008', 'MARGEM', 'V');
INSERT INTO test."CAMADA" (cod_camada, nome_camada, tipo_base_vendas) VALUES('CA009', 'OPERACIONAL', 'V');
INSERT INTO test."CAMADA" (cod_camada, nome_camada, tipo_base_vendas) VALUES('CA010', 'FINANCEIRO', 'V');
INSERT INTO test."CAMADA" (cod_camada, nome_camada, tipo_base_vendas) VALUES('CA011', 'DESCONTO', 'V');
INSERT INTO test."CONDICAO" (cod_condicao, desc_condicao, cod_camada, cod_chavecontas, cod_tipovalor, escala_qtde, pos_neg, tip_base_vendas, mandatoria, estatistica) VALUES('CO000', 'MARGEM_CANAL', 'CA001', 'CC001', 'TV001', 0, 'P', 'V', 0, 0);
INSERT INTO test."SEQUENCIA_CONDICAO" (id, cod_sequencia, cod_condicao) VALUES('CO000SQ000', 'SQ000', 'CO000');
INSERT INTO test."ESQUEMA_DE_CALCULO" (cod_esquema_calculo, tipo_base_vendas) VALUES('EC000', 'B');
INSERT INTO test."ESQUEMA_DE_CALCULO" (cod_esquema_calculo, tipo_base_vendas) VALUES('EC001', 'V');
INSERT INTO test."CONDICAO_CAMADA_ESQUEMA" (id, cod_esquema_calculo, cod_condicao, cod_camada) VALUES('EC001CO000CA001', 'EC001', 'CO000', 'CA001');

