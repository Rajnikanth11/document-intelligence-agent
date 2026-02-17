# document-intelligence-agent

## Overview
This project implements a tool-based AI agent that processes business documents
(PDF/images), extracts structured fields, validates business rules, and produces
explainable decisions using DeepSeek LLM planning.

Pipeline:
OCR → Agent Planning → Tool Execution → Validation → Decision

---

## Features
- OCR ingestion (PDF / image)
- Tool-based AI agent loop
- Schema-driven field extraction
- Rule-based validation engine
- Explainable decision outputs
- DeepSeek LLM-powered reasoning

---

## Architecture
Document Input
|
v
OCR Layer (Tesseract)
|
v
Agent Planner (DeepSeek)
|
v
Tool Executor
|
v
Decision Output


