--
-- PostgreSQL database dump
--

-- Dumped from database version 17.3
-- Dumped by pg_dump version 17.3

-- Started on 2025-03-04 10:48:34

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
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
-- TOC entry 218 (class 1259 OID 16553)
-- Name: ev_manufacturers; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.ev_manufacturers (
    id regclass NOT NULL,
    make character varying(100) NOT NULL
);


ALTER TABLE public.ev_manufacturers OWNER TO postgres;

--
-- TOC entry 217 (class 1259 OID 16552)
-- Name: ev_manufacturers_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.ev_manufacturers_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.ev_manufacturers_id_seq OWNER TO postgres;

--
-- TOC entry 4881 (class 0 OID 0)
-- Dependencies: 217
-- Name: ev_manufacturers_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.ev_manufacturers_id_seq OWNED BY public.ev_manufacturers.id;


--
-- TOC entry 220 (class 1259 OID 16560)
-- Name: ev_models; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.ev_models (
    id integer NOT NULL,
    manufacturer_id integer NOT NULL,
    model character varying(100) NOT NULL,
    year_produced integer NOT NULL
);


ALTER TABLE public.ev_models OWNER TO postgres;

--
-- TOC entry 219 (class 1259 OID 16559)
-- Name: ev_models_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.ev_models_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.ev_models_id_seq OWNER TO postgres;

--
-- TOC entry 4882 (class 0 OID 0)
-- Dependencies: 219
-- Name: ev_models_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.ev_models_id_seq OWNED BY public.ev_models.id;


--
-- TOC entry 224 (class 1259 OID 16660)
-- Name: ev_specs; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.ev_specs (
    spec_id integer NOT NULL,
    trim_id integer NOT NULL,
    all_electric_range integer,
    battery_capacity_kwh numeric(5,2),
    charge_time_240v_hrs numeric(5,2),
    dc_connector_type character varying(100),
    peak_charge_rate_kw numeric(5,2),
    peak_charge_time_minutes integer,
    kw_power_output numeric(5,2),
    battery character varying(50),
    battery_voltage integer
);


ALTER TABLE public.ev_specs OWNER TO postgres;

--
-- TOC entry 223 (class 1259 OID 16659)
-- Name: ev_specs_spec_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.ev_specs_spec_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.ev_specs_spec_id_seq OWNER TO postgres;

--
-- TOC entry 4883 (class 0 OID 0)
-- Dependencies: 223
-- Name: ev_specs_spec_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.ev_specs_spec_id_seq OWNED BY public.ev_specs.spec_id;


--
-- TOC entry 222 (class 1259 OID 16572)
-- Name: ev_trims; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.ev_trims (
    id regclass NOT NULL,
    ev_model_id integer NOT NULL,
    "trim" character varying(100) NOT NULL
);


ALTER TABLE public.ev_trims OWNER TO postgres;

--
-- TOC entry 221 (class 1259 OID 16571)
-- Name: ev_trims_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.ev_trims_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.ev_trims_id_seq OWNER TO postgres;

--
-- TOC entry 4884 (class 0 OID 0)
-- Dependencies: 221
-- Name: ev_trims_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.ev_trims_id_seq OWNED BY public.ev_trims.id;


--
-- TOC entry 4710 (class 2604 OID 16587)
-- Name: ev_manufacturers id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ev_manufacturers ALTER COLUMN id SET DEFAULT nextval('public.ev_manufacturers_id_seq'::regclass);


--
-- TOC entry 4711 (class 2604 OID 16643)
-- Name: ev_models id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ev_models ALTER COLUMN id SET DEFAULT nextval('public.ev_models_id_seq'::regclass);


--
-- TOC entry 4713 (class 2604 OID 16663)
-- Name: ev_specs spec_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ev_specs ALTER COLUMN spec_id SET DEFAULT nextval('public.ev_specs_spec_id_seq'::regclass);


--
-- TOC entry 4712 (class 2604 OID 16603)
-- Name: ev_trims id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ev_trims ALTER COLUMN id SET DEFAULT nextval('public.ev_trims_id_seq'::regclass);


--
-- TOC entry 4715 (class 2606 OID 16589)
-- Name: ev_manufacturers ev_manufacturers_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ev_manufacturers
    ADD CONSTRAINT ev_manufacturers_pkey PRIMARY KEY (id);


--
-- TOC entry 4719 (class 2606 OID 16645)
-- Name: ev_models ev_models_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ev_models
    ADD CONSTRAINT ev_models_pkey PRIMARY KEY (id);


--
-- TOC entry 4727 (class 2606 OID 16665)
-- Name: ev_specs ev_specs_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ev_specs
    ADD CONSTRAINT ev_specs_pkey PRIMARY KEY (spec_id);


--
-- TOC entry 4723 (class 2606 OID 16605)
-- Name: ev_trims ev_trims_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ev_trims
    ADD CONSTRAINT ev_trims_pkey PRIMARY KEY (id);


--
-- TOC entry 4721 (class 2606 OID 16610)
-- Name: ev_models unique_ev_model; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ev_models
    ADD CONSTRAINT unique_ev_model UNIQUE (manufacturer_id, model, year_produced);


--
-- TOC entry 4725 (class 2606 OID 16630)
-- Name: ev_trims unique_ev_trim; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ev_trims
    ADD CONSTRAINT unique_ev_trim UNIQUE (ev_model_id, "trim");


--
-- TOC entry 4717 (class 2606 OID 16586)
-- Name: ev_manufacturers unique_make; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ev_manufacturers
    ADD CONSTRAINT unique_make UNIQUE (make);


--
-- TOC entry 4728 (class 2606 OID 16590)
-- Name: ev_models ev_models_manufacturer_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ev_models
    ADD CONSTRAINT ev_models_manufacturer_id_fkey FOREIGN KEY (manufacturer_id) REFERENCES public.ev_manufacturers(id);


--
-- TOC entry 4730 (class 2606 OID 16666)
-- Name: ev_specs ev_specs_trim_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ev_specs
    ADD CONSTRAINT ev_specs_trim_id_fkey FOREIGN KEY (trim_id) REFERENCES public.ev_trims(id);


--
-- TOC entry 4729 (class 2606 OID 16646)
-- Name: ev_trims ev_trims_ev_model_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ev_trims
    ADD CONSTRAINT ev_trims_ev_model_id_fkey FOREIGN KEY (ev_model_id) REFERENCES public.ev_models(id);


-- Completed on 2025-03-04 10:48:34

--
-- PostgreSQL database dump complete
--

