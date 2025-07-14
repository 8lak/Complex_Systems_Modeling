
Two main types
batch: only process data in interval
streaming: process in real time

Data pipeline consist of a DAG(Directed Acyclic Graph) essential a path. Goes from point A to B and cannot reach B to A via the same edges. Consist of Sources and sink. 

DAG approach is just an implementation of several design patterns. I.E ETL, ELT, Change data Capture

ETL (Extract Transform  and Load)![[Screenshot 2025-06-05 at 5.52.10 PM.png]]

We copy the source data over so as to not have any errors in business data, we then have our transformation which would be some sort of logic done on the data and we can have several transformations that lead to the same sink. These are patterns for Data warehouse solutions (DWH). Finally if using a batch we can orchestrate which involves scheduling a time and interval for data to be processed. Good for consistent transformation rules on data. 

Pattern 2 ELT (Extract Load and Transform)![[Screenshot 2025-06-05 at 6.02.23 PM.png]]

Tries to maintain raw data for as long as possible for novel manipulations in transform stage. CDC is built on top of ELT designs. Best suited with cloud solutions for transform stage since we are dealing with lots of raw data that is unclean manipulation requires computation which if on-prem may prove costly. 


Change Data Capture (CDC)![[Screenshot 2025-06-05 at 6.14.33 PM.png]]

In EL DAG record version in DWH stage with timestamp. Inside DWH stage determine latest version of data for Transform dag retrieval and usage. 


Pattern 4 - EtLT 

Where our t is a mini transform that essentially just tidies the data with deduplication, 


![[Screenshot 2025-06-05 at 6.17.25 PM.png]]


What is a pipeline 

![[Screenshot 2025-06-05 at 6.30.44 PM.png]]

Batch injestion goes into Operational data store (ODS) which could be MySQL and your stream ingestion could go into message hub powered by a nonSQL solutiojn like mongo DB. Either scenario feeds into a Master data management (MDM) to create one single master reference source for all business logic or transformations. This can then flow into data lakes or data warehouse solutiouns. 