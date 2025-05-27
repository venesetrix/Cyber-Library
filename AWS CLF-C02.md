# AWS CLF-C02 Cert Prep Notes

## Cloud Computing Concepts

Cloud Computing = "On-demand delivery of compute, database storage, application, and other IT resources

Advantages of Cloud Computing:
* Trade capital expense for variable expense
* Benefit from massive economies of sale
* Stop guessing capacity
* Increase speed and agility
* Stop spending money running and maintaining data centers
* Go global in minutes

### AWS Well-Architected Framework (aka "How do I setup a good Cloud Architecture")
* Avoid unnecessary costs
  * Use only what you need. 
  * Reserve ressources. 
  * Cost-Monitoring
* Reliability
  * Disaster recovery
  * Redundancy
* Effiziency
  * Go global in minutes
* Security
  * Best practices should be automated
  * Data should always be protected
  * Traceability
  * Manage access
* Operational Excellence
  * Document everything
  * Refine operational procedures
  * Anticipate failure
  * Update processes
  * Learn from failures
        

### AWS Cloud Adoption Frameword (CAF)
=Best practices to migrate On-Premises IT to the Cloud

Value Chains
* Technological transformation: Use cloud to migrate and modernize IT
* Process transformation: Digitize, automate and optimize business operations
* Organizational transformation: Reimagine how your business and technology teams work together
* Product transformation: Reimagine the business model by creating new value propositions

Perspectives and Foundational Capabilities
* Business - Cloud investments accelerate digital transformation and business outcomes
* People - Culture of growth, learning and change
* Governance - Maximize organizational benefits while minimizing cloud-transformation-related risks
* Platform - Scalable hybrid cloud praltforms, implement cloud-native solutions, modernize existing infrastructure
* Security - CIA of cloud data and workloads
* Operations - Cloud services deliver business need
    
Cloud Transformation Journey (CTJ) - Is different on every company
* Envision phase - Envision goals and opportunities
* Align Phase - Identify capability gaps across the six CAF perspectives and dependencies
* Launch Phase - Pilot initiatives and incremental business value demonstration
* Scale Phase - Expand pilots and scaling up

## Security and Compliance

### Shared Responsibility Model

* Security OF the Cloud -> AWS
* Security IN the Cloud -> Customer

### Security in the Cloud Pillar of Well-Architected-Framework
* IAM
* Detective controls
* Infrastructure protection
* Data protection
* Incident response
    
Governance = The process of creating and enforcing decisions within an organization

### Providing Access in AWS
* Principle of Least Privilege
* IAM
  * WHO (users, workloads, roles)
  * CAN ACCESS (permissions with IAM policies)
  * WHAT (resources)
* Identities in AWS
  * Human identities / Workforce identities (Humans in own organization)
  * Workload identities
  * Federated identities: SSO, AWS IAM Identity Center (old: AWS Single Sign-On) with SAML 2.0
* Controlling Access to AWS
  * Roles
  * Policies
* Traffic Control
  * Security Groups Network Access control lists (NACLs)

![Security Groups versus Network Access Control lists](/Resources/Images/AWS-CLF-02-2-SecGroups-vs-NSG.png)

![New reference](./Resources/Images/AWS-CLF-02-2-SecGroups-vs-NSG.png)



### Security Services
| Name | Description |
| :---: | :---------- |
| AWS Systems Manager | Manage AWS resources. Visualize and operate on multiple AWS services from one place. Create logical groups of resources. |
| AWS WAF | Classic WAF. Can be deployed in CloudFront (CDN) or API Gateway. |
| AWS Shield | DDoS Protection and automatic mitigations. Tier: Standard (Free). Tier: Advanced (24/7 access to AWS DDoS response team, Integrates into AWS WAF). Financial protection against DDoS-related spikes. Can be integrated into CloudFront and Route 53. |
| Amazon Inspector | Security assessment service for applications. Automatically assesses for exposure, vulnerabilities and deviations from best practices. Preset or custom policies. Reports. |
| AWS Trusted Advisor | Scans infrastructure and advises on how you follow AWS best practices based on five categories: cost optimization, performance, security, fault tolerance, service limits. Provides recommendations. Seven core checks for free: S3 bucket permissions, security groups, IAM use, MFA on root account, Elastic Block Store public snapshots, Relational Database Service (RDS) public snapshots, service limits. More Checks available together with notifications, automated actions (AWS CloudWatch) and AWS Support API access. |
| Amazon GuardDuty | 24/7 threat detection by machine learning, anomaly detection and threat intelligence. |
| AWS Artifact | Download AWS security and compliance documents and independent software vendor (ISV) compliance reports. |
| AWS Secrets Manager | Saves all secrets like passwords, credentials, tokes, access key and integrates with key AWS Services. |
Amazon CloudWatch | Monitors application performance. Set alarms and automated actions. |
| AWS CloudTrail | Generates audit trails. |
| AWS Audit Manager | Automates evidence collection to generate audit-ready reports to prove system compliance for audits. |
| AWS Config | Detailed views of AWS resource configurations. Tracks how configurations and relationships between resources change over time. Can monitor changes and automatically alert. |