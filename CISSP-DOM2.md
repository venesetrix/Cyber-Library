# CISSP Domain 2 - Asset Security

## Terms

| Term | Description |
| :----- | :----- |
| Asset classification | Categorize then in terms of criticality and sensitivity |
| Data Criticality | How important is the data for the business |
| Data Sensitivity | Level of confidentiality |

## Data life-cycle requirements
* Storage - "data at rest"
  * Subject to unauthorized access, copying, deletion or removel
  * Encryption
  * Access permissions
  * Strong authentication
  * Physical security
  * Inventory of information stored and their media
  * Administrative controls like two-person control.
* Transportation
  * Constant presence of someone assigned to escort or guard the asset
  * Strong Chain of custody during transport
* Transmission - "data in transit"
  * Vulnerable to eavestropping and interception
  * Strong authentication controls
  * Encryption TLS, SSH, Hardware encryption devices
* Use - "Data in use"
  * Destined to be read, transformed or modified and returned back to storage

## Classification Handling

### Commercial/Private
| Name | Description |
| :----- | :----- |
| Public | Nonsensitive |
| Private | Privacy information like PHI, PII |
| Confidential | Sensitive for the organisation like financial information, personnel action… |
| Proprietary | Formulas, processes |

### Military/government
| Name | Description |
| :----- | :----- |
| Top Secret | Exceptionally grave danger to the nation |
| Secret | Serious damage to the nation |
| Confidential | Could cause damage to the nation |
| Unclassified | Could cause undesirable effects if available to public |

## Asset inventory
Tracking assets based on asset value, criticality, sensitivity.
* Maintaining knowlege of an assets location and status
* Give special attention to high-value assets
* Tangible assets
  * Securing from theft, damage, misuse
  * Ensure critical maintenance
  * Replacing component parts
  * Managing the asset's life cycle
* Intangible assets
  * Must be measured constantly

## Asset Management
Ensure that resources are provided to people/processes that need them, when needed, in the right state.
* Secure provisioning - Processes taht ensure that only authorized properly identified and authenticated entities access information and systems
  * Verifing an entity's identity (authentication)
  * Verifyfining the entity's need for access (authorization)
  * Creating the proper access tokens (usernames, passwords, …)
  * Securely providing entities with authentication and access tokens
  * Assingning the correct authorizations based on need-to-know, job position or role, security clearance …
  * Conducting ongoing privilege management

## Managing data lifecycle
NIST SP 800-37 Rev. 2 - Information life cycle = "Stages through which information passes … as creation/collection, processing, dissemination, use, storage, disposition, destruction, deletion."
* Managing an organizations data
  * Assign sensitivity and criticality labels
  * Assigning security measures based on the labels
  * Designating the roles responsible for managing.
* Access may be granted based on:
  * Security clearance
  * Need-to-know
  * Training
  * Statutory requirements

### Roles
| Name | Description |
| :----- | :----- |
| Data owner | Indiviual who has ultimate resposibility. Typically an executive, senior manager, vice president, department head. His resposibilities are: Develop a system or data security plan, Identify access requirements, Implement and manage the security controls |
| Data controller | Determines the purposes and use of data within an organization (senior) |
| Data processor | Routinely processes data, provides services to the data controller (GDPR) |
| Data custodian | Appointed preson that has legal or regulatory responsiblity |
| Data users | Use data |
| Data subject | Is the person whose personal information is collected |

### Data Life cycle
| Name | Description |
| :----- | :----- |
| Collection | inputting data, filling out online web form, only colelct data they need |
| Location | Physical location where the data is collected, stored and processed |
| Data sovereignty | Government has some degree of regulatory oversight |
| Maintenance | Validation for proper use, relevancy, accuracy, Archiving, Transferring, disposing, Documented and only performed by authorized personnel |
| Retention | Backup = Restore in the event of an incident (needed data). Archiving = Required for retention (unneeded data). |
| Remanence | Best way to solve is destruction of the media |

Types of destructions:
* Noncritical - Degauss, smash sh cards and optical discs
* Very sensitive - Destruction must me witnessed and documented
  * Burning or melting
  * Shredding
  * Physical destruction by smashing with hammers, crowbars
  * Degaussing magnetic media

### Asset Life Cycle
* Requirements - Establish requirements due to function and performance
* Design and architecture - Establish design and overall fit into the architecture
* Development or acquisition
* Testing - Suitability for ist intended purpose
* Implementation - Put it into service
* Maintenance/sustainment - Repair, patching, upgrades
* Disposal/Retirement/replacement - Replace and/or dispose it
  * End of life (EOL) - No longer viable of functional as required.
  * End of support (EOS) - No longer services it.

### Data Protection Methods
* Digital Rights Management (DRM)
  * Restrict access to data, used to protect copyrighted material an trade secrets
  * Implemented in software. There are some hardware-enabled solutions
  * Protections like watermarking, file or software encryption, licensing limitations.
  * Using steganography to insert digital watermarking
* Data Loss Prevention (DLP)
  * Is normally applied to the most critical and sensitive data
  * Works by assigning labels or metadata to files which indicates the sensitivity
  * Two types: Network DLP (NDLP) and endpoint DLP (EDLP)
* Cloud Access Security Broker (CASB)
  * Mediates connections to and from the cloud storage and infrastructure
  * Two methods: Proxying and API's
