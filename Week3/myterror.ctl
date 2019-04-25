load data
infile 'myterror.csv'
insert into table myteror
fields terminated by ','
trailing nullcols(
    eventid char,
    iyear char,
    imonth char,
    country char,
    country_txt char,
    region char,
    region_txt char,
    provstate char,
    city char,
    latitude char,
    longitude char
)