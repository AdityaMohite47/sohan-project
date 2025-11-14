from langchain_google_genai import ChatGoogleGenerativeAI
import dotenv

dotenv.load_dotenv()
LLM = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.7)