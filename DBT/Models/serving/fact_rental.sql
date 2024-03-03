{{
    config(
        materialized='view',
        schema= 'serving'
    )
}}
SELECT
r.rental_id,
r.rental_date,
r.inventory_id,
r.customer_id,
r.return_date,
r.staff_id,
r.last_update,
p.payment_id,
p.payment_date,
p.amount,
p.customer_id AS payment_customer_id,
p.staff_id AS payment_staff_id,
p.rental_id AS payment_rental_id,
i.inventory_id AS inventory_inventory_id,
i.film_id AS inventory_film_id,
i.store_id AS inventory_store_id,
i.last_update AS inventory_last_update,
f.film_id AS film_film_id,
f.title AS film_title,
f.description AS film_description,
f.release_year AS film_release_year,
f.language_id AS film_language_id,
f.rental_duration AS film_rental_duration,
f.rental_rate AS film_rental_rate,
f.length AS film_length,
f.replacement_cost AS film_replacement_cost,
f.rating AS film_rating,
f.last_update AS film_last_update,
f.special_features AS film_special_features,
f.fulltext AS film_fulltext,
c.customer_id AS customer_customer_id,
c.store_id AS customer_store_id,
c.first_name AS customer_first_name,
c.last_name AS customer_last_name,
c.email AS customer_email,
c.address_id AS customer_address_id,
c.activebool AS customer_activebool,
c.create_date AS customer_create_date,
c.last_update AS customer_last_update,
c.active AS customer_active
from {{ ref('raw_rental') }} r
LEFT JOIN {{ ref('raw_payment') }} p ON r.rental_id = p.rental_id
LEFT JOIN {{ ref('raw_customer') }} c ON r.customer_id = c.customer_id
LEFT JOIN {{ ref('raw_inventory') }} i ON r.inventory_id = i.inventory_id
LEFT JOIN {{ ref('raw_film') }} f ON i.film_id = f.film_id
