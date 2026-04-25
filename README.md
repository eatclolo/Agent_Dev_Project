# AI Agent System (Gemini + Tool Calling)

## Overview
This project is an AI Agent system using Gemini LLM with tool-calling capabilities.

## Architecture
User → FastAPI → Agent → Tools → Services → Response

## Features
- Tool-based agent system
- Gemini function calling
- Calculator tool (real)
- Weather / RAG tools (stub)
- FastAPI REST API

## Tech Stack
- Python
- FastAPI
- LangChain
- Google Gemini

## API
### POST /ask
Request:
{
  "query": "1+1"
}

Response:
{
  "answer": "2"
}

## Example
- "2+2" → Calculator
- "Tokyo weather" → Weather tool (stub)
- "What is RAG?" → RAG tool (stub)

## Design Philosophy
- Tool abstraction first
- Service layer separation
- Stub-first development for extensibility

## How to Run
uvicorn app.main:app --reload
