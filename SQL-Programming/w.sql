
sel top 10 * from tablename;

--search for a column in a database
sel * from dbc.columns where databasename='xx' and columnname like ('%app%')

--case statement
case when x=1 then 'apple'
    when x=2 then 'orange'
    else 'other' end as fruit;

--window function
--get clients with highest acct balance for each state
--state > clients > accounts > account balances
sel state_nm, client_nm, sum(acct_balance) as total_acct_balance
from tablename
group by 1,2,3
qualify row_number() over (
    partition by state_nm order by total_acct_balance desc
    ) = 1; --picks up the first row for each state

--working with volatile and sandbox tables
create volatile table tablename2 as (
    sel * from tablename; 
) with data on commit preserve rows;
--) with data primary index (xx) on commit preserve rows;

create table tablename2 as (
    sel * from tablename; 
) with data primary index (emp_id, cust_id);

grant select on tablename to username1, username2; 

drop table tablename2, tablename3;

select rolename from dbc.rolemembers where grantee='user-id'


--working with dates
--extract year from a datetime
cast(extract(year from sale_datetime)) as varchar(4) = '2021'

--extract months from a date
startdate - CURRENT_DATE months(4) as tenure_in_months
startdate - CURRENT_DATE year(4) as tenure_in_years

--customized dates in reporting
drop table dates;
create volatile table dates as (
    select 
        cast('2013-07-01' as date) as start_13m
        cast('2014-07-31' as date) as end_13m
) with data on commit preserve rows;
--usage
e.dt between dates.start_13m and dates.end_13m

--first day of the month
add_months(date1 - extract(day from date1) + 1, 0)
add_months(e.dt - e.dy_nbr +1, 0)

--begenning and end of month
add_months((date - extract(day from date) + 1), 0) as bom, 
add_months((date - extract(day from date) + 1), -1) as beg_of_prior_month, 
add_months(last_day(date), 0) as eom, 
add_months(last_day(date), -1) as end_of_prior_month, 


--removing leading or trailing characters
sel emp_id, 
    cast(emp_id as integer), 
    trim(leading '0' from emp_id),
    trim(trailing '0' from emp_id),
    emp_nm
from employee_table;

--adding leading or trailing characters
cast(lpad(cast(columnname as varchar(50)), 25, '0') as varchar(50))
cast(
    lpad(
        cast(
            columnname as bigint
        ) as varchar(20)
    ) 11 , '0'
) as varchar(20)


--casting
cast(columnname as decimal(15,2))

