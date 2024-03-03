{{
    config(
        materialized='view',
        schema= 'serving'
    )
}}
SELECT
a.inventory_id,
a.film_id as inventory_film_id,
a.store_id,
a.last_update,
b.film_id,
b.title,
b.description,
b.release_year,
b.language_id,
b.rental_duration,
b.rental_rate,
b.length,
b.replacement_cost,
b.rating,
b.last_update as film_last_update,
b.special_features,
b.fulltext
from {{ ref('raw_inventory')}} a
LEFT JOIN {{ ref('raw_film')}} b ON a.film_id = b.film_id
