🚀 AI-Powered Amazon Product Recommender using RAG
A full-stack AI project that helps users find products through intelligent conversations using Retrieval-Augmented Generation (RAG).
🔧 Tech Stack

Frontend: Streamlit (Interactive chat interface)
Vector Database: AstraDB (Scalable cloud storage)
Embeddings: HuggingFace BAAI/bge-base-en-v1.5 (Text-to-vector conversion)
LLM: Google Gemini 2.5 Flash (Fast & accurate responses)
Framework: LangChain (RAG pipeline orchestration)
Data: Amazon product reviews CSV

⚡ How it works

Product reviews are converted to vector embeddings and stored in AstraDB
User asks: "Show me wireless headphones under $100"
System retrieves relevant product data using semantic search
LLM generates personalized recommendations based on actual reviews
Chat interface maintains conversation context

💡 Key Features
✅ Real-time product recommendations
✅ Conversational AI interface
✅ Context-aware responses using chat history
✅ Scalable vector database architecture
✅ Easy deployment with Streamlit
🎯 Business Impact
This approach can increase e-commerce conversion rates by providing personalized, context-aware product suggestions instead of basic keyword matching.