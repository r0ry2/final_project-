# check_databases.py
import psycopg2
from cassandra.cluster import Cluster
from influxdb_client import InfluxDBClient

# -------- PostgreSQL --------
print("=== PostgreSQL Databases ===")
try:
    pg_conn = psycopg2.connect(host="127.0.0.1", port="5433",
                               database="postgres", user="postgres", password="postgres")
    cur = pg_conn.cursor()
    cur.execute("SELECT datname FROM pg_database;")
    for r in cur.fetchall():
        print(r[0])
    cur.close()
    pg_conn.close()
except Exception as e:
    print("PostgreSQL Error:", e)

# -------- Cassandra --------
print("\n=== Cassandra Keyspaces ===")
try:
    cluster = Cluster(['127.0.0.1'], port=9042)
    session = cluster.connect()
    rows = session.execute("SELECT keyspace_name FROM system_schema.keyspaces;")
    for r in rows:
        print(r.keyspace_name)
    cluster.shutdown()
except Exception as e:
    print("Cassandra Error:", e)

# -------- InfluxDB --------
print("\n=== InfluxDB Buckets ===")
try:
    influx_url = "http://localhost:8086"
    influx_token = "mmQlCZwUl0xocT_CMRh2lS2MXQpKXTYe68KoEImCHHrLMt39iRtzgDK15YlMHqjE-v36GJnnhIqRWMcod7YOvQ=="
    influx_org = "myorg"
    client = InfluxDBClient(url=influx_url, token=influx_token, org=influx_org)
    buckets = client.buckets_api().find_buckets().buckets
    for b in buckets:
        print(b.name)
except Exception as e:
    print("InfluxDB Error:", e)
