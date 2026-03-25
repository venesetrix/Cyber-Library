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

* ideal for object detection, scene understanding and image tagging
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

Use Azure AI Language to extract structured insight from raw text. Supports over 90 languaged and is accessible via [Azure AI Language Studio](https://language.cognitive.azure.com/), REST API and SDK.

It extracts:
* Positive, neutral and negative tones
* Key themes with Key Phrase Extraction
* Confidence scores
* Auto-language detection

Use in feedback analysis, support prioritization and brand monitoring:
* Named Entity Recognition (NER) identifies/labels/classifies pleople, places, orgs
* PII detection on the other hand redacts sensitive data like Social Security Numbers, emails, phone numbers 

[Python Script Example](./Resources/Scripts/AI102-LanguageAPI.py)
[Python Script Example with asyncronous Requests](./Resources/Scripts/AI102-LanguageAPIpro.py)
[Python Script Example with long running Objects](./Resources/Scripts/AI102-LanguageAPI-LRO.py)

## Build Conversational AI with Bots

The Azure Bot Service is a managed Azure service to register, deploy and manage bots. It supports the Bot Framework SDK or Copilot Studio.

Definitions:
* **Bots** are nothing more or less than conversational user interfaces.
* **Channels** (the "Client side") include Microsoft Teams, Web Chat, Slack, WhatsApp and custom web clients.
* **AI Agents** are autonomous workflows powered by tools like AutoGen, Semantic Kernel, Lang Chain etc. They let us build AI that reasons, plans and acts.

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

[Python Script Example](./Resources/Scripts/AI102_QuestionAnswering.py)

## Implement Speech-to-Text Solutions

Can be accessed via SDK for live transcription in apps, by REST PI for batch jobs on stored files or [Microsoft Foundry > Playgrounds > Speech-Playground](https://ai.azure.com/). The incoming formats are WAV, MP3, OGG or mic/network audio.

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
* Metrics - track WER and view logs in Azure Monitor
* Compliance - PII masking
* Containers - support offline or air-gapped use

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
* In Sandbox Environments read through all the tabs. Each question will usually have the answer in one of the bullet lists in the tabs. Watch out for Buzzwords.