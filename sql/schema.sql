create table if not exists tcg_products (
    id uuid default uuid_generate_v4() primary key,
    product_id text not null,
    name text not null,
    category text not null,
    price numeric,
    currency text,
    last_updated timestamp with time zone default now(),
    unique (product_id, category)
); 