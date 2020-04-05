--
-- PostgreSQL database dump
--

-- Dumped from database version 12.2 (Debian 12.2-2.pgdg100+1)
-- Dumped by pg_dump version 12.2 (Debian 12.2-2.pgdg100+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: camada; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.camada (
    cod_camada character varying(10) NOT NULL,
    nome_camada character varying(50) NOT NULL,
    tipo_base_vendas character(1)
);


ALTER TABLE public.camada OWNER TO postgres;

--
-- Name: campo; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.campo (
    cod_campo character varying(10) NOT NULL,
    nome_campo character varying(20) NOT NULL
);


ALTER TABLE public.campo OWNER TO postgres;

--
-- Name: campo_sequencia; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.campo_sequencia (
    cod_sequencia character varying(10) NOT NULL,
    cod_campo character varying(10) NOT NULL
);


ALTER TABLE public.campo_sequencia OWNER TO postgres;

--
-- Name: chave_contas; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.chave_contas (
    cod_chavecontas character varying(10) NOT NULL,
    desc_chavecontas character varying(50) NOT NULL
);


ALTER TABLE public.chave_contas OWNER TO postgres;

--
-- Name: condicao; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.condicao (
    cod_condicao character varying(10) NOT NULL,
    desc_condicao character varying(30) NOT NULL,
    cod_camada character varying(10) NOT NULL,
    cod_chavecontas character varying(10) NOT NULL,
    cod_tipovalor character varying(10) NOT NULL,
    escala_qtde integer NOT NULL,
    pos_neg character(1) NOT NULL,
    tip_base_vendas character(1) NOT NULL,
    mandatoria integer NOT NULL,
    estatistica integer NOT NULL
);


ALTER TABLE public.condicao OWNER TO postgres;

--
-- Name: condicao_camada_esquema; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.condicao_camada_esquema (
    cod_esquema_calculo character varying(10) NOT NULL,
    cod_condicao character varying(10) NOT NULL,
    cod_camada character varying(10) NOT NULL
);


ALTER TABLE public.condicao_camada_esquema OWNER TO postgres;

--
-- Name: condicao_sequencia; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.condicao_sequencia (
    cod_condicao character varying(10) NOT NULL,
    cod_sequencia character varying(10) NOT NULL
);


ALTER TABLE public.condicao_sequencia OWNER TO postgres;

--
-- Name: esquema_de_calculo; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.esquema_de_calculo (
    cod_esquema_calculo character varying(10) NOT NULL,
    tipo_base_vendas character(1) NOT NULL
);


ALTER TABLE public.esquema_de_calculo OWNER TO postgres;

--
-- Name: preco; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.preco (
    id integer NOT NULL,
    chave integer NOT NULL,
    data date NOT NULL,
    cod_esquema_calculo character varying(10),
    valor double precision NOT NULL,
    tipo_base_venda character(1) NOT NULL
);


ALTER TABLE public.preco OWNER TO postgres;

--
-- Name: preco_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.preco_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.preco_id_seq OWNER TO postgres;

--
-- Name: preco_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.preco_id_seq OWNED BY public.preco.id;


--
-- Name: sequencia; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.sequencia (
    cod_sequencia character varying(10) NOT NULL,
    nome_sequencia character varying(100) NOT NULL
);


ALTER TABLE public.sequencia OWNER TO postgres;

--
-- Name: tipo_valor; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.tipo_valor (
    cod_tipovalor character varying(10) NOT NULL,
    desc_tipovalor character varying(50) NOT NULL
);


ALTER TABLE public.tipo_valor OWNER TO postgres;

--
-- Name: preco id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.preco ALTER COLUMN id SET DEFAULT nextval('public.preco_id_seq'::regclass);


--
-- Data for Name: camada; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.camada (cod_camada, nome_camada, tipo_base_vendas) FROM stdin;
CC000	CMV	B
CC001	MARGEM	B
CC002	VERBA	B
CC003	OPERACIONAL	B
CC004	REGULATORIO	B
CC006	ADICIONAL	B
CC007	PRECO_BASE	V
CC008	MARGEM	V
CC009	OPERACIONAL	V
CC010	FINANCEIRO	V
CC011	DESCONTO	V
\.


--
-- Data for Name: campo; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.campo (cod_campo, nome_campo) FROM stdin;
CP000	CODTERCHV
CP001	CODCNL
\.


--
-- Data for Name: campo_sequencia; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.campo_sequencia (cod_sequencia, cod_campo) FROM stdin;
SQ000	CP000
SQ000	CP001
\.


--
-- Data for Name: chave_contas; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.chave_contas (cod_chavecontas, desc_chavecontas) FROM stdin;
CC000	Chave 1
CC001	Chave 2
CC002	Chave 3
\.


--
-- Data for Name: condicao; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.condicao (cod_condicao, desc_condicao, cod_camada, cod_chavecontas, cod_tipovalor, escala_qtde, pos_neg, tip_base_vendas, mandatoria, estatistica) FROM stdin;
\.


--
-- Data for Name: condicao_camada_esquema; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.condicao_camada_esquema (cod_esquema_calculo, cod_condicao, cod_camada) FROM stdin;
\.


--
-- Data for Name: condicao_sequencia; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.condicao_sequencia (cod_condicao, cod_sequencia) FROM stdin;
\.


--
-- Data for Name: esquema_de_calculo; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.esquema_de_calculo (cod_esquema_calculo, tipo_base_vendas) FROM stdin;
EC000	B
EC001	V
\.


--
-- Data for Name: preco; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.preco (id, chave, data, cod_esquema_calculo, valor, tipo_base_venda) FROM stdin;
\.


--
-- Data for Name: sequencia; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.sequencia (cod_sequencia, nome_sequencia) FROM stdin;
SQ000	CODTERCHV/CODCNL
\.


--
-- Data for Name: tipo_valor; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.tipo_valor (cod_tipovalor, desc_tipovalor) FROM stdin;
TV000	PERCENTUAL
TV001	VALOR
TV002	CALCULADO
\.


--
-- Name: preco_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.preco_id_seq', 1, false);


--
-- Name: camada camada_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.camada
    ADD CONSTRAINT camada_pkey PRIMARY KEY (cod_camada);


--
-- Name: campo campo_cod_campo_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.campo
    ADD CONSTRAINT campo_cod_campo_key UNIQUE (cod_campo);


--
-- Name: campo_sequencia campo_sequencia_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.campo_sequencia
    ADD CONSTRAINT campo_sequencia_pkey PRIMARY KEY (cod_sequencia, cod_campo);


--
-- Name: chave_contas chave_contas_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.chave_contas
    ADD CONSTRAINT chave_contas_pkey PRIMARY KEY (cod_chavecontas);


--
-- Name: condicao_camada_esquema condicao_camada_esquema_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.condicao_camada_esquema
    ADD CONSTRAINT condicao_camada_esquema_pkey PRIMARY KEY (cod_esquema_calculo, cod_condicao, cod_camada);


--
-- Name: condicao condicao_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.condicao
    ADD CONSTRAINT condicao_pkey PRIMARY KEY (cod_condicao);


--
-- Name: condicao_sequencia condicao_sequencia_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.condicao_sequencia
    ADD CONSTRAINT condicao_sequencia_pkey PRIMARY KEY (cod_condicao, cod_sequencia);


--
-- Name: esquema_de_calculo esquema_de_calculo_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.esquema_de_calculo
    ADD CONSTRAINT esquema_de_calculo_pkey PRIMARY KEY (cod_esquema_calculo);


--
-- Name: preco preco_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.preco
    ADD CONSTRAINT preco_pkey PRIMARY KEY (id);


--
-- Name: sequencia sequencia_cod_sequencia_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.sequencia
    ADD CONSTRAINT sequencia_cod_sequencia_key UNIQUE (cod_sequencia);


--
-- Name: tipo_valor tipo_valor_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tipo_valor
    ADD CONSTRAINT tipo_valor_pkey PRIMARY KEY (cod_tipovalor);


--
-- Name: condicao cod_camada_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.condicao
    ADD CONSTRAINT cod_camada_fkey FOREIGN KEY (cod_camada) REFERENCES public.camada(cod_camada);


--
-- Name: condicao_camada_esquema cod_camada_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.condicao_camada_esquema
    ADD CONSTRAINT cod_camada_fkey FOREIGN KEY (cod_camada) REFERENCES public.camada(cod_camada);


--
-- Name: campo_sequencia cod_campo_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.campo_sequencia
    ADD CONSTRAINT cod_campo_fkey FOREIGN KEY (cod_campo) REFERENCES public.campo(cod_campo);


--
-- Name: condicao cod_chavecontas_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.condicao
    ADD CONSTRAINT cod_chavecontas_fkey FOREIGN KEY (cod_chavecontas) REFERENCES public.chave_contas(cod_chavecontas);


--
-- Name: condicao_sequencia cod_condicao_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.condicao_sequencia
    ADD CONSTRAINT cod_condicao_fkey FOREIGN KEY (cod_condicao) REFERENCES public.condicao(cod_condicao) ON DELETE CASCADE;


--
-- Name: condicao_camada_esquema cod_condicao_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.condicao_camada_esquema
    ADD CONSTRAINT cod_condicao_fkey FOREIGN KEY (cod_condicao) REFERENCES public.condicao(cod_condicao);


--
-- Name: condicao_camada_esquema cod_esquema_calculo_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.condicao_camada_esquema
    ADD CONSTRAINT cod_esquema_calculo_fkey FOREIGN KEY (cod_esquema_calculo) REFERENCES public.esquema_de_calculo(cod_esquema_calculo);


--
-- Name: campo_sequencia cod_sequencia_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.campo_sequencia
    ADD CONSTRAINT cod_sequencia_fkey FOREIGN KEY (cod_sequencia) REFERENCES public.sequencia(cod_sequencia) ON DELETE CASCADE;


--
-- Name: condicao_sequencia cod_sequencia_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.condicao_sequencia
    ADD CONSTRAINT cod_sequencia_fkey FOREIGN KEY (cod_sequencia) REFERENCES public.sequencia(cod_sequencia) ON DELETE CASCADE;


--
-- Name: condicao cod_tipovalor_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.condicao
    ADD CONSTRAINT cod_tipovalor_fkey FOREIGN KEY (cod_tipovalor) REFERENCES public.tipo_valor(cod_tipovalor);


--
-- Name: preco preco_cod_esquema_calculo_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.preco
    ADD CONSTRAINT preco_cod_esquema_calculo_fkey FOREIGN KEY (cod_esquema_calculo) REFERENCES public.esquema_de_calculo(cod_esquema_calculo);


--
-- PostgreSQL database dump complete
--

