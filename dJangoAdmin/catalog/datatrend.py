import pyodbc 
import pandas.io.sql as sql

def datatrend(user_email):
  #user_email = 'btaylor@newdayusa.com'
  server = '10.203.1.105\\alpha' 
  database = 'test_yang' 
  username = 'webuser' 
  password = 'Changeme1' 
  cnxn = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
  
  query = """
  
    select dbo.StartOfWeek(date) StartOfWeek, a.PersonID,b.Employee_Code,b.FstNm,b.LstNm,b.WaterFallDivision,Team_Desc,b.Email,
    	sum(case when [EventName] = 'Router Call' then 1 else 0 end) as [RouterCall] ,
    	sum(case when [EventName] = 'Transfer In' then 1 else 0 end) as [TransferIn] ,
    	sum(case when [EventName] = 'Transfer Out' then 1 else 0 end) as [TransferOut] ,
    	sum(case when [EventName] = 'Web Lead' then 1 else 0 end) as [WebLead] ,
    	sum(case when [EventName] = 'Credit Pull' then 1 else 0 end) as [Capture] ,
    	sum(case when [EventName] = 'Pitch' then 1 else 0 end) as [Pitch] ,
    	sum(case when [EventName] = 'Appraisal Order' then 1 else 0 end) as [AO] ,
    	sum(case when [EventName] = 'Appraisal Order' and ProductCat = 'Cash Out' then LoanAMount else 0 end) as  LoanAMount_AO,
    	sum(case when [EventName] = 'Fund' and ProductCat = 'Cash Out' then 1 else 0 end) as [CO Close] ,
    	sum(case when [EventName] = 'Fund' and ProductCat  = 'Cash Out' then LoanAMount else 0 end) as  LoanAMount_CO,
    	sum(case when [EventName] = 'IP' and ProductCat = 'Cash Out' then 1 else 0 end) as  IP,
    	sum(case when [EventName] = 'IP' and ProductCat = 'Cash Out' then LoanAMount else 0 end) as  LoanAMount_IP 
    	
    from AEPerformanceReport_1 as a    
    inner join topDownAELookupTable b on a.PersonID = b.PersonID 
    WHERE a.Date >=   DATEADD(wk, DATEDIFF(wk,0,GETDATE()), 0) -2 -28*3 -7
    and   a.date <=  DATEADD(wk, DATEDIFF(wk,0,GETDATE()), 0)  -2 
    and b.Email = 'aaa@aaa.com'
    and b.WaterFallDivision in ('AVP','DM','WEB','TV','AIT - NFL Rookie','Digital - Router') 
    and b.ActiveCd = 'Y' and MarketingChannel not in ('IRRRL','Internal')
    group by a.PersonID,b.Employee_Code,b.FstNm,b.LstNm,b.WaterFallDivision,Team_Desc,dbo.StartOfWeek(date) ,b.Email
     
  """
  query = query.replace('aaa@aaa.com',user_email)  

  queryResult = sql.read_sql(query, cnxn)
 
  return queryResult

 