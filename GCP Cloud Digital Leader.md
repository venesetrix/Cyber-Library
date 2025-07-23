# GCP Cloud Digital Leader Cert Prep Notes

## Digital Transformation with Google Cloud

Digital transformation = Using cloud platforms to create or modify business processes, culture and customer experiences to meet the needs of changing business and market dynamics.

The cloud = A metaphor for the network of data centers which store and compute information that’s available through the internet.

Digital transformation is...
* an ongoing process, not a one-time effort.
* more than simply migrating and shifting systems to the cloud for cost saving and convenience.

Cloud usage models:

* On-Premises - "No Cloud"
* Private Cloud - "Cloud hosted only for me"
* Public Cloud - "Cloud hosted seperately but for everyone"
* Hybrid Cloud - "Combine On-premises and Public Cloud"
* Multi-Cloud -  "Use multiple public clouds"

### Benefits of cloud computing

* Scalable
  * Scalable resources
  * Latest-Technology On-Demand
  * Accelerates deployment time
* Flexible
  * Access from anywhere
  * Scale up and down when needed
* Agile
  * Develop new applications
  * Repidly get them into production
  * No infrastructure worries
* Strategic value
  * Competitive advantages
  * Higher return in investment
  * Innovate and try new ideas
* Secure
  * Depth and breadth of mechanisms
  * Dedicated teams
* Cost-effective
  * Pay for what is used
  * No overbuilding data centers
  * IT staff to more strategic initiatives

### Cloud eras

| Cloud Era | Benefit |
| :---: | :--- |
| VM | No need to buy or operate hardware. |
| Infrastructure | Saved costs, faster development, better security, reduction of management load. |
| Transformation | Digitalization to all teams in an organisation through App and infrastructure modernization, data democratization, people connections and trusted transactions. |

### Googles transformation cloud

* Data - Be the best at understanding and using data with Google Cloud Data centric solutions.
* Open infrastructure - Want the best technology infrastructure by using open standards and open source
* Collaboration - Create the best hybrid workplace with **_Google Workspace_**.
* Trust - Know their data, systems and users are secure with better visibility and threat remediations powered by Google.
* Sustainable technology - Prioritize sustainability with Google clean cloud

### Google Cloud Adoption Framework

Serves as a map for cloud adoption through a set of actions around People, Process and Technology. 

* Cloud Maturity Assessment
* Actionable adoptiom program

## Foundational Cloud Concepts

### Total cost of ownership (TCO)

TCO analysis mean to compare On-Premise investments for infrastructure and operating with cloud operation costs as well as predicting future expenditures.

### Capital Expenditures (CapEx) vs. Operating expenses (OpEx)

Shift from capital expenditure to operating expenses.

CapEx means huge upfront costs for servers, equipment and software. Typically this means budgeting once a year. It means also, that you have to presume in details changes in upcoming timeframes.

OpEx means, that you're paying for what you use. This means constant monitoring of expenses.

### Private cloud, hybrid cloud and multi-cloud strategies

* Private cloud - Own or dedicated provider. Used, when there has already been large upfront investments or for compliance reasons.
* Hybrid cloud - On-Prem and one or Public cloud provider like Google. Most-Used.
* Multi-Cloud - Two or more Public cloud providers to use the key stengths of the different providers. 
  * Gartner: "81% of organizations are working with two or more public cloud providers
  * Flexera: "93% of enterprises have a multicloud strategy."
  * Benefits:
    * Access to the latest technologies of all cloud providers.
    * Modernize at the right pace
    * Improved return on investments
    * Flexibility through choice of tools
    * Avoid vendor lock-in's
    * Improve reliability and resiliency
    * Maintain regulatory compliance
    * Running apps at remote edge locations

### Cloud networking

__Network performance__

* Bandwidth = Measure of how much data a network can transfer in a given amount of time
* Latency = Amount of time it takes for data to travel from one point to another

__Google Cloud regions and zones__

7 Major locations:

* North America
* South America
* Europe
* Middle East
* Africa
* Asia
* Australia

A region comprises of zones. For example the Region europe-west2 comprises 3 different zones (europe-west2-a, europe-west2-b, europe-west2-c). Some services are in a "Multi-Region" construct like Cloud Storage which is in the Multi-Region called "Europe" and comprises London and Belgium for Geo-Redundancy.

Source: [Regions](https://cloud.google.com/about/locations)

__Google's edge network__

Network edge = Entry point to the network.

## Cloud Computing Models and Shared Responsibility

### Cloud Computing service models

| Model | Name | Benefits | Tradeoffs | Example Products |
| :---: | :--- | :------- | :-------- | :------- |
| IaaS | Infrastructure as a service | Provides Compute, Storage, Database and Network services. You lease the resources and pay only what you use. Saves procurement processes, physical spaces and CapEx. | Need to install and maintain software and OS. | **_Cloud Compute_**, **_Cloud Storage_** |
| PaaS | Platform as a service | No need to build and maintain the associated infrastructure and test the environments. Can use built-in software components. | Limited set of Platforms and Flexibility in Comparison to IaaS | **_Cloud Run_**, **_BigQuery_** |
| SaaS | Software as a service | Abstracts technology completely from the consumer. Only pay subscription fees. All technical issues are out-sourced. | Clear boundaries of usage. Only supports standard software solutions. | **_Google Workspace_** |

### Shared responsiblity model

Some security aspects are given to the cloud provider. The Cloud provider is responsible for the Security OF the Cloud and the customer is responsible for the Security IN the Cloud.

Gartner says that "99% of all cloud security failures will result from user error" ("Is the Cloud Secure?", Gartner, 2019).

General rule: If you configure or store it, you're responsible for securing it.

## The value of data

### Types of data

| Type| Description | Example |
| :---: | :--- | :--- |
| Structured Data | Highly organized and well-defined. Typically stored in a table. Easy to analyze | Spreadsheet or database |
| Semi-Structured Data | Organized into a hierarchy. Doesn't have a formal structure. Without full differentiation or order. | Emails, HTML, JSON, XML |
| Unstructured data | Doesn't have a predefined data model. | Text, Images, Audio, Video, Performance data. Can be analyzed via Maschine Learning and API i.e. **_Cloud Vision API_**. |

### Data Management Concepts

| Type| Description | Purpose of Use |
| :---: | :--- | :--- |
| Databases | Organized collection of data stored in tables. Types are relational (i.e. **_Cloud SQL_**, **_Spanner_**) and non-relational (i.e. **_Bigtable_**).  | Highly consistent and reliable. Suited for large amouts of structured data. |
| Data warehouses | Used for the analysis and reporting of structured and semi-structured data from multiple sources (i.e. **_BigQuery_**). | Analyze sales and identify trends. |
| Data lakes | Repository designed to ingest, store, explore, process and analyze any type or volume of raw data (i.e. **_Cloud Storage_**). Can store different types of data in its original format and thereby ignoring size limits. | Use and analyze raw data. |

### Sources of data

| Source | Description |
| :---: | :--- | 
| First-party data | Proprietary customer datasets that a business collects from customer or audience transactions. |
| Second-party data | First-party data from another organization inserted into a companies internal dataset. |
| Third-party data | Datasets collected and managed by organizations that don't directly interact with an organization's customers or business. |

### Data value chain

| Step | Description |
| :---: | :--- | 
| Data genesis | Initial generation of data. |
| Data collection | Extract data from the source system and bring it to a processing instance. |
| Data processing | Transform the data to a format you can gain insights from. |
| Data storage | Where the data lands, is found and is ready for analysis. |
| Data analysis | Assemble the data to a final solution or product. |
| Data activation | Present the data in form of Dashboards, Reports or automated actions. |

### Data Governance

Setting internal standards of how data is gathered, stored, processed and disposed of. It's also about granting access permissions and how to comply with external standards.

Benefits are:

* Makes data more valuable
* Helps users make better decisions
* Improves cost controls
* Enhances regulatory compliance
* Earns greater trust from customers and suppliers
* Helps manage risk
* Allows more personnel access to more data

## Google Cloud Data Management Solutions

### Unstructured data storage solutions

Cloud storage is an object storage. Object packaged format contains:

* Binary form of the actual data itself
* Relevant associated metadata
* Globally unique identifier

Typically video, audio or image files.

There are four storage classes:

| Storage class | Description |
| :---: | :--- |
| Hot data | Frequently accessed. |
| Nearline Storage | Infrequently accessed/Once per month like data archiving or backup. |
| Coldline Storage | Infrequently accessed/Once every 90 days. |
| Archive Storage | Access once a year for archiving. This is the cheapest option. Has a 365-day minimum storage duration. |

There's a feature called "Autoclass" which automatically transitions objects to appropriate storage classes based on each object's access pattern.


### Structured data storage solutions

**_Cloud SQL_** is a fully managed database service and supports the following engines:

* MySQL
* PostgreSQL
* SQL Server

The service applies patches/updates, manages backups and configures replications. It also encrypts customer data and includes a network firewall. **_DMS_** is a Database Migration Service to migrate production databases to Cloud SQL. It has greater than 99.95% availability.

**_Spanner_**

Google's own SQL RDMS for high availability and Input/Output Operations. Has unlimited scale and strong consistency as well as up to 99.999% availability. Handles replicas, sharding and transaction processing.

**_BigQuery_**

Is a fully-managed data warehouse. Provides two services in one: Storage and analytics. You can store Petabytes of data and analyze them with Machine Learning, Geospatial analysis and Business Intelligence. Data is encrypted at rest by default. Provides seamless integration with the partner ecosystem and works in a multicloud environment. Can export datasets to **_Vertex AI_** which is used to train the Machine Learning modules to generate SQL for BigQuery.

### Semi-structured data storage solutions

**_Firestore_**

A flexible and horizontally scalable NoSQL cloud database. Data will be stored in Documents which will be stored in collections. The documents support nested objects, numbers and strings as data type. It automatic scales and can be used offline in applications. 

**_Bigtable_**

Is a NoSQL big data database service. Handle massive workloads while having a consistent low latency and a high throughput.

Use Bigtable if you're working with more than 1 TB of data or needing high throughput.

### Choosing the right storage product

Is a combination of data type and business need.

Unstructured data -> Cloud Storage

Structured or Semi-Structured data:

* Transactional workload/Online Transaction Processing (OLTP)
  * SQL -> **_Cloud SQL_** or **_Spanner_**
  * NoSQL -> **_Firestore_**
* Analytical workload/Online Analytical Processing (OLAP) ->
  * SQL -> **_BigQuery_**
  * NoSQL -> **_Bigtable_**

### Database migration and modernization

* Lift and shift migration - Setup a DBMS in the cloud and transfer the DB's
* Managed database migration - Take MySQL/PostgreSQL/SQL Server DB's and migrate it to fully managed Cloud DB

**_Database Migration Service (DMS)_** easily migrate databases to Google Cloud.

**_Datastream_** can syncrhonize data across databases, storage systems and applications.

## Making Data Useful and Accessible

**_Looker_** is Google's Business Intelligence (BI) platform. It supports BigQuery along with more than 60 different SQL databases. Provides rich, interactive dashboards and reports. Is 100% web-based.

Streaming analytics is the processing and analyzing of data records continuously instead of in batches. This is used to analyze data in real time and provide insights into activities such as metering, servcer activity, geolocation of devices and website clicks. 

**_Pub/Sub_** is a Google service which ingests hundreds of millions of events per second. This happens in IoT-Devices. Pub/Sub is a distributed messaging service, that can receive these events and streams. It is an abbreviation of Publisher/Subscriper or Publish messages to subscribers. 

**_Dataflow_** is a Google service which unifies streaming and batch data analysis and build cohesive data pipelines. It extracts, transforms and loads (called "ETL") stream and batch data into data warehouses. A popular solution for pipeline design is **_Apache Beam_**. Fully-Managed and serverless.

## AI and ML Fundamentals

### Artificial Intelligence

The use of technologies to build machines and computers that are able to mimic cognitive functions associated with human intelligence. Uses techniques like deep learning, robotics, expert sytems, natural language processing and of course machine learning.

**Generative AI** = Producing new Files, Images, Videos, Audio and other data.

Business Analytics is creating dashboard on analyzing data from the past. AI/ML makes predictions for the future based on data from the past.

**_Explainable AI_** is Google Cloud's set of tools and frameworks to help understand and interpret prections made by ML models.

Googles AI principles:

* Bold innovation
* Responsible development and deployment
* Collaborative progress

### Machine Learning

A subset of AI that enables a machine to learn from data without being explicitly programmed.

Can solve following problems:

* Replacing or simplifying rule based systems (i.e. location based queries on Google Search)
* Automate processes (i.e. Pipelines of error checking, documentation and following actions)
* Understanding unstructured data (i.e. route incoming mail to the right department)
* Personalization (i.e. "Watch next" on Youtube)

There's a need to use high-quality data to train models. Characteristics are:

* Completeness - All the required information is present
* Uniqueness - Data does not have duplicate records
* Timeliness - Data is up-to-date
* Validity - Data conforms to a set of predefined standards and definitions, such as type and format 
* Accuracy - Correctness of the data, such as the accurate number of units sold
* Consistency - The data is uniform and doesn't contain any contradictory information

## Google Cloud's AI and ML Solutions

### BigQuery ML

Use SQL queries to create and execute machine learning models. Can work with **_Vertex AI_** (End-to-end AI and ML platform).

### Pre-trained APIs

Leverage ML models that have already been built and trained by Google. Can be deployed in the Cloud and On-Premise. Examples are:

* **_Vision API_** uses Googles ML models to identify faces, objects, sentiments and text in images and label or categorize them. 
* **_Natural Language API_** can identify syntax, sentiments in text. 
* **_Cloud Translation API_** converts text from one language to another.
* **_Speech-to-Text API_** converts audio to text for data processing.
* **_Text-to-Speech API_** converts text into audio.
* **_Video Intelligence API_** recognizes motion and action in video.

### AutoML

A no-code solution to build ML models on **_Vertex AI_**. Your own data can used with Vertex AI to create ML projects. Auto ML lets you build and train machine learning models from end to end by using graphical user interfaces. For example I use a set of images to custom train AutoML Vision and learn which images are correct and which are not.

### Custom models

Code own ML environment to have the control over the ML pipeline. You can use Vertex AI to built custom ML models with custom data while going down the following chain:

1. Gather data
2. Feature engineering
3. Build models
4. Deploy and monitor models

### TensorFlow

An end to end open source platform for machine learning. It has a flexible ecosystem of tools, libraries, and community resources that enable researchers to innovate in ML and developers to build and deploy ML powered applications. Can use **_Tensor Processing Units (TPU)_** which is a specific hardware to run ML-workloads.

### AI solutions

* Contact Center AI -  Models for speaking with customers and assisting human agents
* Document AI - Extracting and classifying information from unstructured documents such as invoices, receipts, forms, letters, and reports.
* Discovery AI for Retail - Select the optimal ordering of products on a retailer's e-commerce site.
* Cloud Talent Solution - Job search and talent acquisition capabilities, matches candidates to ideal jobs faster.

### Considerations when selecting AI/ML solutions

* Speed to production
* Differentiation / How customized does it have to be?
* Required Expertise
* Effort