
# AI Commerce Agent

This project creates an AI-powered agent as a REST API for an e-commerce website, offering the following features:

1. **Q&A**: General question-answering using GPT-3.  
2. **Text-based Recommendations**: Products recommended based on text queries.  
3. **Image-based Search**: Find products similar to an uploaded image using CLIP.

## Features

### 1. Q&A  
The agent can answer general questions using GPT-3 (OpenAI's language model). You can send queries to the `/qa` endpoint, and the model will provide a relevant answer based on the input question.

### 2. Text-based Recommendations  
You can get product recommendations by sending a text query to the `/recommend` endpoint. The agent will use a SentenceTransformer model to understand the input query and return a list of recommended products.

### 3. Image-based Search  
Upload an image, and the agent will return products similar to the uploaded image. This is powered by the CLIP model from OpenAI, which is capable of understanding images in the context of textual descriptions.

## Setup

1. **Clone the Repository**  
   Clone the repository to your local machine and navigate to the project directory:
   ```bash
   git clone https://github.com/your-repo/ai-commerce-agent.git
   cd ai-commerce-agent
   ```

2. **Install the required dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

3. **Update the .env file and set the required environment variable**  
   Update `.env` file by copying the provided `.env.example` file and set the required variable:

   ```
   OPENAI_API_KEY=your_openai_api_key
   ```
### Endpoints:
- `POST /qa`: Ask a general question.
- `POST /recommend`: Get text-based product recommendations.
- `POST /image-search`: Upload an image and get similar product suggestions.