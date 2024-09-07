import os
import streamlit as st
import json
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_groq import ChatGroq
from langchain.chains import RetrievalQA

GROQ_API_KEY = "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"
os.environ["GROQ_API_KEY"] = GROQ_API_KEY

st.title("RAG-enabled Groq Chatbot")

@st.cache_resource
def load_and_process_documents():
    directory = "data/"
    all_documents = []
    count = 0
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            file_path = os.path.join(directory, filename)
            loader = TextLoader(file_path)
            documents = loader.load()
            all_documents.extend(documents)
            count += 1
    
    st.write(f"Total number of text files added: {count}")
    
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=2000,
        chunk_overlap=500,
        length_function=len,
        separators=["\n\n", "\n", " ", ""]
    )
    
    text_chunks = text_splitter.split_documents(all_documents)
    st.write(f"Added {len(text_chunks)} chunks to the Chroma database.")
    
    persist_directory = "clg_db"
    embedding = HuggingFaceEmbeddings()
    vectorstore = Chroma.from_documents(
        documents=text_chunks,
        embedding=embedding,
        persist_directory=persist_directory
    )
    
    return vectorstore

vectorstore = load_and_process_documents()

retriever = vectorstore.as_retriever()
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0
)

qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=retriever,
    return_source_documents=True
)

with open("college_name.json", "r") as file:
    name_data = json.load(file)

with open("data_expander.json", "r") as file:
    data_expander = json.load(file)
    print(data_expander[0])


links = ['http://www.ciitm.org/',
 'http://www.aietm.com/',
 'https://www.poornima.org/',
 'https://gitjaipur.com/',
 'https://jeckukas.org.in/',
 'https://www.iilmjaipur.ac.in/',
 'https://www.piet.poornima.org/']

st.title("An AI Assistant For Colleges Under Government Of Rajasthan.")

st.sidebar.title("Some questions you can ask")
st.sidebar.markdown("""
- Do you have data for IILM or PIET?
- Tell me about their alumni.
- What data do you have about JEC?
- Why should I take admission in Jaipur Engineering College?
""")

tab1, tab2 = st.tabs(["Colleges List", "Chatbot"])

with tab1: 
  with st.expander("List of 108 colleges under the government of Rajasthan."):
    st.markdown("""- Arya Institute of Engineering Technology & Management F-29 Omaxe City Phase-II Jaipur Ajmer Express
  - IILM Academy of Higher Learning Jaipur, Campus 35/95 Kumbha Marg RHB Colony Sector-10
  - Jaipur Engineering College SP-43 RIICO Industrial Area Kukas Jaipur-
  - Arya Institute of Engineering & Technology Jaipur-302028
  - Maharani Girls Engineering College Kalwara Near Mahendra World City (Sez) Ajmer
  - Arya College of Engineering & Information Road Kukas Jaipur-302028
  - Arya College of Engineering & Research Jaipur-302028
  - Chandrawati Group of Institutions Bharatpur -321001
  - Jaipur Institute of Engineering and Management NH-8 Jaipur - Ajmer Highway Village - Gadota
  - Poornima Group of Institutions - Faculty of Engineering BT-1 Bio-Technology Park RIICO Sitapura
  - Modi Institute of Management & Technology Modi Education Complex Dadabari Extension
  - International School of Informatics & Management Sector-12 Mahaveer Marg Mansarovar Jaipur-
  - Regional College for Education Research & Technology ISI-17 RIICO Institutional Area Sitapura Jaipur-
  - Pacific Business School Chitrakoot Nagar Bhuwana Scheme, Phase-1
  - Swami Vivekanand Institute of Management & Maa Saraswati Campus Near Jatwara Bridge
  - Arya College of Engineering & Information Technology SP-42 Kukas Industrial Area (RIICO) Delhi Road
  - Maharishi Arvind Institute of Science and Management Ambabari Circle Ambabari Jaipur-302023
  - Vedant College of Engineering & Technology Village-Tulsi Post-Jhakmund Distt- Bundi -
  - Arya Institute of Engineering & Technology SP-40 Kukas Industrial Area (RIICO) Kukas
  - Sine International Institute of Technology Balawala -Lakhna Road Via Sanganer Bazar
  - Arya Institute of Engineering Technology & Express Highway Jaipur Rajasthan-302026
  - Arya College of Engineering & Research Centre SP-40 Kukas Industrial Area (RIICO) Kukas
  - Poornima College of Engineering ISI-6 RIICO Institutional Area Goner Road
  - Vivekanand Institute of Technology Sisyawas NRI Road Jagatpura Jaipur-303012
  - Shri Digamber Institute of Technology NH-11, Mitrapura, Bhandarej Mode, Dausa-303501
  - Khandelwal Vaish Girls Institute of Technology Hanuman Nagar Block - E Vaishali Nagar Jaipur -
  - Biff & Bright College of Engineering & Technology Village & Post - Padasoli NH-8 Dudu Distt-Jaipur
  - Jaipur Institute of Technology - Group of Institutions Newta - Kalwara Road Kalwara Sanganer Distt. -
  - Govt. Engineering College Banswara-327001
  - Gurukul Institute of Engineering & Technology IPB-13 RIICO Institutional Area Ranpur Kota-
  - Sri Balaji College of Engineering & Technology Village-Macheda, Tehsil-Ajmer, Benad Road Dadi
  - Vedic Gurukul Institute of Engineering & Technology Gram-Pawalia, Tehsil-Sanaganer, Khasra Number-
  - Apex Institute of Engineering & Technology ISI-5 RIICO Institutional Area Sitapura Jaipur-
  - Compucom Institute of Technology & Management SP-3, 5, 5A, EPIP, RIICO Industrial Area
  - Rajasthan Engineering College Somnath Nagar,Ganeshpura Road, Dausa-303303
  - Compucom Institute of Information Technology & SP-5 EPIP RIICO Industrial Area Sitapura Jaipur-
  - Dr. Radhakrishnan Institute of Technology Kalwara Near Mahendra World City (Sez) Ajmer
  - Govt. Engineering College Village-Manchi, Tahshil-Karauli, Near Mega
  - Pinkcity Engineering College & Research Centre Gawar Jatan, Sanganer Jaipur-303905
  - S.S. Jain Subodh Management Institute Sector-5 Shiprapath Mansarovar Jaipur-302020
  - S. S. College of Engineering Jamar Kotra Road, Post-Umarda, Panchayat-
  - Advait Vedanta Institute of Technology Road Village Gangarampura Tehsil-Bassi Dist.Jaipur-303903
  - Baldev Ram Mirdha Institute Of Technology (East ITS-3 IT Park EPIP Sitapura Jaipur-302022
  - Asians Institute of Technology Post-Luhara, Tahsil-Neewai, Tonk-304019
  - Poornima Institute of Engineering & Technology ISI-2 RIICO Institutional Area Goner Road
  - Techno India NJR Institute of Technology Plot-SPL-T Bhamashah Industrial Area Kaladwas
  - Baldev Ram Mirdha Institute Of Technology nan
  - Rajdhani Engineering College Rohini Nagar Phase - I Sanganer Renwal Road
  - Shrinathji Institute of Technology & Engineering Upali Oden Nathdwara, Rajsamand-313301
  - Shankara Institute of Technology SP-44 RIICO Industrial Area Kukas Jaipur-
  - Rajasthan Institute of Engineering & Technology Bhankrota Ajmer Road Jaipur-302026
  - Govt. Engineering College Village Shyorana Near NH-11, Bharatpur-321303
  - Apex Institute of Management & Science Sector-5 V. T. Road Mansarovar Jaipur-302020
  - Shiv Charan Mathur Institute of Management & Pathik Nagar Bilwara (Raj.)-311001
  - Shankara International School of Management & SP-41C RIICO Industrial Area Kukas Jaipur-
  - Poddar Management and Technical Campus Gram - Fatehpuravas Vatika, Tehsil Chaksu, Jaipur-
  - Govt. Engineering College Govt. Polytechnic College Baran, NH-27, Village-
  - M. L. V. Textile & Engineering College Pratap Nagar Pur Road Bhilwara--311001
  - Vision School of Management Bojunda, Udaipur Road P. Box No. 23 Chittorgarh-
  - Kautilya Institute of Technology & Engineering ISI-16, RIICO Institutional Complex, Kautilya
  - Yagyavalkya Institute of Technology IP-1, Phase-IV, RIICO Industrial Area, Sitapura,
  - Aravali Institute Of Technical Studies Umarada Railway Station Udaipur-313015
  - Maharishi Arvind School of Management Studies Sector-2, Kaverapath, Mansarovar, Jaipur-302020
  - Geetanjali Institute of Technical Studies Airport Road Dabok, Taluka Mavli, Udaipur-
  - School of Architecture Apex Group of Institutions IS-2018 Ramchandrapura Industrial Area Sitapura
  - Modi Institute of Technology Nayagaon Rawatbhata Road Post Office-Borabas
  - Mahatma Gandhi Engineering College Bada Padampura Road Shivdaspura Tonk Road
  - Biyani Institute of Science & Management R-4 Sectior-3 Vidhyadhar Nagar Jaipur -302039
  - Om Kothari Institute of Management & Research A-1 Special I.P.I.A. Jhalawar Road Kota-324005
  - Rajasthan Institute of Engineering & Technology Village-Aachoda PO-Samelpura, Chittor-Kota
  - Shree Bhawani Niketan Institute of Technology & Shree Bhawani Niketan Shiksha Samiti Campus
  - Apex Institute of Engineering & Technology 302022
  - Buddha Institute of Architecture & Town Planning Seth Ji Ki Kundal Nh-8 Near Iim, Balicha Udaipur-
  - Sawai Madhopur College of Engineering and Technology Village-Thingla Sawai Madhopur Rajasthan-
  - Bal Krishna Institute of Technology Rajasthan-324005
  - Govt. Engineering College Village-Batavadi, Tehsil-Antah, Baran(Raj.)-325202
  - Govt. Engineering College Village & Tehsil-Surajpura, Dholpur-328001
  - Govt. Engineering College Behind Mayur Mill Kupda Dungarpur Road
  - Govt. Engineering College Highway, Karauli-322241
  - Maharishi Arvind International Institute of Technology IPA-1 RIICO, Institutional Area, Jhalawar Road,
  - Arya College of Engineering & Information Road, Kukas, Jaipur-302028
  - Pacific College of Engineering P.B. No. 12, Pratap Nagar Extension Airport Road
  - Swami Keshvanand Institute of Technology, Management Ramnagaria Jagatpura Jaipur-302017
  - Maharishi Arvind Institute of Engineering & Technology Sector-7 Madhyam Marg Mansarovar Jaipur-
  - Biff & Bright College of Engineering & Jaipur -303008
  - Compucom Institute of Technology & Sitapura Jaipur-302022
  - Rajasthan College of Engineering for Women Bhankrota Ajmer Road Jaipur-302026
  - Nathdwara Institute of Engineering & Technology Upali Oden Nathdwara Distt. - Rajsamand (Raj.)-
  - Advait Vedanta Institute of Technology Adved Knowledge Park Kanota-Sambhariya Road
  - Sunrise Group of Institution Near Bari Mata-Mandir, Tehsil-Girwa, Udaipur-
  - Tirupati College of Technical Education #262, Sector-26 Pratap Nagar Sanganer Jaipur-
  - Anand International College of Engineering 814, Near Kanota Agra Road Jaipur-303012
  - Rajasthan Technical University, Kota Akelgarh Rawatbhata Road Kota-324010
  - Govt. Engineering College Village-Chandlai Sunel Road Tehsil- Jhalarapatan
  - Jagannath Gupta Institute of Engineering & Technology Plot No. IP-2&3 Phase IV Sitapura Industrial Area
  - Acharya Shree Nanesh Samta Mahavidhyalaya Nanesh Nagar Danta Tehsil-Kapasan Distt-
  - Bal Krishna Institute of Technology IPC-15 RIICO Institutional Area Ranpur Kota
  - Geetanjali Institute of Technical Studies 313022
  - S. S. Jain Subodh P. G. College Rambagh Circle Jaipur-302004
  - Stani Memorial College of Engineering & Technology Phagi Jaipur-303005
  - Global Institute of Technology ITS-1 IT Park EPIP Sitapura Jaipur-302022
  - Aishwarya Institute of Management & Information 1-4D Block, Adarsh Nagar, University Road,
  - Chandrawati Group of Institutions NH-11 Opposite Ghana National Park Bharatpur -
  - Jaipur Engineering College & Research Centre Sri Ram Ki Nangal, Via-Vitika, Opp. EPIP Gate,
  - Shankara Institute of Management SP-44 RIICO Industrial Area Kukas Jaipur-
  - Biff & Bright College of Technical Education Village & Post - Padasoli NH-8 Dudu Distt-Jaipur
  - Aayojan School of Architecture ISI-4 RIICO Institutional Area Sitapura Goner
  - Dr. Radhakrishnan Institute of Technology Ajmer Road Jaipur-302037""")

  st.success("Out of 108 colleges, we’ve implemented a RAG model for 6, with overviews provided below. To use the chatbot, please follow the next step.")

  for i, college_name in enumerate(name_data):
    st.markdown(f"""
        <a href="{links[i]}" target="_blank" style="text-decoration: none; color: #1f77b4;">
            {i + 1}. {college_name}
        </a>
    """, unsafe_allow_html=True)

    with st.expander(f"More about {college_name}"):
        st.markdown(data_expander[i])

with tab2:
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    if prompt := st.chat_input("What is your question?"):
        st.chat_message("user").markdown(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})
    
        with st.spinner("Generating response..."):
            response = qa_chain.invoke({"query": prompt})
    
        with st.chat_message("assistant"):
            st.markdown(response["result"])
        st.session_state.messages.append({"role": "assistant", "content": response["result"]})
    
        with st.expander("View Source Documents"):
            for doc in response["source_documents"]:
                st.write(doc.page_content)
                st.write(f"Source: {doc.metadata.get('source', 'Unknown')}")
                st.write("---")
    
    st.sidebar.title("About")
    st.sidebar.info("This is a RAG-enabled chatbot using Groq and Langchain. It answers questions based on the loaded text documents.")
    st.sidebar.write("Model: llama-3.1-8b-instant")
