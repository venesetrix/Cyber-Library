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

## Modernize Infrastructure in the Cloud

### Terms

| Term | Description |
| :----- | :----- |
| Workload | A specific application, service, or capability that can be run in the Cloud or on premises like containers, databases or virtual machines. |
| Retired | Remove a workload from the platform. |
| Retained | Intentionally kept workload. |
| Rehosted | The migration of a workload to the Cloud without changing anything in the workload's code or architecture. Often referred to as "Lift-and-Shift". |
| Replatform | Migrating a workload to the Cloud while making some changes to the workloads code or architecture. Often referred to as "Move-and-Improve". |
| Refactored | Refers to the process of changing the code of a workload.  |
| Reimagined | The process of rethinking how an organization uses technology to achieve its business goals. |

### Benefits of running compute workloads in the cloud

* Total cost of ownership (TCO) - Measure of the total cost of a system or solution over its lifetime.
* Scalability - Scale up and down by demand
* Reliability - High reliability 
* Security
* Flexibility - Choose the cloud services you need whenever you need it.
* Abstraction - Provide management layer without concern about the details.


### Virtual machine

Virtualization is a form of resource optimization that lets multiple systems run on the same hardware. **_Compute engine_** is Google's IaaS solution. Can be configured like a physical server by specifing the amount of CPU and memory needed.

Virtual machines can be created through **_Google's Cloud Console_** (Web based tool) or the **_Google Cloud CLI_** (command-line interface).

Will be billed by the second with the one minute minimum. Automatically applied sustained-use discounts the longer they run. Compute Engine also offers committed-use discounts (1- or 3-year period).

Costs can be reduced, in some cases by up to 90%, by choosing Preemptible or Spot VMs to run the job. Compute Engine might preemptively interrupt Spot VMs to reclaim the capacity at any time. Spot VMs differ from Preemptible VMs by offering more features.

* Spot VMs
  * More features
  * No maximum runtime
  * Same pricing
* Preemptible VMs
  * Less features
  * Runtime up to 24h
  * Same pricing

### Containers

Provide isolated environments to run software services and optimize resources from one piece of hardware. Well suited for a microservices based architecture. Communicate with each other through APIs or other lightweight communication methods, such as REST or gRPC.

### Managing containers

Kubernetes, originally developed by Google, is an open-source platform for managing containerized workloads and services. **_Google Kubernetes Engine (GKE)_** is a managed Kubernetes service in the Cloud. Provides Web-GUI and API to manage containers. 

**_Cloud Run_** is a fully managed serverless platform to deploy and run containerized applications. Takes care of scaling and managing the infrastructure automatically. Ideal for running stateless applications that need to scale up and down quickly in response to traffic.

### Serverless computing

Means that resources like compute power are automatically provisioned in the background as needed. Businesses provide the code for whatever function they want and the public Cloud provider does everything else. Google's Function as a service (FaaS) are:

* **_Cloud Run_** - Containerized application hosting.
* **_Cloud Run functions_** - Hosting simple, single-purpose functions that are attached to events.
* **_App Engine_** - Service to build and deploy web applications.

## Modernizing Applications in the cloud

### Benefits of modern cloud application development

Modern cloud applications are typically built as a collection of microservices and are deployed to the cloud with all advantages like scalability, pay-as-you-go pricing model, resiliency and security. 

### Rehosting legacy applications in the cloud

**_Google Cloud VMware Engine_** helps migrating existing VMware workloads to the cloud without rearchitect the applications or retool operations. With that you can use other Google services.

For organizations with legacy applications on Oracle, Google Cloud offers **_Bare Metal Solution_**.

### Application programming interfaces (APIs)

An API is a set of instructions that lets different software programs communicate with each other. Provides a standardized and predictable way for them to exchange data and interact. 

**_Apigee API Management_** is Googles API management service to operate APIs with enhanced scale, security and automation.

### Hybrid and multi-cloud

**_GKE Enterprise_** is a production-ready platform for running Kubernetes applications across multiple cloud environments. It provides a consistent way to manage Kubernetes, clusters, applications and services regardless of where they are running. GKE enterprise can run Kubernetes clusters on Google Cloud, AWS, Azure, and other public clouds.

## Trust and Security with Google Cloud

### Terms

| Term | Description |
| :----- | :----- |
| Privileged access | Grants specific users access to a broader set of resources. |
| Least Privilege | Advocates granting users only the access they need to perform their job responsibilities. |
| Zero-trust architecture | No user or device can be trusted by default. Every user and device must be authenticated and authorized before accessing resources. |
| Security by default | Integrating security measures into systems and applications from the initial stages of development. |
| Security posture | Overall security status of a cloud environment. |
| Cyber resilience | An organization's ability to withstand and recover quickly from cyber attacks. |
| Firewall | A network device that regulates traffic based on predefined security rules. |
| Encryption | The process of converting data into an unreadable format by using an encryption algorithm. |
| Decryption | Uses an encryption key to restore encrypted data back to its original form. |

### Cloud security components

| Concept | Description |
| :----- | :----- |
| Confidentiality | Keeping important information safe and secret. |
| Identity | Keeping data accurate and trustworthy. |
| Availability | Systems and services are always accessible and ready for use by the right people when needed. |
| Controls | THe measures and processes implemented to manage and mitigate security risks. Most important are Authentication, Access and Awareness. |
| Compliance | Ensuring that security practices and measures align with established standards and guidelines. |

### Cloud security versus traditional on-premises security

* Location - Local vs. cloud provider
* Responsibility - Securitng Data/Apps/Access vs. Infrastructure/Network
* Scalability/Elasticity - Long cycles vs. agile
* Maintenance/Updates - Self vs. Provider
* Expenditure - CapEx vs. OpEx

### Cybersecurity Threats

| Threat | Description |
| :----- | :----- |
| Social Engineering | Skillfully craft tailored emails and mimic authenticity to deceive their targets. |
| Physical damage | Damage to hardware components, power disruptions, or natural disasters such as floods. |
| Malware, viruses and ransomware | Aim to disrupt operations, inflict damage, or gain unauthorized access to computer systems. |
| Vulnerable 3rd party systems | Imagine inviting a trusted ally into your domain, only to discover that they inadvertently compromise your security. |
| Misconfiguration | When errors arise during the setup or configuration of resources, which inadvertently exposes sensitive data and systems to unauthorized access. |

## Google's Trusted Infrastructure

### Data centers

Google operates over 30 data centers worldwide. Has custom hardware and software with features like Tamper-evident hardware, secure boot, Hardware-based encryption.

Measures the success through Power Usage Effectiveness (PUE) score.

### Secure storage

Automatic (free, built-in) encryption of data at rest in Google Cloud. With **_Cloud Key Management Service (Cloud KMS)_** the customer can use his own key. Data in transit will be encrypted as well, especially when it comes to outside connections. Google Cloud uses memory encryption for data in use. 

### Identity

Leveraged by '3A': 

* Authentication - Validating identity by using 2-step-verification (2SV or 2FA or MFA).
* Authorization - What a user is allowed to do by rules, hierarchy or responsibilites.
* Auditing/Accounting - Collecting and analysing logs of user activity and system events.

Can be used by **_Identity and Management (IAM)_**.

### Network security

Implement Zero-trust security model by using Google's **_BeyondCorp Enterprise_** which analyzes credentials and context.

Secure connections between on-premises datacenters and Google Cloud can be established by using **_Cloud VPN_** or **_Cloud Interconnect_**.

Networks inside of Google Cloud can be secured by **_Firewall_** and **_Virtual Private Cloud_**.

Customers can protect themselves from DDoS-Attacks by using **_Cloud Armor_**.

With automation tools like **_Terraform_**, **_Jenkins_** and **_Cloud Build_** customers can assure to create secure and reliable cloud environments.

### Security operations

Google Cloud's **_Security Command Center (SCC)_** provides a centralized view of the security posture and helps to identify and fix vulnerabilites.

**_Cloud Logging_** is a service to collect and analyze security logs from your entire Google Cloud environment.

Other aspects of SecOps are Incident Response and Awareness measures.

## Google Cloud's Trust Principles and Compliance

### Trust Principles and Transparency Reports

* You own your data, not Google
* Google does not sell customer data to third parties
* Google Cloud does not use customer data for advertising
* All customer data is encrypted by default
* We guard against insider access to your data
* We never give any government entity "backdoor" access
* Our privacy practices are audited against international standards

Transparency reports,Independent Audit transparency, 3rd party audits and certifications proof these principles.

### Data residency and data souvereignty

* Data souvereignty - The legal concept that data is subject to the laws and regulations of the country where it resides.
* Data residency - Refers to the physical location where data is stored or processed.

Can be implemented by choosing the correct data center region. You can also use Organization Policy constraints coupled with IAM configuration to prevent accidental data storage in the wrong region. **_VPC service controls_** let you restrict network access to data based on defined perimeters.

### Industry and regional compliance

The **_Compliance resource center_** hub provides detailed information on the regional and industry related certifications and compliance standards Google Cloud satisfy.

**Link:** [Compliance Resource Center](https://cloud.google.com/security/compliance)

In addition, the **_Compliance Reports Manager_** offers access to critical compliance resources at no extra cost like ISO/IEC certificates, SOC reports and self-assessments.

**Link:** [Compliance Reports Manager](https://cloud.google.com/security/compliance/compliance-reports-manager)

## Scaling with Google Cloud Operations

### Fundamentals of cloud financial governance

To manage cloud costs effectively, a partnership across finance, technology, and business functions is required. The central team would consist of several experts who ensure that best practices are in place across the organization and that there's visibility into the ongoing cloud spend. **_Center of excellence_** is a centralized hub within an organization for that.

On a daily or weekly basis, organizations should monitor and analyze their cloud usage and costs. Then, on a weekly or monthly basis, the finance team should analyze the results, charge back the costs through the appropriate teams, and determine whether any changes are needed to ensure that the organization's cloud spend is optimized.

### Cloud financial governance best practices

* Identify who manage cloud costs.
  * Defining clear ownership for projects.
  * Sharing cost views with the departments and teams that are using cloud resources.
  * Creating multiple budgets with meaningful alerts.
* Understand invoices versus cost management tools
  * An invoice is a document that is sent by a cloud service provider to a customer to request payment for the services that were used.
  * A cost management tool is software to help track, analyze, and optimize cloud spend.
* Use Google Cloud's cost management tools
  * Capture what cloud resources are being used, by whom, for what purpose, and at what cost.
  * Determine who will be responsible for monitoring that information, who will be involved in managing costs, and how the spending information will be reported on an ongoing basis.
  * Set up the cadence and format for ongoing communication with main cloud stakeholders.

The **_Pricing Calculator_** lets you estimate how changes to cloud usage will affect costs. **Link:** [Pricing Calculator](https://cloud.google.com/products/calculator)

### Using the resource hierarchy to control access

The **_Google Cloud resource hierarchy_** is a powerful tool that can be used to control access to cloud resources. 

Google Cloud’s resource hierarchy contains four levels, and starting from the bottom up they are:

1. Resources
2. Projects
3. Folders
4. Organization node

A policy is a set of rules that define who can access a resource an what they can do with it. Policies can be defined on levels 2 to 4. Some services can even add policies on resource level.

### Controlling cloud consumtion

Google Cloud offers several tools to help control cloud consumption:

* **_Resource quota policies_** - Set limits on the amount of resources that can be used by a project or user.
* **_Budget threshold rules_** - Set alerts to be informed when your cloud costs exceed a certain threshold.
* **_Cloud Billing reports_** - Offer a reactive method to help you track and understand what you’ve already spent on Google Cloud resources and provide ways to help optimize your costs. Data can be exported to **_BigQuery_** for further analysis.

## Operational Excellence and Reliability at Scale

### Fundamentals of cloud reliability

DevOps is a software development approach that emphasizes collaboration and communication between development and operations teams to enhance the efficiency, speed, and reliability of software delivery.

One particular concept within the DevOps framework is **_Site Reliability Engineering_**, or SRE, which ensures the reliability, availability, and efficiency of software systems and services deployed in the cloud.

Monitoring is the foundation of product reliability. There are "Four Golden Signals" that measure a systems's performance and reliability:

| Signal | Description |
| :----- | :----- |
| Latency | Measures how long it takes for a particular part of a system to return a result. |
| Traffic | Measures how many requests reach your system. |
| Saturation | Measures how close to capacity a system is. |
| Errors | Events that measure system failures or other issues. |

Three main concepts in site reliability engineering are:

| Concept | Abbreviation | Description |
| :----- | :-----: | :----- |
| Service-level indicators  | SLI | Measurements that show how well a system or service is performing. |
| Service-level objectives  | SLO | The goals that we set for a system's performance based on SLIs. |
| Service-level agreements  | SLA | Agreements between a cloud service provider and its customers. They outline the promises and guarantees regarding the quality of service. |

### Designing resilient infrastructure and processes

Key design considerations:

| Consideration | Description | Advantages | 
| :----- | :----- | :----- |
| Redundancy | Duplicating critical components or resources to provide backup alternatives. | Enhances system reliability and mitigates the impact of single points of failure. |
| Replication | Creating multiple copies of data or services and distributing them across different servers or locations. | Ensures redundancy and fault tolerance by allowing systems to continue functioning even if certain components or servers fail. |
| Regions | Distributing resources across regions. | Improves resilience and reduces the risk of prolonged service interruptions. |
| Scalable infrastructure | Dynamic allocation and deallocation of resources based on workload fluctuations by autoscaling mechanisms. | Ensuring that services remain available and responsive during peak periods or sudden spikes in traffic. |
| Backups | Regular backups of critical data and configurations. | Ensure that if data loss, hardware failures, or cyber-attacks occur, organizations can restore their systems to a previous state. |

### Modernizing operations by using Google Cloud

Observability involves collecting, analyzing, and visualizing data from various sources within a system to gain insights into its performance, health, and behavior.

**_Google Cloud Observability_**, is a comprehensive set of monitoring, logging, and diagnostics tools:

| Tool | Description |
| :----- | :----- |
| **_Cloud Monitoring_** | Collects metrics, logs, and traces from your applications and infrastructure, and provides you with insights into their performance, health, and availability. It also lets you create alerting policies to notify you when metrics, health check results, and uptime check results meet specified criteria. |
| **_Cloud Logging_** | Collects and stores all application and infrastructure logs. |
| **_Cloud Trace_** | Helps identify performance bottlenecks in applications. It collects latency data from applications, and provides insights into how they’re performing. |
| **_Cloud Profiler_** | It continuously gathers CPU usage and memory-allocation information from production applications and provides insights into how applications are using resources. |
| **_Error Reporting_** | Counts, analyzes, and aggregates the crashes in running cloud services in real-time. A centralized error management interface displays the results with sorting and filtering capabilities. Error Reporting supports email and mobile alerts notification through its API. |

### Google Cloud customer care

| Service Level | Description |
| :----- | :----- |
| Basic | Free and is included for all Google Cloud customers. It provides access to documentation, community support, Cloud Billing Support, and Active Assist recommendations. **_Active Assist_** is the portfolio of tools used in Google Cloud to generate insights and recommendations to help you optimize your cloud projects. |
| Standard | Recommended for workloads under development. Offers unlimited individual access to English-speaking support representatives during working hours, 5 days a week.  Provides access to the **_Cloud Support API_**, which lets you integrate Cloud Customer Care with your organization's customer relationship management (CRM) system. |
| Enhanced | Designed for workloads in production. Support is available 24/7 in a selection of languages, and initial response times are quicker than those provided by Standard Support. Offers technical support escalations and third-party technology support to help you resolve multi-vendor issues. |
| Premium | Designed for enterprises with critical workloads. It features the fastest response time, Customer Aware Support, and a dedicated Technical Account Manager. Offers credit for the Google Cloud Skills Boost training platform, an event management service for planned peak events, operational health reviews, and customer aware support. |

Both the Enhanced and Premium support plans offer Value-Add Services that are available for additional purchase. **Link:** [Support](https://cloud.google.com/support)

### The life of a support case



### Sustainability with Google Cloud


