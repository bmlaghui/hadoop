from impala.dbapi import connect
conn = connect('impala-coordinator.exmple.com', 28000,
  auth_mechanism="GSSAPI",
  kerberos_service_name='impala',
  use_http_transport=True,
  http_path='cliservice',
  auth_cookie_name='impala.auth')
cursor = conn.cursor()
cursor.execute("show databases")
res = cursor.fetchall()