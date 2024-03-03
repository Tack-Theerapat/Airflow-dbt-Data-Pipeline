
        {{
            config(
                materialized='table',
                schema= 'raw'
            )
        }}

        select
            rental_id,
rental_date,
inventory_id,
customer_id,
return_date,
staff_id,
last_update
        from {{ source('Ecom','rental') }}
        