# Knowledge Graph RAG System

A comprehensive implementation of Retrieval-Augmented Generation (RAG) systems using knowledge graphs and Neo4j. This repository demonstrates how to build, query, and leverage knowledge graphs for enhanced AI applications.

## Overview

This project showcases different approaches to building and utilizing knowledge graphs for RAG systems:

1. **Simple Knowledge Graph** - Basic Neo4j implementation for creating and querying knowledge graphs
2. **Knowledge Graph RAG** - Advanced RAG system using knowledge graphs for structured information retrieval
3. **Healthcare Knowledge Graph** - Domain-specific implementation for healthcare data
4. **Text Preparation for RAG** - Tools for preparing and processing text data for RAG systems

## Features

- Neo4j integration for knowledge graph storage and querying
- LangChain integration for RAG pipeline implementation
- Entity extraction and relationship mapping
- Full-text search capabilities
- Hybrid retrieval combining structured and unstructured data
- Conversation history handling for contextual responses
- Domain-specific implementations (healthcare, Roman Empire)

## Project Structure

```
knowledge-graph-rag/
├── simple_kg/                  # Basic knowledge graph implementation
│   └── kg_simple.py            # Simple Neo4j operations
├── kgraph_rag/                 # Advanced RAG with knowledge graphs
│   └── roman_emp_graph_rag.py  # Roman Empire knowledge graph RAG
├── prep_text_for_rag/          # Text preparation tools
│   └── app.py                  # Text processing application
├── healthcare/                 # Healthcare domain implementation
│   ├── health_care_kg.py       # Healthcare knowledge graph
│   ├── health_care_langchain.py # Healthcare RAG with LangChain
│   └── healthcare.csv          # Sample healthcare data
├── requirements.txt            # Project dependencies
└── .env                        # Environment variables (not tracked in git)
```

## Prerequisites

- Python 3.8+
- Neo4j Aura instance or local Neo4j database
- OpenAI API key

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Badribn0612/knowledge-graph-rag.git
   cd knowledge-graph-rag
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file with your credentials:
   ```
   NEO4J_URI=your_neo4j_uri
   NEO4J_USERNAME=your_neo4j_username
   NEO4J_PASSWORD=your_neo4j_password
   AURA_INSTANCENAME=your_aura_instance_name
   OPENAI_API_KEY=your_openai_api_key
   ```

## Usage

### Simple Knowledge Graph

```python
from simple_kg.kg_simple import connect_and_query

# Connect to Neo4j and run a simple query
connect_and_query()
```

### Knowledge Graph RAG

```python
from kgraph_rag.roman_emp_graph_rag import chain

# Ask a question about the Roman Empire
response = chain.invoke({
    "question": "Who was the first Roman emperor?",
})

print(response)
```

### Healthcare Knowledge Graph

```python
from healthcare.health_care_langchain import health_care_chain

# Ask a question about healthcare
response = health_care_chain.invoke({
    "question": "What are the symptoms of diabetes?",
})

print(response)
```

## Key Components

### Knowledge Graph Creation

The system supports multiple approaches to knowledge graph creation:
- Manual entity and relationship creation
- Automated extraction from text using LLMs
- Import from structured data (CSV)

### RAG Implementation

The RAG system combines:
- Structured data retrieval from the knowledge graph
- Unstructured data retrieval using vector search
- Context-aware question answering with conversation history

### Entity Extraction

The system uses LLMs to extract entities from text, which are then stored in the knowledge graph for future retrieval.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Acknowledgments

- Neo4j for the graph database
- LangChain for the RAG framework
- OpenAI for the language models
