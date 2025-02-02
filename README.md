
# RAG Chatbot using LangChain and ChromaDB

This repository contains a Retrieval-Augmented Generation (RAG) chatbot built using LangChain and ChromaDB. The application is implemented in the `app.py` file and is deployed as a web application using Streamlit.

## Project Overview

This project was developed as a hackathon submission to address a real-world problem faced by the Department of Technical Education, Government of Rajasthan. During the admission process, numerous engineering and polytechnic institutes receive a high volume of inquiries from students, parents, and other stakeholders. These queries range from admissions and fee structures to scholarships and placement opportunities.

The traditional methods of handling these inquiries—through phone, email, or in-person visits demand significant manpower. This project aims to streamline the process by creating an AI-powered chatbot that serves as a virtual assistant, available 24/7 to provide instant responses to a wide range of questions. This solution not only enhances accessibility to important information but also reduces the workload on college staff.
### Key Features

1. Efficient Information Retrieval: The chatbot rapidly accesses and provides accurate information on topics such as admissions, fees, and scholarships using advanced NLP.
2. Enhanced User Experience: The chatbot interface is intuitive and capable of understanding natural language, making it user-friendly.
3. Reduced Workload: By automating responses to frequently asked questions, the chatbot reduces the need for human intervention, allowing staff to focus on more complex queries.
4. Data Insights: The chatbot gathers valuable data from user interactions, helping the department optimize its services.
## Getting Started

### Prerequisites

- Python 3.6 or later
- Streamlit
- LangChain
- ChromaDB

All required Python packages are listed in the `requirements.txt` file.

### Installation and Running the App

1. **Clone the repository (if applicable):**

   ```bash
   git clone https://github.com/Kunal-sharan/SSH_24_Techtronix.git
   cd SSH_24_Techtronix
   ```

2. **Install the required packages:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit application:**

   ```bash
   streamlit run app.py
   ```

This will start the Streamlit server, and you can interact with the RAG Chatbot by navigating to `http://localhost:8501` in your web browser.

### How the RAG Chatbot Works

- **LangChain:** This is used to manage the logic of the chatbot, combining language models with external data sources.
- **ChromaDB:** This is a vector database that stores and retrieves relevant documents or information to augment the language model's responses.
- **GROQ/Llama:** This is the actual llm used which utilises the query response from the vector database and returned embeddings to give a smooth and effective response.

The chatbot leverages these tools to retrieve information from ChromaDB and use it to generate accurate and contextually relevant responses.

### Application Structure

- **app.py:** The main script containing the Streamlit app and chatbot logic.
- **requirements.txt:** Lists the Python dependencies required to run the application.

### Deployment

To deploy the app on a hosting platform such as Streamlit Cloud, follow their documentation and ensure your repository contains both the `app.py` and `requirements.txt` files.

### Contributing

If you'd like to contribute to this project, feel free to fork the repository, make your changes, and submit a pull request.
---

!-- <<<<<<< HEAD
This is a [Next.js](https://nextjs.org) project bootstrapped with [`create-next-app`](https://nextjs.org/docs/app/api-reference/cli/create-next-app).

## Getting Started

First, run the development server:

```bash
npm run dev
# or
yarn dev
# or
pnpm dev
# or
bun dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

You can start editing the page by modifying `app/page.tsx`. The page auto-updates as you edit the file.

This project uses [`next/font`](https://nextjs.org/docs/app/building-your-application/optimizing/fonts) to automatically optimize and load [Geist](https://vercel.com/font), a new font family for Vercel.

## Learn More

To learn more about Next.js, take a look at the following resources:

- [Next.js Documentation](https://nextjs.org/docs) - learn about Next.js features and API.
- [Learn Next.js](https://nextjs.org/learn) - an interactive Next.js tutorial.

You can check out [the Next.js GitHub repository](https://github.com/vercel/next.js) - your feedback and contributions are welcome!

## Deploy on Vercel

The easiest way to deploy your Next.js app is to use the [Vercel Platform](https://vercel.com/new?utm_medium=default-template&filter=next.js&utm_source=create-next-app&utm_campaign=create-next-app-readme) from the creators of Next.js.

Check out our [Next.js deployment documentation](https://nextjs.org/docs/app/building-your-application/deploying) for more details.
=======
# Hackathon
>>>>>>> 8d5f8666ed7efd8eac0f09b2fe8d5ccaa6e1eabb -->
