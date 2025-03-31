import streamlit as st
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

# 環境変数の読み込み
load_dotenv()

# LLMからの回答を取得する関数
def get_llm_response(input_text, expert_type):
    # 専門家の種類に応じたシステムメッセージを設定
    system_messages = {
        "医療専門家": "あなたは医療分野の専門家です。患者にわかりやすく説明してください。",
        "法律専門家": "あなたは法律分野の専門家です。法律に基づいて正確に回答してください。",
        "技術専門家": "あなたは技術分野の専門家です。技術的な詳細を簡潔に説明してください。"
    }
    system_message = system_messages.get(expert_type, "あなたは一般的な専門家です。")

    # LangChainのChatOpenAIを使用して応答を生成
    chat = ChatOpenAI(temperature=0.7)
    messages = [
        SystemMessage(content=system_message),
        HumanMessage(content=input_text)
    ]
    response = chat(messages)
    return response.content

# Streamlitアプリの構築
st.title("専門家に質問できるアプリ")
st.write("このアプリでは、専門家に質問をして回答を得ることができます。以下のフォームに質問を入力し、専門家の種類を選択してください。")

# 入力フォーム
input_text = st.text_area("質問を入力してください:", placeholder="例: 健康診断の結果について教えてください。")

# ラジオボタンで専門家の種類を選択
expert_type = st.radio(
    "専門家の種類を選択してください:",
    ("医療専門家", "法律専門家", "技術専門家")
)

# 送信ボタン
if st.button("送信"):
    if input_text.strip():
        # LLMからの回答を取得
        response = get_llm_response(input_text, expert_type)
        # 結果を表示
        st.subheader("専門家からの回答:")
        st.write(response)
    else:
        st.warning("質問を入力してください。")