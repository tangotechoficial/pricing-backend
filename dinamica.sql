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

DROP TABLE IF EXISTS test.MERCADORIA;
CREATE TABLE test."MERCADORIA" (
   CODPRD INTEGER unique not null primary key,
   DESPRD VARCHAR(50),
   CODDRTCLLATU INTEGER not NULL,
   DESDRTCLLATU VARCHAR(50),
   CODGRPPRD INTEGER not NULL,
   DESGRPPRD VARCHAR(50),
   CODCLSPRD INTEGER not NULL,
   DESCLSPRD VARCHAR(50),
   CODSUBCTGPRD INTEGER not null,
   DESSUBCTGPRD VARCHAR(50),
   CODSMR INTEGER not null,
   DESSMR VARCHAR(100)
);

DROP TABLE IF EXISTS test.FILIAL_EXPEDICAO;
CREATE TABLE test."FILIAL_EXPEDICAO" (
	CODFILEMP INTEGER unique not null primary key,
	DESFILEMP VARCHAR(50)
);

DROP TABLE IF EXISTS test.FILIAL_FATURAMENTO;
CREATE TABLE test."FILIAL_FATURAMENTO" (
	CODFILEMPFAT INTEGER unique not null primary key,
	DESFILEMPFAT VARCHAR(50)
);

DROP TABLE IF EXISTS test.ESTADO;
CREATE TABLE test."ESTADO" (
	CODESTUNI VARCHAR(2) unique not null primary key,
	DESESTUNI VARCHAR(20)
);

DROP TABLE IF EXISTS test.REGIAO;
CREATE TABLE test."REGIAO" (
	CODEDEREG INTEGER unique not null primary key,
	CODESTUNI VARCHAR(2) references test."ESTADO"(CODESTUNI),
	TIPEDEREG INTEGER
);


DROP TABLE IF EXISTS test.CHAVE_PRECIFICAO;
CREATE TABLE test."CHAVE_PRECIFICAO" (
	ID INTEGER unique not null primary key,
	CODMER INTEGER references test."MERCADORIA"(CODPRD),
	CODFILEMP INTEGER references test."FILIAL_EXPEDICAO"(CODFILEMP),
	CODFILEMPFAT INTEGER references test."FILIAL_FATURAMENTO"(CODFILEMPFAT),
	TIPEDEREG INTEGER,
	CODEDEREG INTEGER references test."REGIAO"(CODEDEREG)
);

DROP TABLE IF EXISTS test.ESQUEMA_CHAVE;
CREATE TABLE test."ESQUEMA_CHAVE" (
	ID INTEGER unique not null primary key,
	Cod_Esquema_Calculo VARCHAR(10) references test."ESQUEMA_DE_CALCULO"(Cod_Esquema_Calculo),
	ID_CHAVE INTEGER references test."CHAVE_PRECIFICAO"(ID)
);

DROP TABLE IF EXISTS test.PRECO;
CREATE TABLE test."PRECO" (
   ID INTEGER unique not null primary key,
   Cod_Esquema_Calculo VARCHAR(10) references test."ESQUEMA_DE_CALCULO"(Cod_Esquema_Calculo),
   TIPO_BASE_VENDAS VARCHAR(1) not null,
   DATAINICIO DATE,
   VALOR FLOAT null,
   CHAVE INTEGER references test."CHAVE_PRECIFICAO"(ID)
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
INSERT INTO test."MERCADORIA" (codprd, desprd, coddrtcllatu, desdrtcllatu, codgrpprd, desgrpprd, codclsprd, desclsprd, codsubctgprd, dessubctgprd, codsmr, dessmr) VALUES(1648010, 'LEITE PO NINHO INSTANT.24X400G', 5, 'DIRETORIA ABB', 43, 'MERCEARIA DOCE', 22, 'NUTRICAO', 9, 'LEITE PO INTEGRAL/INSTANTANEO', 172, 'LEITE PO NINHO 24X400G');
INSERT INTO test."ESTADO" (codestuni, desestuni) VALUES('SP', 'Sao Paulo');
INSERT INTO test."ESTADO" (codestuni, desestuni) VALUES('MG', 'Minas Gerais');
INSERT INTO test."ESTADO" (codestuni, desestuni) VALUES('RJ', 'Rio de Janeiro');
INSERT INTO test."FILIAL_EXPEDICAO" (codfilemp, desfilemp) VALUES(1, 'MARTINS-UBERLANDIA MATRIZ');
INSERT INTO test."FILIAL_EXPEDICAO" (codfilemp, desfilemp) VALUES(29, 'MARTINS-MARINGA PR CDA');
INSERT INTO test."FILIAL_EXPEDICAO" (codfilemp, desfilemp) VALUES(52, 'MARTINS-CAD PB');
INSERT INTO test."FILIAL_FATURAMENTO" (codfilempfat, desfilempfat) VALUES(1, 'MARTINS-UBERLANDIA MATRIZ');
INSERT INTO test."FILIAL_FATURAMENTO" (codfilempfat, desfilempfat) VALUES(29, 'MARTINS-MARINGA PR CDA');
INSERT INTO test."FILIAL_FATURAMENTO" (codfilempfat, desfilempfat) VALUES(52, 'MARTINS-CAD PB');
INSERT INTO test."REGIAO" (codedereg, codestuni, tipedereg) VALUES(20, 'MG', 32);

