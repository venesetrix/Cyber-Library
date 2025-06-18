# CISSP Domain 6 - Security Assessment and Testing

Definitions
    • Test - Procedure, that records properties, characteristics and behaviours of the tested system
        ○ Veriy limited in scope and involves only the list of procedures to check for functionality
    • Assessment - Test, designed to determine if a system meets specified security standards
        ○ Technical testing, documentation reviews, interviews with key personnel
        ○ Consists of several checks and is of a much broader scope
    • Audits - Conducted to measure the effectiveness of security controls.
        ○ Detective control by looking at audit trails, log files
        ○ Or a tailored systematic assessment of a particular system  if it meet as particular standard
        ○ Focuses on a specific event or business process

Use of Internal, External and Third-Party Assessors
    • Internal Security Auditors
        ○ Tasked with reviewing logs and other data on a daily basis to detect policy violations
        ○ Or assigned to specific events
        ○ Advantages:
            § Cost effectiveness
            § Less difficulty in scheduling an internal audit
            § Familiarity with the organization
            § Reduces exposure of sensitive data to outsiders
        ○ Disadvantages:
            § Influences by organizational politics and conflicts of interest
            § Likely have other duties
            § Lack of independence
            § Not as experienced
            § Not be allowed by external agencies
    • External Security Auditors (second-party auditor)
        ○ Work for a business partner and comes periodically to meet contractual requirements
        ○ Advantages
            § Cost more than internal but is already budgeted via the contract
            § Not as easily influences
            § Defined schedule
        ○ Disadvantages:
            § Lack of familiarity with the organization
            § Lack of independence (allegiances to the business partner)
            § May be influenced by internal conflicts
            § May incur some of the same limitations as an internal team such as split time, lack of experience
    • Third-Party Auditors
        ○ Required for independence
        ○ May be employed by a regulatory agency
        ○ Advantages:
            § True independence
            § Access to advanced auditing tools and techniques
            § Established unbiased proof of compliance or noncompliance
        ○ Disadvantage
            § Most expensive option
            § Difficult to schedule
            § Lack of familiarity with the organization
        


Security Control Testing
    • Vulnerability Assessment
        ○ Identifying the vulnerabilities present in a system/processes/people
        ○ Involve the use of network scanning tools
        ○ We don't act on the vulnerabilities
    • Penetration Testing
        ○ Proves, that a vulnerability can be exploited and affect system changes.
        ○ Can be very intrusive and can result in failure or degradation of infrastructure components
        ○ Client has to sign an agreement, that they understand the potential risks.
        ○ Never carry out a penetration test unless you are properly authorized.
        ○ Management and test team should develop a set of "rules of engagement" that clearly defines test parameters and grants permissions to perform the test.
        ○ Types of testers:
            § White-hat (ethical) hackers - Security professionals
            § Black-hat (unethical) hackers - Malicious entities to infiltrate or disrupt
            § Gray-hat hackers - Selling their expertise for good or illegal activities
            § Red Team - Pentesting team
            § Blue Team -  Defenders of the infrastructure and detect and respond
            § White Cell - Independent entity facilitating communication and coordination between blue and red teams and management. Team managing the exercise
        ○ Types of tests:
            § Full-knowledge (white or crystal box) test - Full knowledge about infrastructure, segmentation, devices and vulnerabilities. Useful to focus on specific areas of interest
            § Zero-knowledge (blind or black box) test - No Knowledge at all. Useful in discovering from an attacker's point of view.
            § Partial-knowledge (gray box) - Limited useful knowledge
            § Double-blind test -  Zero-knowledge for both attacking as well as defending team. Used to assess defenders on their detection and response capabilities.
            § Targeted test - Focused on specific areas of interest.
    • Log reviews
        ○ On a daily basis to inspect types of transactions within the network such as user actions
        ○ On a frequent basis to determine anomalous or malicious behavior.
        ○ On a test to ensure that the test happened according to its designed parameters
        ○ Can be manually reviewed or by automated systems like a SIEM.
        ○ Are useful in reconstructing timelines
    • Synthetic transactions
        ○ A transaction is a collection of individual events to produce a desired behaviour
        ○ Synthetic transactions are automated events that are designed to simulate behaviors of real users/processes
        ○ They are controlled, predictable and repeatable
    • Code review and testing
        ○ Examining developed software code's functional, performance and security characteristics
        ○ Approval of an application's move into production
        ○ Designed to determine if code meets specific standards set by the organization
        ○ Security aspects of code testing involve:
            § Input validation
            § Secure data storage
            § Encryption and authentication mechanisms
            § Secure transmission
            § Reliance on unsecured or unknown resources (library files)
            § Interaction with system resources
            § Bounds checking
            § Error conditions
        ○ Fagan inspection
            § Planning
            § Overview
            § Preparation
            § Inspection
            § Rework
            § Follow-Up
    • Fuzz Testing
        ○ Mutation "dumb" fuzzing - Takes previous input values and mutates them
        ○ Generational "intelligent" fuzzing - Data models used to create new fuzzed input by understanding data types
    • Misuse Case Testing
        ○ Assess all the different possible scenarios where software may be misused or abused.
        ○ Shows how software code can be interacted with in an unauthorized, malicious or destructive way.
    • Test coverage analysis
        ○ Determine which parts will be covered by the assessment, how much you're going to test and to what depth
        ○ Is a percentage measurement (Number of Use cases tested / total number of use cases)
        ○ Decision is based on costs, personnel availability and system criticality.
        ○ For example 25% of its assets tested each week.
        ○ Coverage types:
            § Branch coverage - Has every IF been executed under all IF and ELSE conditions?
            § Conditional coverage - Has every logical test been executed under all sets of inputs?
            § Function coverage - Has every function been called and returned results?
            § Loop coverage - Has every loop in the code been executed?
            § Statement coverage - Every line of code been executed?
    • Interface testing
        ○ Interfaces can be GUI, API, database tables and security mechanisms
        ○ Interfaces represent critical junction points
        ○ Security issues might
            § Data movement from a more secure environment to a less secure one
            § Introduction of malware into a system
            § Unauthorized access by a user or process.
            § Affected integrity by data transformations.
    • Breach attack simulations
        ○ Automated penetration tests that an organization conducts on itself
        ○ Runs automated tests and synthetic transactions to show that the vulnerability was exploitable
        ○ Performed on a regular basis not a point-in-time like penetration tests
    • Compliance checks
        ○ Determine if a control or security process complies with governance requirements
        ○ Checked against sometime detailed requirements passed down through laws, regulations and standards

Collect security process data
    • Security process data - Any type of data generated, that is relevant to managing the security program
        ○ Technical - Come from technical tools to collect data from systems (logs, config files, audit trail)
        ○ Administrative - Analyzed or narrative data from administrative processes (i.e. metrics, risk reports)
    • Data Sources
        ○ Technical - agent-based software on devices, running a script or manually, collected by DIEM
        ○ Account Management data - Details on user accounts, rights, permissions, usage history
        ○ Backup verification data - Written log, transaction logs, event that causes data loss, restore process
        ○ Training and Awareness data - Training completed, when, what
        ○ Disaster recovery and business continuity data - Response times, recovery point objective, maximum allowable downtime, how well the organization actually meets these objectives
        ○ Key Performance and Risk Indicators
            § Key Performance indicators (KPIs) - Metric how well a process/system is doing
            § Key Risk indicator (KRIs) - Singular or aggregated risk for system, process
            § Key control indicator (KCIs) - How well a control is functioning an performing
            § Key goal indicator (KGIs) - Overall indicators that uses the other indicators how the goals are met
        ○ Management Review and Approval
            § Paper trail that results from management review and approval of assessments, reports and actions should be collected
            § Established, that the security program has management approval and involvement
            § Can establish due diligence and due care
    
Test results and reporting
    • Test results should provide:
        ○ Analysis that is thorough, clear and concise
        ○ Reduction or elimination of repetitive or unnecessary data
        ○ Prioritization of vulnerabilities or other issues like severity, risk, cost
        ○ Information that shows what is going on in the infrastructure and how it affects the organization's security posture and risk
        ○ Root causes of issues
        ○ Business impact to the organization
        ○ Mitigation alternatives or compensating controls
        ○ Changes to KPI, KGI, KRI and other defined metrics
    • Reporting best practices
        ○ Include historical analysis, root causes and negative/positive trends.
        ○ Nontechnical summary for senior management and nontechnical stakeholders
        ○ In technical terms for those who have the knowledge and experience
        ○ Include recommendation and mitigations

Vulnerability handling
    • Remediation
        ○ All vulnerabilities should be identified as soon as possible and mitigated in short order.
        ○ The organization should prioritize the vulnerabilities in following order:
            § Severity
            § Cost to mitigate
            § Level of actual risk to the organization
            § Scope of the vulnerability
        ○ Actions should be carefully considered by management and included in the formal change and configuration management processes. And formally documented in maintenance records and risk documentation
    • Exception handling
        ○ How vulnerabilities are handles when they cannot be immediately remediated
        ○ US Food and Drug Administration (FDA) regulations requires the organization to develop an exception handling process by employing compensating controls.
        ○ Process
            § Notifying decision-makers about the mitigation options (senior management)
            § Documenting the exception and the reasons
            § Determining compensating controls
            § Follow-up plan to look at the long-term viability of mitigating it on a more permanent basis
    • Ethical disclosure
        ○ Cybersecurity professionals ethical obligation to disclose the discovery of vulnerabilities to stakeholders
        ○ Targets are creators of the products, users and professional communities
        ○ Not disclose a newly discovered vulnerability to the general population without first disclose it to the above
            
Additional
    • SAS70 - outdated
    • ISAE 3402 - Audit of the ICS, Service organization control
    • Statements on Standards for Attestation Engagements (SSAE 18), Reporting on Controls at a Service Organization, is the American auditing standard for auditing the ICS of outsourcing service providers.
    • SOC Reports - Service organization control report
        ○ SOC-1 - financial reporting
        ○ SOC-2 - design and operational effectiveness
        ○ SOC-3 - Shared with community, web site seal
            § Type 1 - point in time
            § Type 2 - period in time
    • Types of security audits
        ○ Limited assurance - Agreed upon procedures
        ○ Negative assurance - Wir haben nichts schlimmes gefunden
        ○ Positive assurance - Wir können bestätigen, dass es gut ist.
