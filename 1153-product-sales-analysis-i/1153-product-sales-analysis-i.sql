# Write your MySQL query statement below

select b.product_name, a.year, a.price from Sales as a left outer join Product as b
on a.product_id = b.product_id