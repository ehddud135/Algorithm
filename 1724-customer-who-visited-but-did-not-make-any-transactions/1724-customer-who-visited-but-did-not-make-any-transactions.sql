# Write your MySQL query statement below


select 
-- *
a.customer_id as customer_id, count(*) as count_no_trans 
from Visits as a left outer join Transactions as b on a.visit_id = b.visit_id
where amount is null and b.transaction_id is null
group by a.customer_id
;