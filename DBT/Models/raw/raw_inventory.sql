
        {{
            config(
                materialized='table',
                schema= 'raw'
            )
        }}

        select
            inventory_id,
film_id,
store_id,
last_update
        from {{ source('Ecom','inventory') }}
        