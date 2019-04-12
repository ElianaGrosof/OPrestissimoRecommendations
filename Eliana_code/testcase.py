#teach myself shit - convert example to pandas
#then convert that into my use case
#https://gallery.technet.microsoft.com/scriptcenter/Script-to-convert-Multiple-7d28b523
#these are the key https://www.liquidweb.com/kb/how-to-check-the-mysql-version/

#sql - convert into multi-row format
select t.mailid,fn.data
into temp
from
table1 t
cross apply sample_split(t.to_mail,',') fn

#pandas
data[(mailid)]
