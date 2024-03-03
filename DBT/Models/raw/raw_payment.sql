
        {{
            config(
                materialized='table',
                schema= 'raw'
            )
        }}

        select
            payment_id,
customer_id,
staff_id,
rental_id,
amount,
payment_date
        from {{ source('Ecom','payment') }}
        