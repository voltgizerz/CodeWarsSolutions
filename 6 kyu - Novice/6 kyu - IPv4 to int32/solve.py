def ip_to_int32(ip):
  ip = ip.split(".")
  con =""
  for i in range(len(ip)):
    con += (bin(int(ip[i]))).zfill(10).replace("0b","")
  return int(con,2) 