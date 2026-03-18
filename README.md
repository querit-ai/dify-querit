# Querit Search Plugin for Dify

[![Version](https://img.shields.io/badge/version-0.0.1-blue)](https://github.com/querit-ai/dify-querit)
[![Python](https://img.shields.io/badge/python-3.12+-green)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-orange)](LICENSE)

**Author:** querit-ai
**Version:** 0.0.2
**Type:** Dify Tool Plugin

---

## What is Querit.ai Search?

Querit.ai Search is a retrieval system specifically designed for generative LLMs invocation scenarios, providing real-time search results.

Limited training data and local knowledge bases restrict LLMs, leading to hallucinations and timeliness issues when handling complex or real-time queries. To address this, AI search needs to provide retrieval services that are **real-time**, **authoritative**, **accurate**, **high-quality**, and **comprehensive**. Therefore, we offer a Web Search API that seamlessly integrates with your LLM applications, giving you access to authoritative, accurate, and high-quality information from across the web.

### Why Querit.ai?

- **Comprehensive Content**: Massive global index spanning nearly 20 countries and 10 languages with hundreds of billions of web pages.
  - Countries include: United States, India, United Kingdom, Canada, etc.
  - Languages include: English, Spanish, Portuguese, etc.
- **Strong Capabilities**: Flexible retrieval options allowing enterprises to customize results for specific scenarios.
- **Excellent Results**: Delivers accurate, authoritative, and high-quality content coverage.
- **High Performance**: Ensures enterprise-grade high availability with ultra-low latency.

---

## Description

This plugin integrates **Querit.ai** real-time search and retrieval services into **Dify** platform through standardized APIs, allowing agents to query external knowledge sources with natural language and obtain structured search results.

Querit.ai provides a global-scale multilingual indexing and semantic understanding engine for more reliable and precise results, with integrated filtering and ranking strategies to enhance LLM context support.

### Features

- Real-time web search for LLM applications
- Natural language query understanding
- Structured search results with URLs, images, and data
- Global multi-language coverage
- Low-latency enterprise-grade API

---

## Installation

### Prerequisites

- Python 3.11+
- Dify platform (self-hosted or cloud)

### Steps

1. Clone this repository:
   ```bash
   git clone https://github.com/querit-ai/dify-querit.git
   cd dify-querit
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Copy the environment file and configure your API key:
   ```bash
   cp .env.example .env
   ```

4. Get your Querit API key from [Querit Dashboard](https://www.querit.ai/en/dashboard/api-keys) and add it to the `.env` file.

5. Run the plugin:
   ```bash
   python -m main
   ```

---

## Usage

### In Dify

1. Install the plugin in your Dify workspace
2. Configure the Querit API key in the plugin settings
3. Use the Querit Search tool in your AI agents/workflows

### API Endpoint

The plugin uses the Querit Search API:

```
POST https://api.querit.ai/v1/search
```

**Parameters:**
- `query`: The search query (natural language)
- `count`: Number of results to return (optional)

---

## Development

See [GUIDE.md](GUIDE.md) for detailed development documentation.

### Plugin Structure

```
dify-querit/
├── main.py                 # Plugin entry point
├── manifest.yaml           # Plugin manifest
├── provider/               # Provider configuration
│   ├── dify_querit.py
│   └── dify_querit.yaml
├── tools/                  # Tool definitions
│   ├── dify_querit.py
│   └── dify_querit.yaml
├── _assets/                # Icons and assets
├── README.md               # This file
├── GUIDE.md                # Development guide
└── requirements.txt        # Python dependencies
```

---

## Publishing to Dify Marketplace

This plugin follows the official Dify plugin publishing workflow:

1. **Develop & Test**: Make changes in this repository and test locally
2. **Create Release**: Publish a new release with a version tag (e.g., v0.0.1)
3. **Auto-Publish**: GitHub Actions will automatically:
   - Package the plugin
   - Create a branch in [dify-plugins](https://github.com/querit-ai/dify-plugins)
4. **Submit to Dify**: The branch will be merged into the official Dify plugin repository

For detailed publishing instructions, see [CONTRIBUTING.md](CONTRIBUTING.md#publishing-releases).

---

## License

See [LICENSE](LICENSE) for details.

---

## Support

- [GitHub Issues](https://github.com/querit-ai/dify-querit/issues)
- [Querit Website](https://www.querit.ai/)
- [Querit Dashboard](https://www.querit.ai/en/dashboard)
