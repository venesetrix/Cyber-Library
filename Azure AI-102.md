# Azure AI Engineer Associate (AI-102) Prep Notes

## Plan Azure AI Solutions

### Vision Services

| Name | Description |
| :----- | :----- |
| Azure AI Vision | Pre-built image and video analysis |
| Custom Vision | Train custom image classifiers |
| Face API | Face detection and recognition |
| Document Intelligence | Extract text from documents |

### Language and Speech Services

| Name | Description |
| :----- | :----- |
| Azure AI language | Text analysis, sentiment, NER |
| Azure AI Translator | 100+ languages translation |
| Azure OpenAI Service | Advanced language models |
| Speech-to-Text/Text-to-Speech | Extract text from documents |
| Speaker Recognition | |
| Speech Translation | | 

### Decision and Search Services

| Name | Description |
| :----- | :----- |
| Content Safety | Content moderation |
| Azure AI Search | Cognitive search solution |
| Knowlege Mining | Extract inisights from content |
| Azure AI Model Inference | Flagship model inference |
| Azure AI Agent Service | Generative AI with real-world data |

### AI Development Environment

| Name | Description |
| :----- | :----- |
| Azure AI Foundry Portal | Central hub for AI service development, Model deployment, monitoring, resource management and scaling. |
| Azure AI CLI and SDK's | CLI's, SDKs, REST APIs |

### Key Principles

* Fairness
* Reliability and Safety
* Privacy and Security
* Inclusiveness
* Transparency
* Accountability

## Design AI Architectures

### Types of Business requirements

* Functional - What the AI System should do like image classification
* Performance - Latency, Throughput, Scalability
* Data - Data needs of the AI System like volume and variety
* Security - Access control, data protection and compliance
* Cost - Budgets

### Architectural patterns

* Batch Processing - Process data in large chunks
* Real-time Inference - Process data as it arrives
* Hybrid Architectures - Combine both
* Edge AI

![Azure AI Reference Architecture](./Resources/Images/AI-102-Reference-Arch.png)

### Configure services AI for Performance

* Compute Targets (CPU or GPU) - Select the appropriate compute resource
* Model Optimization - Reduce model size and complexity
* Hyperparameter Tuning
* Deployment

### Monitoring

* Azure Monitor - Track performance and metrics
* Bottleneck Identification - Identify performance bottlenecks
* Alerts - Setting up alerts to detect performance degradation

### Caching

* API Response caching
* Model Prediction caching
* Azure Cache for Redis - Implement caching

### Load Testing

* Performance under stress
* Load Testing Tools like Azure Load Testing and Application Insights

## Manage and Secure AI Solutions
TBD

### Implement Monitoring and Logging

Main tool is Azure Monitor with uses

* **Metrics** - Numerical values, that describe the performance of Azure resources overt time like CPU usage, memory consumption, network traffic and so on. It's stored in a time-series database and analyzed using Portal, CLI, SDK and API's.
* **Logs** - Detailed records of events that occur like application logs. It's stored in Log Analytics Workspaces and analyzed usinig KQL.

### Apply security best practices to AI workloads

* Access Control - Use Built-in or Custom Roles and Entra ID Priviledged Identity Management
* Secure Endpoints and Identities - Like Private Links and Managed Identities
* Encryption at Rest - Azure Storage Service Encryption or Customer-Managed Key
* Encryption in Transit - TLS certificats and using Azure Key Vault for Secrets Management
* AAA - Conditional Access, RBAC, Azure Monitor

Authentication in general follows the following flow: Private Link + Entra ID > Managed Identity > API Keys.

## Moderate Text Content

### Content safety categories

| Category | Description | Severity Levels | Numeric Values |
| :----- | :----- | :----- | :----- |
| Hate | Content promoting hate or violence against groups | Safe, Low, Medium, High | 0,2,4,6 |
| Sexual | Sexually explicit or suggestive content | Safe, Low, Medium, High | 0,2,4,6 |
| Violence | Depictions or descriptions of violence | Safe, Low, Medium, High | 0,2,4,6 |
| Self-Harm | Content related to self-injury or suicide | Safe, Low, Medium, High | 0,2,4,6 |

### Automated compliance workflows

Components:

* Input triggers
* Integration with Azure AI Content Safety
* Decision logic based on moderation scores
* Actions for approved, flagged and rejected content

## Moderate Image Content

### Implement Image moderation

Moderate unsafe content at scale with Content Safety and Vision API.

| Feature| Content Safety API | Vision API |
| :----- | :----- | :----- |
| Harm Categories | Yes (hate, sexual, violence, self-harm) | No |
| Adult/Racy Detection | Yes | Yes |
| Image + Text Support | Yes | No (image only) |
| Use Case | Deep content filtering | Lightweight adult flagging |

[Vision Studio Link](https://portal.vision.cognitive.azure.com/)

Results of the Vision API will have a text, polygons ("boundingPolygons") around the identified text and a confidence score.  

## Analyze Images with Pre-Built Models
TBD

## Create Custom Computer Vision Models
TBD

## Analyze Video Content
TBD

## Process Text with Azure AI Language
TBD

## Build Conversational AI with Bots
TBD

## Implement Speech-to-Text Solutions
TBD

## Deploy Text-to-Speech Solutions
TBD

## Translate and Localize Content
TBD

## Deploy Knowledge Mining Solutions
TBD

## Extract Data from Documents
TBD

## Leverage Azure OpenAI Services
TBD

## Optimize Generative AI Models
TBD

## Implement Responsible AI Practices
TBD

## Monitor and Optimize Azure AI Solutions
TBD


## Exam Tips

* Focus on matching between specific Azure AI services to business requirements (compare (Azure AI Architecture Framework)[https://learn.microsoft.com/en-us/azure/architecture/browse/?terms=Azure%20ai])
* Expect scenario-based questions where choosing the correct service involves considering Scalability, Security, Compliance, Cost and Performance trade-offs.