# CISSP Domain 1 - Security and Risk Management

## Organisation
Mission (has)> Goals <(supported by) Business Strategy <(supported by) IS-Strategy

## Security Governance - Control Frameworks
| Name | Description |
| ----- | ----- |
| NIST SP 800-53 rev 5 | Security control framework - mandatory for US fed government |
| ISO 27002 | Security Control Framework |
| CIS Controls | 18 controls |
| ITIL | "IT Infrastructure Library" are IT Process Controls |
| Cobit 2019 | Set of practices (IT Controls) |

## Definitions
| Name | Description |
| ----- | ----- |
| Due Diligence | Carefully considered risk and implemented controls (proactive) |
| Due Care | Actions taken in response to a specific event (reactive) |
| Cyber Crime | A crime which targets computers, networks or related techs |
| Vertical Enactment | Laws for specific sectors |
| Horizontal Enactment | Laws independetly of the sectors (z.B. PII) |

## Laws
### Security Controls
| Abbr.  | Name | Description |
| ----- | ----- | ----- |
| FISMA | Federal Information Security Management Act - Government |
| HIPAA | Health Insurance Protability and Accountability Act - Security & privacy of PHI. § Privacy rule. § Security rule |
| HI-TECH | Health Information Technology for Economic and Clinical Health Act - HIPAA ++ penalties for noncompliance and requirements for breach notification |
| GLB | Gramm-Leach-Bliley Act (1999) - Protect financial data, data breach concerns |
| SOX | Sarbanes-Oxley Act - Establish strong internal cybersecurity controls |
| CALEA | Communication Assistance for Law Enforcement Act (1994) - Wiretaps are allowed under court order |
| EEA | Economic Espionage Act - Stealing trade secrets from a U.S. corporation |
| ECPA | Electronic Communications Privacy Act - Implements safeguards against electronic eavesdropping |
| LA | Lanham Act - trademark protection |

### Privacy
| Abbr.  | Name | Description |
| ----- | ----- | ----- |
| GDPR | General Data Protection Regulation (2018) - EU regulation |
| FERPA | Family Educationasl Rights and Privacy Act - Privacy of student education records |
| CCPA | California Consumer Privacy Act - US state law protecting PII and breach notification |
| CPIPED | Canada's Personal Information Protection and Electronic Documents Act |
| NZPA | New Zealand's Privacy Act (1993) |
| LGPD | Brazil's Lei Geral de Protecao de Dados |
| PDPA | Thailand's Personal Data Protection Act |
| PA | American Privacy Act (1974) |
| COPPA | Children's Online Privacy Protection Act - Protect privacy of children using the internt (Minimum Age for PII collection 13y) |

### Export
Bureau of Industry and Security sets regulations on export of encyption products.
| Abbr.  | Name | Description |
| ----- | ----- | ----- |
| EE | Economic Espionage Act | From 1996 |
| ITAR | Internation Traffic in Arms Regulations | Prohibits export of items designated as military and defense items. |
| EAR | Export Administration Regulation | Prohibits the export of commercial items that may have military applications. |
| WA | Wassenaar Arragement | Observed by 42 countries. Details export controls. Important for Cyber is Category 3 (Electronics), 4 (Computers), and 5 (Telecommunikations).

## Licensing/Intellectual Property (IP)

| Name | Description |
| ----- | ----- |
| Trade Secret | Proprietary to a company, provides legal protection, not registered |
| Copyright | Rights of the creator to control the public distribution. Applies to the expression of an idea, not the idea itself. Provides legal protection, registered, Protection: 70y after death of last author |
| Trademark | Word, name, symbol that represents a brand, registered |
| Patent | Legal registration of an invention, registered, Protection: 20y beginning with application |

## Investigation Types
| Name | Description |
| ----- | ----- |
| Administrative | Focuses on Members of an organization, by internal personnel |
| Civil | Two parties have a dispute, burden of proof, preponderance of the evidence |
| Criminal | Individual or organization has broken the law, conducted by law enforcement personnel, guilt or innocence beyond a reasonable doubt |
| Regulatory | Violated administrative law or regulation, conducted by a government agency/law enforcement |

## Internal Governance

| Name | Intention | Description |
| ----- | :-----: | ----- |
| Policy | THE WHY | Directive, dictate requirements, administrative control, don't go into detail, the WHY, brief and concise, specific scope and purpose, approved by senior management |
| Procedures | THE HOW | approved by senior management, detail processes like disposing of media |
| Standards | WHAT LEVEL | Details minimum requirements or a control framework. 
| Guidelines | SUPPLEMENTAL INFORMATION | Not mandatory, provide supplemental information on how to perform procedures |
| Baseline | STANDARDIZED CONFIGURATION | part of configuration management |

## Personal Security
| Process | Description |
| ----- | ----- |
| Candidate Screening and Hiring | Background checks, financial responsibility checks, education, criminal records, EXCLUDE: personal relationships, organization affiliations, political learnings, medical history |
| Employment Agreements and Policies | Review, understand, attest understanding. Acceptable use, Equipment care, social media, data classification, harassement, safety, security incident |
| Onboarding | Policy signing, provisioning of rights and equimpent, awareness training. |
| Transfers | Policy update signing, refresher trainings, permission review vs. Privilege creep. |
| Termination | Return of equipment, deactivation of accounts, return of data. In firing/violation situation immediately revoke access once the decision has been made. Escorted at all times. |
| Vendor controls | Ensure personnel requirements are included in all contractual agreements. |

## Risk Management

### Elements of risk

* Asset - anything of value (tangible (greifbar) or intangible)
* Vulnerabilities - a weakness or deficiency in security measures
* Threats - negative event that has the potential to exploit a vulnerability causing damage. 
* Likelihood - Probability that a negative event will occur
* Impact - Level or magnitude of damage

### Determining Risk

Risk = Likelihood x Impact

Identify Threats - Threat libraries, Threat modeling

Identify Vulnerabilities - Vulnerability Assessment

| Name | Description |
| ----- | ----- |
| Risk Assessment | Collecting assets, vulns and threats |
| Risk Appetite | How much risk is the organization willing to accept |
| Risk tolerance | Risk to accept for individual business ventures |
| Risk culture | How the organization as a whole feels about taking risk |

### NIST SP 800-30 

Risk Management Framework (Assessment):
1. Prepare for the assessment
2. Conduct the assessment
    1. Identify threat sources and events
    2. Identify vulnerabilities
    3. Determine the impact
    4. Determine risk
3. Communicate results
4. Maintain the assessment

### Risk Analysis

Calculate likelihood and impact for the risks with:
* Quantitative analysis - Concrete, measurable data. 25% exposure factor x 200€ asset >> 50€ loss
    * Single loss expectancy (SLE) - SLE = Asset value x exposure factor
    * Annualized loss expectancy (ALE) - ALE = SLE x Annualized Rate of occurrence (how many times per year)
    * Annual cost of safeguard (ACS)
* Qualitative analysis - Subjective data (opinion) or based on extrapolation

### Risk Response

| Name | Description |
| ----- | :----- |
| Mitigation (reduction) | Minimizing vulnerabilites or strengtheing security controls, reduce level of total risk |
| Transfer (sharing) | Insurance, Using Service provider |
| Avoidance | Avoid activities |
| Acceptance | accept remaining risk (residual risk) |


### Risk Frameworks

* NIST SP 800-30
* ISO 27005
* OCTAVE (Operationally Critical Threat, Asset and Vulnerability Evaluation)
* FAIR (Factor Analysis of Information Risk)

### Countermeasure selection

* Based on cost/benefit analysis
* Must outweigh the coft of implementing and maintaining the control
* Balanced with the cost or monetary value of the asset
* Consider repair, replacement costs as well as amount of revenue it generates

### Types of controls

| Name | Description |
| ----- | :----- |
| Administrative (managerial) | Imposed by management like policies |
| Technical (logical) | Hardware and software like firewalls |
| Physical (operational) | Physical environment like guards and gates |

### Control functions - describe what a control does

| Name | Description | Example |
| ----- | :------------- | :----- |
| Deterrent | Deters an indiviual | Cameras or Warning Banners |
| Preventive | Prevents an individual | Firewall rules, Locks, Guards |
| Detective | Detect a violation | Audit logs, IDS, Alarm Systems |
| Corrective | Temporary measure | Guards, Rerouting network traffic |
| Compensating | Longer-term measure | Additional security devices, Stronger encryption, Physical Barriers |
| Recovery | Bring a damaged asset back | Backups, Redundant spares |

### Test controls

* Interviews with key personnel
* Observing the control in operation
* Documentation reviews

* Technical testing
* Reporting - Risk register or Plan of Action and Milestones (POA&M) - risk owners and timeline
* Continuous Improvement - Risk maturity modeling
  1. No
  2. Ad hoc
  3. Unmanaged
  4. Repeatable
  5. Ahead of the game

## Threat Modeling

* Threat Indicators - Pieces of data that show that a threat has exploited a vuln
* Indicators of compromise - Threat indicators viewed collectively
* Characterized
  * Natural vs human-initiated
  * Potential vs actual
  * Threat source
  * Generalized vs specific
  * Known vs unknown
* Threat Actors / Agents / Sources
  * Adversarial - Malicious groups
  * Accidental - complacent users
  * Structural - software failure
  * Environmental - disasters and outages
* Frameworks
  * MITRE ATT&CK - Threat tactics and techniques
  * Diamond Model of Intrusion Analysis - Analytical model to view threat actors
  * Cyber Kill Chain - Identify various stages of threats during a cyberattack
  * OCTAVE - Operational risk, security controls and technologies
  * Trike - TM methodology focused on auditing
  * STRIDE
  * VAST - Visual, Agile, and Simple TM - Incorporated into SDLC and Agile
  * PASTA - Process for Attack Simulation and Threat Analysis - TM method focused on integrating technical requirements with business process objectives

## Apply Supply Chain Risk Management (SCRM)

* Hardware
  * Faulty components
  * Counterfeit or fake parts
  * Firmware-level malware
* Software
  * Faulty code
  * Counterfeit or pirated software
* Services
  * Services are below the level of performance and function
  * Malicious insiders
* Reduce risk
  * SLA includes clear security roles and resposibilities
  * Reviewing the security program
  * Conducting audits by myelf or a third-party assessor
  * Reviewing the service providers own security assessments
  * Conducting own tests and security reviews
  * Implementing NDA's
  * Understand the legal and ethical environment in which the service provider operates
  * Void the Authoriziation to operate (ATO) of a vendor with issues. Four types auth decisions: Auth to operate, Auth to use, Common control auth, Denial of auth
* Minimum security requirements (in contract or SLA)
  * Access control
  * Auditing and accountability
  * Configuration management
  * Secure software development
  * System security
  * Physical security
  * Personnel security

## Security Awareness

* Types
  * Awareness - WHAT - Basic information
  * Education - WHY - Insight and understanding, advanced knowlege or theory
  * Training - HOW - Intermediate knowlege, related skills
* Presentation Techniques
  * Social Engineering role-play exercises
  * Organizational phishing exercises
  * Training games
* The WHEN
  * Onboarding - Basic awareness overview
  * More advanced security responsibilities - In-depth training, more frequent
  * Managers/Seniors - Specific training targeting their unique roles
  * Building "security champions"
* Effectiveness
  * Content reviews and occasionally change
  * Just-in-time-Training = #Student receives the training as soon as they need it
  * Update if organization has any type of operating environment changes, new regulations, new systems or security features, turnover in personnel
  * Collect data on increase or decrease of security incidents and security compliance
  * Record who gets trained, how often and on what topics. Maintained in HR files

## Additional

* Security Goals: CIA + Authenticity und Non-Repudiation
* Supply Chain and Third Party Risk ist ein neues topic.
* NCA - Non Compete Agreement - Don't work at a competitor
* Risk Management - Safeguard = The measure itself
* Threat modeling methods are: STRIDE, PASTA, Trike ,SCAP, Attack Tree Analysis, MITRE-Attack, BSI-Grundschutz

## Risk Management

### Prozess of Risk analysis

1. Identify Assets
2. Identify vulnerabilites and Threats
3. Quantify the probability and business impact
4. Determine where to implement security controls

### Basic threat modelling process

1. Assessement Scope
2. Identify Threat Agents and possible attacks
3. Existing counter measures
4. Identify exploitable vulnerabilities

### Vulnerability Analysis

* Scanning systems
* Identify missing patches
* Identify misconfigured settings
* Identify orphaned user accounts
* Identify programming code mistakes

### Where measuring not possible, try qualitative risk analysis

* Scenario based
* Rank threats on a scale
* Techniques: Brainstorming, Intervidws, Checklists, Delphi technique

There is alway some risk left over. This is called residual risks.

Control categories:
* Preventive
* Detective
* Compensating
* Corrective

Due care = Acting responsibly ("doing the right thing.")
Due diligence (Sorgfältige Prüfung) = Act of gathering the necessary information to make good decisions

# Business continuity

* Business continuity planning (BCP) provides methods and procedures for minimizing the impact
* Disaster recovery planning (DRP) provides methods and procedures, when the continuity is broken

## BIA

1. List, document and prioritize key business processes
2. Process owners develop own mission and goal statements
3. Inventory and list key upstream processes
4. Understand relationships between processes
    
1. Identify priorities
2. Risk identification
3. Likelihood assessment
4. Impact assessment
5. Resource prioritization

| Abbreviation | Description |
| ----- | :----- |
| MTD | Maximum tolerable downtime |
| RPO | Recovery Point Objective |
| RTO | Recovery Time Objective |
| WRT | Work Recovery Time |


































