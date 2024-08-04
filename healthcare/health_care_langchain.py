from dotenv import load_dotenv
import os
from langchain_community.graphs import Neo4jGraph

load_dotenv()

AURA_INSTANCENAME = os.environ["AURA_INSTANCENAME"]
NEO4J_URI = os.environ["NEO4J_URI"]
NEO4J_USERNAME = os.environ["NEO4J_USERNAME"]
NEO4J_PASSWORD = os.environ["NEO4J_PASSWORD"]
NEO4J_DATABASE = os.environ["NEO4J_DATABASE"]
AUTH = (NEO4J_USERNAME, NEO4J_PASSWORD)


kg = Neo4jGraph(
    url=NEO4J_URI,
    username=NEO4J_USERNAME,
    password=NEO4J_PASSWORD,
    database=NEO4J_DATABASE,
)

cypher = """
  MATCH (n) 
  RETURN count(n) as numberOfNodes
  """

result = kg.query(cypher)
print(f"There are {result[0]['numberOfNodes']} nodes in this graph.")


# Match only the Providers nodes by specifying the node label
cypher = """
  MATCH (n:HealthcareProvider) 
  RETURN count(n) AS numberOfProviders
  """
res = kg.query(cypher)
print(f"There are {res[0]['numberOfProviders']} Healthcare Providers in this graph.")


# return the names of the Healthcare Providers
cypher = """
  MATCH (n:HealthcareProvider) 
  RETURN n.name AS ProviderName
  """
res = kg.query(cypher)
print("Healthcare Providers:")
for r in res:
    print(r["ProviderName"])

# list all patients in the graph
cypher = """
  MATCH (n:Patient) 
  RETURN n.name AS PatientName
  LIMIT 10
  """
res = kg.query(cypher)
print("Patients:")
for r in res:
    print(r["PatientName"])


# list all Specializations in the graph
cypher = """
  MATCH (n:Specialization) 
  RETURN n.name AS SpecializationName
  """
res = kg.query(cypher)
print("Specializations:")
for r in res:
    print(r["SpecializationName"])


# list all Locations in the graph
cypher = """
  MATCH (n:Location) 
  RETURN n.name AS LocationName
  """
res = kg.query(cypher)

print("Locations:")
for r in res:
    print(r["LocationName"])


# list all patients treated by a specific provider
cypher = """
  MATCH (hp:HealthcareProvider {name: 'Dr. Smith'})-[:TREATS]->(p:Patient) 
  RETURN p.name AS PatientName
  """
res = kg.query(cypher)
print("Patients treated by Dr. Smith:")
for r in res:
    print(r["PatientName"])

# And More...
# list all Specializations of a specific provider
cypher = """
  MATCH (hp:HealthcareProvider {name: 'Dr. Smith'})-[:SPECIALIZES_IN]->(s:Specialization) 
  RETURN s.name AS SpecializationName
  """
res = kg.query(cypher)
print("Specializations of Dr. Smith:")
for r in res:
    print(r["SpecializationName"])

# 4. List All Healthcare Providers Located in a Specific Location
cypher = """
  MATCH (hp:HealthcareProvider)-[:LOCATED_AT]->(l:Location {name: 'Houston'}) 
  RETURN hp.name AS ProviderName
  """
res = kg.query(cypher)
print("Healthcare Providers located Houston:")
for r in res:
    print(r["ProviderName"])


# 5. List All Patients Treated by a Provider Specializing in a Specific Specialization
cypher = """
  MATCH (hp:HealthcareProvider)-[:TREATS]->(p:Patient), 
        (hp)-[:SPECIALIZES_IN]->(s:Specialization {name: 'Cardiology'}) 
  RETURN p.name AS PatientName
  """
res = kg.query(cypher)
print("Patients treated by a Cardiologist:")
for r in res:
    print(r["PatientName"])

# 6. List All Healthcare Providers Located in a Specific Location Specializing in a Specific Specialization
cypher = """
  MATCH (hp:HealthcareProvider)-[:LOCATED_AT]->(l:Location {name: 'Houston'}), 
        (hp)-[:SPECIALIZES_IN]->(s:Specialization {name: 'Cardiology'}) 
  RETURN hp.name AS ProviderName
  """
res = kg.query(cypher)
print("\nCardiologists located in Houston:")
for r in res:
    print(r["ProviderName"])

# 7. List All Patients Treated by a Provider Specializing in a Specific Specialization Located in a Specific Location
cypher = """
  MATCH (hp:HealthcareProvider)-[:TREATS]->(p:Patient), 
        (hp)-[:SPECIALIZES_IN]->(s:Specialization {name: 'Cardiology'}), 
        (hp)-[:LOCATED_AT]->(l:Location {name: 'Houston'}) 
  RETURN p.name AS PatientName
  """
res = kg.query(cypher)
print("\nCardiology patients treated by providers in Houston:")
for r in res:
    print(r["PatientName"])

# list all patients who have Parkinson's Disease
cypher = """
  MATCH (p:Patient {condition: 'Migraine'}) 
  RETURN p.name AS PatientName
  """
res = kg.query(cypher)
print("\n \n****Patients with Migrane: ***")
for r in res:
    print(r["PatientName"])
