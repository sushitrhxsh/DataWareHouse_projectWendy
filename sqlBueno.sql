DROP TABLE IF EXISTS public.dimClient;

CREATE TABLE IF NOT EXISTS public.dimClient
(
	id_client integer NOT NULL,
	first_name varchar(100) NOT NULL,
	country varchar(50) NOT NULL,
	job_title varchar(50) NOT NULL,
	CONSTRAINT client_pkey PRIMARY KEY (id_client)
);

DROP TABLE IF EXISTS public.dimProduct;

CREATE TABLE IF NOT EXISTS public.dimProduct
(
	id_product integer NOT NULL,
	product varchar(150) NOT NULL,
	CONSTRAINT product_pkey PRIMARY KEY (id_product)
);

DROP TABLE IF EXISTS public.dimDate;

CREATE TABLE IF NOT EXISTS public.dimDate
(
	id_date integer NOT NULL,
	date_sale date NOT NULL,
	CONSTRAINT date_pkey PRIMARY KEY (id_date)
);

DROP TABLE IF EXISTS public.dimCard;

CREATE TABLE IF NOT EXISTS public.dimCard
(
	id_card integer NOT NULL,
	card varchar(150) NOT NULL,
	CONSTRAINT card_pkey PRIMARY KEY (id_card)
);

DROP TABLE IF EXISTS public.factSale;

CREATE TABLE IF NOT EXISTS public.factSale
(
	id_sale integer NOT NULL,
	id_client integer NOT NULL,
	id_card integer NOT NULL,
	id_date integer NOT NULL,
	id_product integer NOT NULL,
	sale_paid numeric(13,2) NOT NULL,
	articles integer NOT NULL,
	CONSTRAINT sale_pkey PRIMARY KEY (id_sale)
);