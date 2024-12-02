-- note that sample file must be ',' delimited, sed -e "s/   /,/g"
with t (x,y) as (SELECT * FROM EXTERNAL '/database/config/db2inst1/sqlinput.txt' (x INT, y int) USING (DELIMITER ',')) 
select sum(x * (select count(case when t1.x=t2.y then 1 end) from t t2)) 
from t t1;

-- conditional count above was faster than (select count(1) from t t2 where t1.x=t2.y)

