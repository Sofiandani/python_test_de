WITH prep_ventes_meuble AS(
SELECT
    client_id,
    SUM(prod_price * prod_qty) AS ventes_meuble
FROM    
    TRANSACTION
INNER JOIN
    PRODUCT_NOMENCLATURE AS PRODUCT
ON
    TRANSACTION.prod_id = PRODUCT.product_id
WHERE
    product_type = 'MEUBLE'
    AND date BETWEEN DATE('2019-01-01') AND DATE('2019-12-31')
),

prep_ventes_deco AS(
SELECT
    client_id,
    SUM(prod_price * prod_qty) AS ventes_deco
FROM    
    TRANSACTION
INNER JOIN
    PRODUCT_NOMENCLATURE AS PRODUCT
ON
    TRANSACTION.prod_id = PRODUCT.product_id
WHERE
    product_type = 'DECO'
    AND date BETWEEN DATE('2019-01-01') AND DATE('2019-12-31')
)

SELECT
    COALESCE(prep_ventes_meuble.client_id, prep_ventes_deco.client_id) AS client_id,
    ventes_meuble,
    ventes_deco
FROM
    prep_ventes_meuble
FULL JOIN
    prep_ventes_deco
ON
    prep_ventes_meuble.client_id = prep_ventes_deco.client_id