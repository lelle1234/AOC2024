-- note that sample file must be ',' delimited, sed -e "s/   /,/g"
with t (x,y) as (SELECT * FROM EXTERNAL '/database/config/db2inst1/test1.txt' (x INT, y int) USING (DELIMITER ','))
select sum(abs(x-y))
from (select row_number() over (order by x) as rn, x from t)
join (select row_number() over (order by y) as rn, y from t)
    using (rn);
    
