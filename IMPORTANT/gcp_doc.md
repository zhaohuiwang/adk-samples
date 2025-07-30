


## Google Cloud
[`pip install google-cloud-aiplatform`](https://pypi.org/project/google-cloud-aiplatform/) the Python client library for Google Cloud's Vertex AI, a unified machine learning (ML) platform designed for building, training, deploying, and managing ML models and AI applications. It integrates various Google Cloud AI services, including AutoML, custom model training, and deployment, with support for frameworks like TensorFlow, PyTorch, and scikit-learn. It also supports generative AI, large language models or LLMs (see migration notes), and integrations with Google Cloud services like BigQuery and Cloud Storage. 

### Vertex AI SDK for Python
[Vertex AI SDK for Python](https://github.com/googleapis/python-aiplatform)<Br>
`vertexai` Higher-level Python module within google-cloud-aiplatform for specific Vertex AI features(,including RAG and generative AI -- check for the depreciation notes).<br>
<mark>The Generative AI module in the Vertex AI SDK is deprecated and will no longer be available after June 24, 2026. The Google Gen AI SDK contains all the capabilities of the Vertex AI SDK, and supports many additional capabilities.</mark> For details, see the [migration guide](https://cloud.google.com/vertex-ai/generative-ai/docs/deprecations/genai-vertexai-sdk#migration).
### Google Gen AI SDK
[Google Gen AI SDK, `pip install google-genai`](https://github.com/googleapis/python-genai) Google Gen AI Python SDK provides an interface for developers to integrate Google's generative models into their Python applications. 

### Google Gen AI SDK
```python

# https://github.com/googleapis/python-genai
### Installation ###
pip install google-genai

### import ###
from google import genai
from google.genai import types

### Create a client ###
from google import genai

# Only run this block for Gemini Developer API
client = genai.Client(api_key='GEMINI_API_KEY')

# Only run this block for Vertex AI API
client = genai.Client(
    vertexai=True, project='your-project-id', location='us-central1'
)

### To create a client by configuring the necessary environment variables. ###
# Set the GEMINI_API_KEY or GOOGLE_API_KEY. If both are set, GOOGLE_API_KEY takes precedence
export GEMINI_API_KEY='your-api-key'

export GOOGLE_GENAI_USE_VERTEXAI=true
export GOOGLE_CLOUD_PROJECT='your-project-id'
export GOOGLE_CLOUD_LOCATION='us-central1'

# Environment variables will automatically be picked up by the client.
from google import genai
client = genai.Client()


```
### Google Vertex AI SDK
```python
### Installation ###
pip install --upgrade google-cloud-aiplatform

### import ###
import vertexai
from vertexai import types

# Instantiate GenAI client from Vertex SDK
client = vertexai.Client(project='my-project', location='us-central1')



### Agent Development Kit
[Agent Development Kit (ADK)](https://github.com/google/adk-python) An open-source, code-first Python toolkit for building, evaluating, and deploying sophisticated AI agents with flexibility and control.

```python
### Installation ###
# https://github.com/google/adk-python
pip install google-adk
```

### Agent2Agent (A2A) Protocol
[Agent2Agent (A2A) Protocol](https://github.com/a2aproject/a2a-python) A Python library that helps run agentic applications as A2AServers following the Agent2Agent (A2A) Protocol

```python
### Installation ###
# https://github.com/a2aproject/a2a-python
uv add a2a-sdk          # uv
pip install a2a-sdk     # or pip
```

### Other Options
```bash
# Running on a Specific Address (Default is to bind on address ('127.0.0.1', 8000))
adk web --host 0.0.0.0 --port 8080 --reload
# Specify the .env file path when running ADK commands (By default, the ADK looks for an .env file in the cwd)
adk web --env-file /mnt/e/zhaohuiwang/dev/custom_configs/my_env.env 
# optional --verbose
# or set environmenta variable directly, e.g. export GOOGLE_GENAI_USE_VERTEXAI=TRUE
# or added them to your shell profile, e.g., ~/.bashrc

```

## References

- [Docs - Google Agent Development Kit](https://google.github.io/adk-docs/)
- [Github - Vertex AI SDK for Python](https://github.com/googleapis/python-aiplatform)
- [Docs - Generative AI on Vertex AI](https://cloud.google.com/vertex-ai/generative-ai/docs)
- [Docs - Generative AI on Google Cloud](https://cloud.google.com/ai/generative-ai?hl=en)
- [Github - Generative AI on Google Cloud](https://github.com/GoogleCloudPlatform/generative-ai)
- [Docs - Google Model versions and lifecycle](https://cloud.google.com/vertex-ai/generative-ai/docs/learn/model-versions)
- [Docs - LangChain](https://python.langchain.com/docs/introduction/)
- [Docs - LanChain Embedding models](https://python.langchain.com/docs/integrations/text_embedding/)
- [Docs - LangChian Integrations Provider/Components](https://python.langchain.com/docs/integrations/providers/)

- [Github - NirDiamant GenAI_Agents](https://github.com/NirDiamant/GenAI_Agents?tab=readme-ov-file)
- [Github - RAGFlow](https://github.com/infiniflow/ragflow?tab=readme-ov-file)