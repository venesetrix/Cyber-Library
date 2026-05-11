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
| Azure AI Language | Text analysis, sentiment, NER |
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

Six principles AI framework
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

![Azure AI Reference Architecture](./Resources/Images/AI102-Reference-Arch.png)

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

### Features

| Feature | Purpose |
| :-- | :-- |
| Prompt Shields | Scans text for the risk of a User input attack on a LLM. |
| Groundedness detection | Detects whether the text responses of LLM's are grounded in the source materials provided by the user. |
| Protected material text detection | Scans AI-generated text for known text content |
| Task adherence API | Detects when tool use by AI agents is misaligned or unintented |
| Analyze text API | Scans text for sexual content, violence, hate and self harm |
| Analyze image API | Scans images for sexual content, violence hate and self harm |
| Custom detection | Create and train own custom content categories |

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

[Python Script Example](./Resources/Scripts/AI102-ContentAPI.py)

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

Categories in Image moderation might be:
* Optical character recognition (OCR) = Find text in images
* Spatial analysis = Find stuff in a 3D environment (aka Video)
* Face = Face recognition
* Photo ID matching = Match a photo ID to a person's face

## Analyze Images with Pre-Built Models

Azure AI Vision = pre-trained models, no ML expertise needed

* Ideal for object detection, scene understanding and image tagging
* Part of Azure Cognitive Services

[Python Script Example](./Resources/Scripts/AI102-VisionAPI.py)

## Create Custom Computer Vision Models

Use Custom Vision API Models when prebuilt models fail your domain. Choose the base domain that is closest to your use case (i.e. "Food", when you need to built a custom "tomato"-Model). 

The flow is:
1. Create project (classification or detection)
    * Classification = Image classification tags whole images
    * Detection = Detection finds the location of content within an image
2. Add tags and images (>=50/tag recommended)
3. Workflow
    1. Train - Via API or the [Custom Vision Training Site](https://www.customvision.ai/)
    2. Evaluate - Test with Test-Images
    3. Publish - Access via API or Download the model in different formats

Metrics to deal with are:

* **Precision**
    * Base question: How many of the cases predicted to be positive were actually positive? 
    * Focus: Avoiding false positives.
* **Recall**
    * Base question: How many of the actual positive cases did the model find? 
    * Focus: Finding all positive cases (avoiding false negatives).
* **F1**
    * Base task: The F1 score is the harmonic mean of precision and recall. It combines both metrics into a single value to provide a balanced overall picture of model performance. 
    * Focus: When both false positives and false negatives are to be avoided.

### Endpoints for Models

* CoreML (iOS) - Run Model on iPHones and iPads
* TensorFlow (Android) - On Android apps or edge devivces with TensorFlow Lite
* ONNX - Integrate into Windows ML, ML.NET or cross-plattform apps using open standards
* Dockerfile - Package for Azure IoT Edge, Functions or custom containers in Azure MLVision
* AI Dev Kit (VAIDK) - Deploy models to physical camera devices.

![CustomVision Workflow](./Resources/Images/AI102-CustomVision-Workflow.png)

[Python Script Example](./Resources/Scripts/AI102-CustomVisionAPI.py)

## Analyze Video Content

### Azure AI Video Indexer

Is a prebuilt pipepline combining Vision, Speech and Language AI accessible via Portal, REST API and SDK. It extracts:

* Spoken words (speech-to-text)
* Faces and emotions
* Brands, topics and scenes
* OCR text from frames
* Translations and keywords

## Process Text with Azure AI Language

Use Azure AI Language to extract structured insight from raw text. Supports over 90 languaged and is accessible via [Azure AI Language Studio](https://language.cognitive.azure.com/), REST API and SDK. Is a consolidated Azure AI service that replaced and absorbed Azure Text Analytics and Azure Language Understanding (LUIS).

It extracts:
* Positive, neutral and negative tones
* Key themes with Key Phrase Extraction
* Confidence scores
* Auto-language detection

Other important knowledge about AI Language:
* Utterances are example user inputs used to train an intent recognition model. Entities refer to specific pieces of information extracted from utterances, such as dates, locations or product names.
* Setting **include_opinion_mining=True** enables sentence-level sentiment analysis, allowing the API to return sentiment scores for each sentence instead of just the overall document.
* Knowledge bases of Azure AI language are exported as JSON files where question-answer pairs are stored in the qnaPairs array.

Use in feedback analysis, support prioritization and brand monitoring:
* Named Entity Recognition (NER) identifies/labels/classifies pleople, places, orgs
* PII detection on the other hand redacts sensitive data like Social Security Numbers, emails, phone numbers (using the parameter categories_filter=["CreditCard, "Email"])

[Python Script Example](./Resources/Scripts/AI102-LanguageAPI.py)

[Python Script Example with asyncronous Requests](./Resources/Scripts/AI102-LanguageAPIpro.py)

[Python Script Example with long running Objects](./Resources/Scripts/AI102-LanguageAPI-LRO.py)

## Build Conversational AI with Bots

The Azure Bot Service is a managed Azure service to register, deploy and manage bots. It supports the Bot Framework SDK or Copilot Studio.

[Bot Service Documentation](https://learn.microsoft.com/en-us/azure/bot-service/bot-service-overview?view=azure-bot-service-4.0)

Definitions:
* **Bots** are nothing more or less than conversational user interfaces.
* **Channels** (the "Client side") include Microsoft Teams, Web Chat, Slack, WhatsApp and custom web clients.
* **AI Agents** are autonomous workflows powered by tools like AutoGen, Semantic Kernel, Lang Chain etc. They let us build AI that reasons, plans and acts.
* **RAG** Retrieval augmented generation. Let the model "read up" before answering.

Can optionally use integrations like:
* Azure AI Language (intent/QA)
    * Answer user questions
    * Detect intents (CLUs - Conversational Language Understanding) 
* Azure Cognitive Searchs (RAG Grounding)
* Azure OpenAI (for generative replies)

Microsofts perferred modern bot pattern is:
* AI Language or OpenAI for Natural Language Processing (NLP)
* Cognitive Search for Grounding
* Azure Communication Services (ACS) + Direct Line for Multichannel reach

To create dynamic question answering bots that supports follow-up questions related to previous queries each question-answer pair needs a contextId assigned, referencing a parent question. To provide users with variations of answers the developer should define alternate phrasing for a single question like:

```python
kb.add_qna(
    question="What is your refund policy?",
    answer="Refunds are processed within 7 days.",
    alternateQuestions=[
        "How do refunds work?",
        "Can I return an item?"
    ]
)

```

[Python Script Example](./Resources/Scripts/AI102_QuestionAnswering.py)

## Implement Speech-to-Text Solutions

Can be accessed via SDK for live transcription in apps, by REST PI for batch jobs on stored files or [Microsoft Foundry > Playgrounds > Speech-Playground](https://ai.azure.com/). The incoming formats are WAV, MP3, OGG or mic/network audio. Is designed for streaming audio and live transcription in real time and you only need text and no video insights.

The flow is:
1. Input: An audio stream or file is sent to Azure endpoint
2. Decode: An acoustic model decodes sound into phonemes
3. Assembling: A language Model assembles phonemes into text
4. Appling Enhancements: Profanity mask, custom phrases, speaker ID
5. Output: JSON with text and confidence scores

Transkription models can be optimized for accuracy with:
* Custom Speech - Train on labeled audio + text
* Phrase hints - Accuracy for key terms
* Features - Language ID, multi-channel, diarization
* Metrics - Track WER and view logs in Azure Monitor
* Compliance - PII masking
* Containers - Support offline or air-gapped use

Deployment patterns:
| Deployment | Usage |
| :----- | :----- |
| Client SDK | Capture MIC input on desktop, mobile, IoT |
| REST API | Save Audio to blob / Batch |
| Hybrid | Local preprocessing > Cloud analytics |
| Edge | Run containers in secure or offline sites |
| Security | Key Vault, Private Link, RBAC |
| Monitoring | Azure Monitor alerts and logs |

[Python Script Example](./Resources/Scripts/AI102_SpeechToText.py)

## Deploy Text-to-Speech Solutions

Azure AI Speech supports more than 400 Voices in 140+ languages. Can be used for reading dynamic content in the user's preferred language. Is accessible via [Microsoft Foundry > Playgrounds > Speech-Playground](https://ai.azure.com/), REST API or SDK. Include styles like 'cheerful', 'assistant' and 'newscast'.

In Use-Cases the text has to be translated first and then synthesized. Otherwise the pronounciation may be wrong. The flow is:

1. User Inputs text
2. Azure Translator translates into target language
3. Azure Speech SDK applies SSML (Speech Synthesis Markup Language) Customization
4. TTS Engine generates Speech Audio
5. Output the Audio

### SSML
SSML is markup for pitch, rate, pauses, volume and emphasis. By this we can swap voices and emotions [see Speech Studio Voice Gallery](https://speech.microsoft.com/portal/voicegallery). It works in REST and SDK.

Important tags are:
* \<voice> - Switch speakers
* \<break time="500ms"> - pause naturally
* \<prosody rate="slow" pitch="+10%"> - control delivery
* \<phoneme ph="t€k 'tr€ina"> - fix pronunciation
* \<lang xml:lang="fr-FR"> - mix languages

SSML Example:
```xml
<speak version='1.0' xml:lang='en-US'>
    <voice name='en-US-JennyNeural'>
        <mstts:express-as style='cheerful'>
            <prosody rate='slow' pitch='+10%'>Welcome to Paris!</prosody>
            <break time='500ms'/>
            <emphasis level='moderate'>Your stay in our Hotel is confirmed.</emphasis>
        </mstts:express-as>
    </voice>
</speak>
```
### TTS Best-Practices
* Use Azure Key Vault for API Keys
* Pre-generate frequent phrases
* Don't feed raw translations to TTS
* Test audio for pacing and tone

[Python Script Example](./Resources/Scripts/AI102_TextToSpeech.py)

## Translate and Localize Content

The Azure Translation Service is capable of Real-time text translation, broad language support, custom translation and document translation with access via [Language Studio](https://language.cognitive.azure.com/translation), SDK, REST API and container support.

It's possible to use Azure Functions, Azure Logic Apps or Power Automate to automate translation workflows.

[Python Script Example](./Resources/Scripts/AI102_Translator.py)

## Deploy Knowledge Mining Solutions
 
Knowledge mining = Extracting structured info from unstrctured content (PDFs, images, ...). It combines AI Search, Document Intelligence and AI Language.

### Azure AI Search

The main components are Indexes, Indexers, Skills and Data Sources. To built an usable Azure AI Search Service follow this procedure:
1. Connect to Data - Select data sources like Databases, Storage Services or Data Lakes
2. Add cognitive skills - For example document intelligence
3. Customize target index - Create an index with key extracted fields from the source data. It's the actual search database for your data. It's like a book index and tells you where to find data.
4. Create an indexer - Extract load agent. It pulls data from the source, extracts data and pulls it into the index.

### Built-in cognitive skills

Skillsets run during indexing, not querying. Skills enrich data before it reaches the index. SplitSkill + Embeddings ≈ modern RAG pattern.

| Skill | Description |
| :----- | :----- |
| ContentReaderSkill | Reads text content from files or blobs |
| OcrSkill | Extracts text from images or scanned PDFs |
| MergeSkill | Combines multiple text inputs into one output |
| SplitSkill | Splits long text into pages or chunks |
| LanguageDetectionSkill | Detects the language of text |
| KeyPhraseExtractionSkill | Extracts important phrases from text |
| EntityRecognitionSkill | Identifies entities such as people, organizations, locations and dates |
| PII Detection Skill | Detects personal data like names, emails, phone numbers |
| SentimentAnalysisSkill | Determines sentiment (positive, neutral, negative) |
| TextTranslationSkill | Translates text into a target language |
| Custom Web API Skill | Calls your own REST API |
| ShaperSkill | Reshapes or restructures data in the enrichment tree |
| Azure OpenAI Embedding Skill | Generates vector embeddings |
| Custom Document Skill | Can use Azure AI Document Intelligence endpoint |

To add a skill the code would look like:
```json
{
    "name":"ExtractText",
    "skill":"contentReaderSkill",
    "inputs": [
        {
            "name" : "document",
            "source" : "/document/content"
        }
    ]
}
```

### Vector based search

Azure AI Search (formerly Azure Cognitive Search) is working with vectors:
* Contents are transformed into vectors ('embeddings').
* All vectors are safed in a vector-DB.
* The search-term is also transfered into a vector.
* The database is finding the closest vectors - these are the most relevant contents.

### Creating and managing indexes

* An index defines the structure of searchable content, including fields and data types.
* Use the Azure portal or REST API to create and manage indexes.

parsingMode options are:
* default
    * For unstructured documents like PDF, DOCX, PPTX, HTML, TXT.
    * Produces one search document per file
    * Required for OCR
* json
    * For JSON objects.
    * Produces one search document per object.
    * When you need structured field mappings.
* jsonArray
    * For JSON Arrays.
    * Each object in the array produces a separate document.
* delimitedText
    * Supports CSV and other delimited formats.
    * Each row becomes a search document.
* markdown
    * For markdown-documents.
    * Submodes:
        * oneToMany: Each content section becomes a search document
        * oneToOne: One search document for the whole markdown file

[Python Script Example](./Resources/Scripts/AI102_SearchAPI.py)

## Extract Data from Documents

Azure AI Document Intelligence (formerly Form Recognizer) automates the extraction of information from documents using machine learning. It supports prebuilt models (i.e. invoices, receipts, ID cards, credit cards, contracts, business cards) for common document types and custom models for specific layouts. Specialization on forms. It is accessible via SDK, REST API and the [Document Intelligence Studio](https://contentunderstanding.ai.azure.com/documentintelligence/studio). It supports PDFs, images and scanned forms.

Requirements:
* Supported File-Formats: PDF, JPEG/JPG, PNG, BMP, TIFF
* Less that 500 MB (S0 tier) and 4 MB (F0 tier)
* Image dimensions: Between 50x50 and 10.000x10.000 pixels.
* <500 pages training data


[Python Script Example](./Resources/Scripts/AI102_DocumentIntelligenceAPI.py)

## Leverage Azure OpenAI Services

GPT models enable generative tasks like summarizing, rewriting and explaining content. Azure OpenAI exposes models via chat/completions API. Prompts are structured as role-based messages: system, user, assistant.

* **OpenAI** is an AI research lab who created the Generative Pretrained Transformer (GPT) and other of its variants like DALL.E (Images), Whisper, Sora, Operator, etc.
* **ChatGPT** is OpenAI's consumer SaaS app powered by GPT models. It's hosted at chat.openai.com and includes tools like code interpreter and web browsing.
* **Microsoft Copilot** embeds GPT models into M365, GitHub and more.
* **Azure OpenAI Service** offers private access to OpenAI's models via REST APIs and SDKs in the Azure ecosystem
* **Azure AI Foundry** offers GPT-4, GPT-4 Turbo (Text & Code), Embeddings and DALL.E 3 models with security, governance and quota controls.

Models are deployed via [Azure Foundy Portal](https://oai.azure.com/resource/deployments) (either OpenAI Service or Foundry Service) or CLI.

**Assistant (Azure OpenAI)**
* = "Workflow"
* Defined behavior + tools
* Built-in Azure AI Studio
* Chat based & goal-driven
* Powered by deployed GPT

**Agent (Azure AI Agent Service)**
* = "Chat"
* Executes tasks autonomously
* Orchestrated by Agent Service
* May act without user prompting (autonomy)
* Support tools, reflections, memory, triggers
* The agent in "agentic AI"

[Python Script Example](./Resources/Scripts/AI102_OpenAI.py)

## Optimize Generative AI Models

### Model adjustments

* Temperature (Limits probability distribution): 
    * Temperature scales the probabilities of all tokens before one is selected.
        * Low temperature → Differences are amplified
        * High temperature → Differences are smoothed out 
    * Setting temperature to a low value like 0.3 reduces randomness, making output more structured and consistent.
    * Low Value (0.2) means, that the result is the most probable.
    * High Value (1.0) means, that the probability is used like trained.
    * Very High Value (1.5) means, that every possible choice is used frequently.
* Top_p (Nucleus Sampling - Limits probability mass)): 
    * Allows as many tokens as necessary until a cumulative probability is reached.
    * Affects probability of the next choice. 
    * Low Value (0.1-0.3) is very conservative and predictive. 
    * Medium Value (0.8-0.95) is the middle between creativity and quality.
    * Highest value (1.0) means every possible output token.
* Top_k (Limits Number of tokens):
    * Limits the choice on the k-number of most probable tokens without taking their individual probability into account.
* Frequency_penalty (Reduces the likelihood of repeated words or phrases)
    * A negative frequency-Penalty encourages repetition
* Presence_penalty (Promoting response variety)
    * Increasing presence_penalty encourages the model to introduce new tokens instead of reusing common ones.

| Scenario | Temperature | Top_p | Top_k |
| :----: | :----: | :----: | :----: |
| Q&A/Chatbot | 0.3-0.5 | 0.8-0.9 | N/A |
| Creative Content | 0.8-1.0 | 0.95 | 40 |
| Compliance/Deterministic | 0.0 | 1.0  OR top_k | 1 OR top_p |


### Prompt engineering

* No training, just smart input crafting
* Giving the model system messages, few-shot examples and delimiters
* Use when cost/time must stay low

### Fine tuning

* Upload labeled data to teach a model custom patterns
    * Preparing the dataset requires training data in JSONL (JSON lines) format
    * Each entry has to consist of a prompt and a completion field.
* Great for structured outputs
* Costs a lot to train the model
* Integrates data directly into the model instead of "RAG" or read it up in front of each request

### Retrieval-augmented Generation (RAG)

* Create a vector store + data retrieval pipeline
* Embed custom content into the store
* Model retrieves chunks as context for queries
* No training required; easier to update content

### Use Semantic Kernel and Autogen in agent workflows

Both are free solutions from Microsoft for agentic AI.

Langchain is a tool for connecting different LLM's together. [Semantic Kernel](https://github.com/microsoft/semantic-kernel) is the Microsoft tool for that.
[Autogen](https://github.com/microsoft/autogen) on the other side is the competitor to Anthropics MCP.

[Python Script Example](./Resources/Scripts/AI102_Autogen.py)
* Create a vector store + data retrieval pipeline
* Embed custom content into the store
* Model retrieves chunks as context for queries
* No training required; easier to update content

## Implement Responsible AI Practices

The six responsible AI practices framework:

| Principle | Description |
|:----|:----|
| Fairness | Ensure models treat all people and groups equitably by detecting, measuring, and mitigating bias and data in predictions. This often involve personally identifiable information and other secrets. |
| Reliability & Safety | Validate performance under real world conditions, run continuous tests, and build safeguards to prevent harmful failures. |
| Privacy & Security | Protect personal data by design, enforce strong encryption, manage access controls, and comply with regulatory requirements. |
| Inclusiveness | Design for diverse user needs, support accessibility features, and avoid excluding any community or ability level. |
| Transparency | Document model designs, share decision making logic, and communicate limitations so stakeholders can understand how our AI works. |
| Accountability | We assign clear ownership, establish governance processes, and maintain audit trails to monitor, review, and remediate through the AI lifecycle. |

### Build transparent AI systems

* Identify and mitigate model bias (training data, prompts, access patterns)
    * Interpretability tools help organizations understand how AI models make decisions, ensuring transparency and fairness.
    * Adversarial debiasing can help reduce bias, but have to be used in conjunction with other measures.
* Document model behavior with transparency notes
* Add explanation layers to model outputs
* Log and trance prompts and completions using Azure AI telemetry

### Tool to detect and explain model bias

* Azure Ai Content Safety: Detect harmful outputs
* Prompt Flow evaluation nodes: Assess prompt relevance and fairness
* Responsible AI dashboards (SDK v2): Visualize disparity across groups
* Fairlearn library: Generate fairness metrics and parity charts.

### Bake in privacy, safety and compliance

* PII detection and content filters
* Secure endpoints with Entra ID, RBAC and managed identities
* Store secrets in Azure Key Vault
* Enable audit trails with Azure Monitor and Log Analytics
* Follow region-specific compliance rules (GDPR, HIPAA, ...)
* Prompt shielding to prevent risky completions in Azure OpenAI

### Groundedness detection

Groundedness describes, how much of the LLM's answer is "grounded" or based on what it learned before. Depending on the Model and its Generation it saves communications like a log file. But with the time the limit exceeds older data is removed. Groundedness detection figures out if the LLM's responses are still based on the "Source of Truth". Or to say it simple: It tries to prevent or at least detect hallucination.

## Monitor and Optimize Azure AI Solutions

### Instrument services with diagnostics

#### Diagnostic services

* Azure Monitor is for platform telemetry
* Application Insights for performance and usage
* By enabling diagnostic settings on the resources we can set up alert rules for error spikes, latency, etc.

#### Logging

* Stream diagnostic logs to Log Analytics
* Query with Kusto (KQL) for insights
* Use log-based alerts for precision
* Integrate logs with Azure Dashboard or Sentinel

#### Using KQL

* Use Kusto Query Language (KQL) in Log Analytics
* Filter logs from Azure AI resources by time, result or caller
* Project relevant fields: time, response, user agent, error code
* Built charts in Azure Monitor workbooks or set alert rules

KQL-Example:
```SQL
Azure Diagnostics
| where ResourceProvider == "MICROSOFT.COGNITIVESERVICES"
| where OperationName == "PromtCompletion"
| extent prompt = tostring(parse_json(RequestPayload).prompt)
| extent completion = tostring(parse_json(ResponsePayload).completion)
| project TimeGenerated, prompt, completion, userSentiment
| order by TimeGenerated desc
| take 5
```

### Govern cost with workbooks and alerts

* Use built-in or custom Azure Monitor workbooks
* Visualize usage by model, resource group, SKU
* Correlate token usage with billing

```console
az consumption budget create \
--resource-group ai-102
--amount 100 \
--name aiUsageCap \
--time-grain monthly \
--notifications \
    emailHook={
        "enabled": true,
        "operator": "GreaterThan",
        "threshold": 80,
        "contactEmails" : ["ai102Operations@example.com]
    }
```

### Auto-scale & update container deployments

* Use Azure Container Apps or AKA
* Define CPU/memory/queue-based rules
* Support rolling upgrades or blue/green
* Monitor health probes and logs

### Modernize Model deployments

* Version with labels or tags
* Roll forward with canary (small amount of users on new version and then enlarge) or blue/green (live vs update environment and switch traffic dynamically)
* Route traffic incrementally
* Rollback on failure detection

### Trace, collect feedback and reflect models

* Enable tracing in Azure AI Foundry.
* Use feedback signals (thumbs up/donw, starred completions)
* Log feedback in Cosmos DB or App Insights.
* Evaluate using Prompt Flow or manual review.

## Useful links

### Preparation Roadmaps
[AI-102 Exam Preparation](https://github.com/Arturo-Quiroga-MSFT/AI-102-Exam-Prep)

### Practice tests

[Free Full-Length Practice Exam](https://certificationpractice.com/practice-exams/microsoft-azure-ai-engineer-associate)

[AI-102 Free Practice Tests](https://www.testpreplab.com/AI-102-free-practice-test/)

[Examsland](https://examsland.com/free-practice-test/ai-102)

[OpenExamPrep](https://open-exam-prep.com/practice/azure-ai-102)

[Examtopics](https://www.examtopics.com/exams/microsoft/ai-102/view/)

[Free AI-102 Mock Exam](https://www.freemockexams.com/AI-102-practice-test.html)

[Code with Bibek Youtube Playlist](https://youtu.be/Xt1zt0FLHrY?si=V7ElKniEVLHV8Bbp)

## Exam Tips

* Focus on matching between specific Azure AI services to business requirements (compare [Azure AI Architecture Framework](https://learn.microsoft.com/en-us/azure/architecture/browse/?terms=Azure%20ai))
* Expect scenario-based questions where choosing the correct service involves considering Scalability, Security, Compliance, Cost and Performance trade-offs.
* In Sandbox Environments read through all the tabs. Each question will usually have the answer in one of the bullet lists in the tabs. Watch out for Buzzwords.
* Whenever you can decide between API key and RBAC, use RBAC as it is the best practice approach.
* What can you do, when you not have enough performance? Adjust the scale of the service.

## Services at a glance

### AI Bot Service

* The Bot Framework includes a modular and extensible SDK for building bots and connecting to AI services. 
* The SDK supports Memory and storage, Natural language understanding and adding media and cards.
* You can connect the bots to [channels](https://learn.microsoft.com/en-us/azure/bot-service/bot-service-manage-channels?view=azure-bot-service-4.0), such as Facebook, Messenger, Slack, Microsoft Teams, Telegram, and SMS via Twilio.

### Azure Content Safety

[Azure Content Safety Studio](https://contentsafety.cognitive.azure.com/)

#### Features
* Provides API's for different moderation needs:
    * AI safety and prompt protection
        * Prompt Shields (max 10K chars)
        * Groundedness detection (max 55K chars for grounding source, 7,5K for query length)
        * Protected material text detection (max 10K chars)
        * Task adherence API (max 100K chars)
    * Content analysis
        * Analyze text (max 10K chars)
        * Analyze image (max 4MB, between 50x50-7200x7200 pixels, can be JPG, PNG, GIF, BMP, TIFF or WEBP)

#### Szenarios
* User prompts submitted to a generative AI service.
* Content produced by generative AI models.
* Online marketplaces that moderate product catalogs and other user-generated content.
* Gaming companies that moderate user-generated game artifacts and chat rooms.
* Social messaging platforms that moderate images and text added by their users.
* Enterprise media companies that implement centralized moderation for their content.
* K-12 education solution providers filtering out content that's inappropriate for students and educators.

### Custom Vision

[Custom Vision web portal](https://customvision.ai/)

#### Features

* Azure AI Custom Vision is an image recognition service that lets you build, deploy, and improve your own image identifier models. 
* Projects (F0=2, S0=100)
* Training Images Limits (F0=5K, S0=100K)
* Predictions (F0=10K, S0=Unlimited)
* Iterations (F0=50, S0=500)
* Accepted Image Types (JPG, PNG, BMP, GIF)
* Project types:
    * Classifier = Is it a Dog or a Cat?
        * Classification Types
            * Multilabel = Multiple tags per image
            * Multiclass = Singeg tag per image
        * Domains are General, Food, Landmarks, Retail, Compact (can run on mobile devices)
        * Classifier evaluation:
            * Precision = For example, if the model identified 100 images as dogs, and 99 of them were actually of dogs, then the precision would be 99%.
            * Recall = For example, if there were actually 100 images of apples, and the model identified 80 as apples, the recall would be 80%.
            * Probability threshold = When you interpret prediction calls with a high probability threshold, they tend to return results with high precision at the expense of recall—the detected classifications are correct, but many remain undetected. 
    * Object Detection = Is there a Dog?
        * Domains are Genral, Logo, Products on shelves and Compact domains
        * In order to train your model effectively, use images with visual variety.
        * Detection evaluation:
            * Has Precision and Recall, too.
            * Mean average precision = Is the average value of the average precision (AP). The AP is the area under the precision/recall curve (precision plotted against recall for each prediction made).
            * Overlap Threshold = How correct an object prediction must be to be considered correct in training.

### Azure Face

[Documentation](https://learn.microsoft.com/en-us/azure/ai-services/face/overview-identity)

[Vision Studio for Face](https://portal.vision.cognitive.azure.com/gallery/face)

The Azure Face service provides AI algorithms that detect, recognize, and analyze human faces in images.

#### Features

* Identification (find a face of a known person in an image)
* Verification ("Do these two faces belong to the same person?")
* Find similar faces ("face matching between a target face and a set of candidate faces") with matchPerson and matchFace modes.
* Group Faces (divides a set of unknown faces into several smaller groups based on similarity)
* Formats are JPEG, PNG, GIF and BMP with a size between 36 x 36 to 4096 x 4,096

#### Szenarios

* Verify user identity
* Liveness detection (anti-spoofing like printed photo, recorded video or a 3D mask)
* Touchless access control
* Face redaction (blur detected faces)

### Azure AI Search

Azure AI Search is a fully managed, cloud-hosted service that connects data to AI. The service unifies access to enterprise and web content so agents and LLMs can use context, chat history, and multi-source signals to produce reliable, grounded answers.

#### Features

* Two engines: classic search for single requests and agentic retrievel for parallel LLM-assisted search (RAG).
* Full-text, vector, hybrid, and multimodal queries over local (indexed) and remote content.
* Enrich and structure content at indexing or query time with skills that perform chunking, embedding, and LLM-assisted transformations.
* Indexing:
    * Azure AI Search can only index JSON documents.
    * During indexing, you can use AI enrichment to chunk text, generate vectors, and apply other transformations that create structure and content.
* Agentic retrieval:
    * Each query targets a knowledge base that represents a complete domain of knowledge.
    * A knowledge base consists of one or more knowledge sources, an optional LLM for query planning and answer synthesis, and parameters that govern retrieval behavior.
* If your content is in a supported data source, use the pull method to retrieve and serialize data into JSON. If you don't have a supported data source, or if your content and index must be synchronized in real time, the push method is your only option.

#### Classic Search

* Full-text search
    * Import JSON-formatted data
    * Configure field-definitions
        * Retrievable
            * = Field can be returned in a search result. 
            * If false it can be used for filtering, sorting or scoring. 
            * Must be true for key fields and null for complex fields.
            * Doesn't cause any increase in index storage requirements.
        * Searchable
            * = Is full-text searchable and can be referenced in search queries.
        * Filterable
            * = Enable the field in filter-queries. 
            * Don't undergo lexical analysis so only exact matches will work.
        * Sortable
            * = Enable the field in orderby expressions.
            * Only sortable if it's single-valued
        * Facetable
            * = Referenced in facet queries (hit count by category).
* Vector search
    * Vectors are high-dimensional embeddings that represent text, images, and other content mathematically.
    * At query time, the vector fields in your index enable similarity search, where the system retrieves documents whose vectors are most similar to the vector query.
    * More storage is required for filterable fields.
* AI enrichment
    * Refers to integration with Foundry Tools to process content that isn't searchable in its raw form.
    * BuiltIn-Skills:
        * Multimodal Image and text vectorization
        * Entity "Custom Lookup", "Recognition", "Linking"
        * Image analysis
        * Key Phrase Extraction
        * Language Detection
        * OCR
        * PII Detection
        * Sentiment
        * Text translation

#### Agentic retrieval (RAG)

* A knowledge SOURCE specifies the content used for agentic retrieval.
* A knowledge BASE is a top-level object that orchestrates agentic retrieval.

[Documentation](https://learn.microsoft.com/en-us/azure/search/)


### Azure AI Video Indexer

[Documentation](https://learn.microsoft.com/en-us/azure/azure-video-indexer/)


### Azure AI Language

[Documentation](https://learn.microsoft.com/en-us/azure/ai-services/language-service/)


### Azure AI Document Intelligence

[Documentation](https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/?view=doc-intel-4.0.0)


### Azure Vision in Foundry Tools

[Documentation](https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/)


### Azure Translator in Foundry Tools

[Documentation](https://learn.microsoft.com/en-us/azure/ai-services/translator/)


### Azure Speech

[Documentation](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/)


### Azure Foundry

[Documentation](https://learn.microsoft.com/en-us/azure/foundry/)