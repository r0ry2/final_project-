import psycopg2
from cassandra.cluster import Cluster
from influxdb_client import InfluxDBClient

# -------- PostgreSQL --------
try:
    pg_conn = psycopg2.connect(
        host="127.0.0.1",
        port="5432",
        database="postgres",
        user="admin",
        password="admin"
    )
    pg_conn.close()
    print("PostgreSQL OK ✅")
except Exception as e:
    print("PostgreSQL Error:", e)

# -------- Cassandra --------
try:
    cluster = Cluster(['127.0.0.1'], port=9042)
    session = cluster.connect()
    cluster.shutdown()
    print("Cassandra OK ✅")
except Exception as e:
    print("Cassandra Error:", e)

# -------- InfluxDB --------
try:
    influx_url = "http://localhost:8086"
    influx_token = "XRqh1k6Gk9u-hYPr2HeMgqhqS41JcffhAizaVXucP5VfMcKS7g0rCmWvlUBQ0EW-WshAsyA7jIcO3qPikMgjxg=="
    influx_org = "my-org"

    client = InfluxDBClient(url=influx_url, token=influx_token, org=influx_org)
    client.close()
    print("InfluxDB OK ✅")
except Exception as e:
    print("InfluxDB Error:", e)
