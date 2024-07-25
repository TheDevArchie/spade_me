--
-- PostgreSQL database dump
--

-- Dumped from database version 15.7 (Homebrew)
-- Dumped by pg_dump version 15.7 (Homebrew)

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
-- Name: games; Type: TABLE; Schema: public; Owner: spud
--

CREATE TABLE public.games (
    game_id integer NOT NULL,
    winner_id integer,
    num_of_rounds integer
);


ALTER TABLE public.games OWNER TO spud;

--
-- Name: games_game_id_seq; Type: SEQUENCE; Schema: public; Owner: spud
--

CREATE SEQUENCE public.games_game_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.games_game_id_seq OWNER TO spud;

--
-- Name: games_game_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: spud
--

ALTER SEQUENCE public.games_game_id_seq OWNED BY public.games.game_id;


--
-- Name: player; Type: TABLE; Schema: public; Owner: spud
--

CREATE TABLE public.player (
    player_id integer NOT NULL,
    name character varying(30) NOT NULL
);


ALTER TABLE public.player OWNER TO spud;

--
-- Name: player_player_id_seq; Type: SEQUENCE; Schema: public; Owner: spud
--

CREATE SEQUENCE public.player_player_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.player_player_id_seq OWNER TO spud;

--
-- Name: player_player_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: spud
--

ALTER SEQUENCE public.player_player_id_seq OWNED BY public.player.player_id;


--
-- Name: scores; Type: TABLE; Schema: public; Owner: spud
--

CREATE TABLE public.scores (
    score_id integer NOT NULL,
    player_id integer,
    game_id integer,
    score integer
);


ALTER TABLE public.scores OWNER TO spud;

--
-- Name: scores_score_id_seq; Type: SEQUENCE; Schema: public; Owner: spud
--

CREATE SEQUENCE public.scores_score_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.scores_score_id_seq OWNER TO spud;

--
-- Name: scores_score_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: spud
--

ALTER SEQUENCE public.scores_score_id_seq OWNED BY public.scores.score_id;


--
-- Name: games game_id; Type: DEFAULT; Schema: public; Owner: spud
--

ALTER TABLE ONLY public.games ALTER COLUMN game_id SET DEFAULT nextval('public.games_game_id_seq'::regclass);


--
-- Name: player player_id; Type: DEFAULT; Schema: public; Owner: spud
--

ALTER TABLE ONLY public.player ALTER COLUMN player_id SET DEFAULT nextval('public.player_player_id_seq'::regclass);


--
-- Name: scores score_id; Type: DEFAULT; Schema: public; Owner: spud
--

ALTER TABLE ONLY public.scores ALTER COLUMN score_id SET DEFAULT nextval('public.scores_score_id_seq'::regclass);


--
-- Name: games games_pkey; Type: CONSTRAINT; Schema: public; Owner: spud
--

ALTER TABLE ONLY public.games
    ADD CONSTRAINT games_pkey PRIMARY KEY (game_id);


--
-- Name: player player_pkey; Type: CONSTRAINT; Schema: public; Owner: spud
--

ALTER TABLE ONLY public.player
    ADD CONSTRAINT player_pkey PRIMARY KEY (player_id);


--
-- Name: scores scores_pkey; Type: CONSTRAINT; Schema: public; Owner: spud
--

ALTER TABLE ONLY public.scores
    ADD CONSTRAINT scores_pkey PRIMARY KEY (score_id);


--
-- PostgreSQL database dump complete
--

