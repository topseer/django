import pyodbc 
import pandas.io.sql as sql

def numOfRouterCalls(startdate,enddate,user_email):
  server = '10.203.1.105\\alpha' 
  database = 'test_yang' 
  username = 'webuser' 
  password = 'Changeme1' 
  cnxn = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
  cursor = cnxn.cursor()
  query = """
    select Count(*) Router 
    from AEPerformanceReport_1 as a 
    inner join topDownAELookupTable as b 
    on a.Date >= '@@@startDate@@@'
    and a.Date <= '@@@endDate@@@'
    and a.PersonID = b.PersonId 
    and b.Email = 'aaa@aaa.com'
    and EventName = 'Router Call'
  """
  query = query.replace('aaa@aaa.com',user_email)
  query = query.replace('@@@startDate@@@',startdate)
  query = query.replace('@@@endDate@@@',enddate)
  queryResult = sql.read_sql(query, cnxn)
    
  num_Router_lstWk = queryResult["Router"][0]
  return num_Router_lstWk


def numOfWebLeads(startdate,enddate,user_email):
  server = '10.203.1.105\\alpha' 
  database = 'test_yang' 
  username = 'webuser' 
  password = 'Changeme1' 
  cnxn = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
  cursor = cnxn.cursor()
  query = """
    select Count(*) Router 
    from AEPerformanceReport_1 as a 
    inner join topDownAELookupTable as b 
    on a.Date >= '@@@startDate@@@'
    and a.Date <= '@@@endDate@@@'
    and a.PersonID = b.PersonId 
    and b.Email = 'aaa@aaa.com'
    and EventName = 'Web Lead'
  """
  query = query.replace('aaa@aaa.com',user_email)
  query = query.replace('@@@startDate@@@',startdate)
  query = query.replace('@@@endDate@@@',enddate)
  queryResult = sql.read_sql(query, cnxn)
    
  numOfWebLeads = queryResult["Router"][0]
  return numOfWebLeads


def numOfAOs(startdate,enddate,user_email):
  server = '10.203.1.105\\alpha' 
  database = 'test_yang' 
  username = 'webuser' 
  password = 'Changeme1' 
  cnxn = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
  cursor = cnxn.cursor()
  query = """
    select Count(*) Router 
    from AEPerformanceReport_1 as a 
    inner join topDownAELookupTable as b 
    on a.Date >= '@@@startDate@@@'
    and a.Date <= '@@@endDate@@@'
    and a.PersonID = b.PersonId 
    and b.Email = 'aaa@aaa.com'
    and EventName = 'Appraisal Order'
  """
  query = query.replace('aaa@aaa.com',user_email)
  query = query.replace('@@@startDate@@@',startdate)
  query = query.replace('@@@endDate@@@',enddate)
  queryResult = sql.read_sql(query, cnxn)
    
  numOfAOs = queryResult["Router"][0]
  return numOfAOs



def numOfIPs(startdate,enddate,user_email):
  server = '10.203.1.105\\alpha' 
  database = 'test_yang' 
  username = 'webuser' 
  password = 'Changeme1' 
  cnxn = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
  cursor = cnxn.cursor()
  query = """
    select Count(*) Router 
    from AEPerformanceReport_1 as a 
    inner join topDownAELookupTable as b 
    on a.Date >= '@@@startDate@@@'
    and a.Date <= '@@@endDate@@@'
    and a.PersonID = b.PersonId 
    and b.Email = 'aaa@aaa.com'
    and EventName = 'IP'
  """
  query = query.replace('aaa@aaa.com',user_email)
  query = query.replace('@@@startDate@@@',startdate)
  query = query.replace('@@@endDate@@@',enddate)
  queryResult = sql.read_sql(query, cnxn)
    
  numOfIPs = queryResult["Router"][0]
  return numOfIPs



def numOfFunds(startdate,enddate,user_email):
  server = '10.203.1.105\\alpha' 
  database = 'test_yang' 
  username = 'webuser' 
  password = 'Changeme1' 
  cnxn = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
  cursor = cnxn.cursor()
  query = """
    select Count(*) Router 
    from AEPerformanceReport_1 as a 
    inner join topDownAELookupTable as b 
    on a.Date >= '@@@startDate@@@'
    and a.Date <= '@@@endDate@@@'
    and a.PersonID = b.PersonId 
    and b.Email = 'aaa@aaa.com'
    and EventName = 'Fund'
  """
  query = query.replace('aaa@aaa.com',user_email)
  query = query.replace('@@@startDate@@@',startdate)
  query = query.replace('@@@endDate@@@',enddate)
  queryResult = sql.read_sql(query, cnxn)
    
  numOfFunds = queryResult["Router"][0]
  return numOfFunds  


def numOfPitch(startdate,enddate,user_email):
  server = '10.203.1.105\\alpha' 
  database = 'test_yang' 
  username = 'webuser' 
  password = 'Changeme1' 
  cnxn = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
  cursor = cnxn.cursor()
  query = """
    select Count(*) Router 
    from AEPerformanceReport_1 as a 
    inner join topDownAELookupTable as b 
    on a.Date >= '@@@startDate@@@'
    and a.Date <= '@@@endDate@@@'
    and a.PersonID = b.PersonId 
    and b.Email = 'aaa@aaa.com'
    and EventName = 'Pitch'
  """
  query = query.replace('aaa@aaa.com',user_email)
  query = query.replace('@@@startDate@@@',startdate)
  query = query.replace('@@@endDate@@@',enddate)
  queryResult = sql.read_sql(query, cnxn)
    
  numOfPitch = queryResult["Router"][0]
  return numOfPitch