import streamlit as st
import youtube_utils
import gemini_utils

def main():
    # Configurações da página
    st.set_page_config(page_title="Resumo de Vídeos YouTube com Gemini", page_icon="🎬", layout="centered")

    # Estilo com gradiente Flare + botões e input customizados
    st.markdown(
        """
        <style>
            .stApp {
                background: linear-gradient(to right, #F12711, #F5AF19);
                color: white;
            }
            h1, h2, h3, h4, h5, h6, p, label {
                color: white !important;
            }
            .stTextInput > div > div > input {
                background-color: #ffffffcc;
                color: black;
                border-radius: 8px;
                padding: 8px;
            }
            .stButton>button {
                background-color: #ffffffdd;
                color: black;
                border-radius: 12px;
                padding: 0.5em 1.2em;
                border: none;
                transition: all 0.3s ease;
                font-weight: bold;
            }
            .stButton>button:hover {
                background-color: #000000;
                transform: scale(1.03);
                box-shadow: 0 4px 10px rgba(0,0,0,0.2);
                border: 1px solid #333;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Cabeçalho
    st.markdown("""
        <div style='text-align: center; padding: 10px;'>
            <h1>🎥 YouTube Transcript Summarizer do ZeroZero</h1>
            <p style='font-size: 18px;'>Resuma vídeos do YouTube com a inteligência do <b>coimbrazin</b> (powered by Gemini)</p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # Entrada da URL
    video_url = st.text_input("📎 Insira a URL do vídeo do YouTube:", "https://youtu.be/Ys7-6_t7OEQ?feature=shared")

    if video_url:
        try:
            video_id = youtube_utils.extract_video_id(video_url)
            video_title = youtube_utils.get_video_title(video_url)
            transcript = youtube_utils.get_transcript(video_id)

            if video_title:
                st.success(f"🎬 Título do Vídeo: {video_title}")

            if transcript:
                with st.expander("📄 Ver Transcrição Completa"):
                    st.write(transcript)

                st.markdown("---")
                if st.button("🚀 Gerar Resumo com coimbrazin AI"):
                    with st.spinner("Enviando para o cérebro do coimbrazin AI..."):
                        gemini_utils.configure_gemini()
                        summary = gemini_utils.generate_summary(transcript)

                    if summary:
                        st.markdown("## 🧠 Resumo Gerado por coimbrazin AI:")
                        st.markdown(f"""
                            <div style='
                                background: rgba(255, 255, 255, 0.15);
                                border-radius: 16px;
                                padding: 20px;
                                color: white;
                                font-size: 16px;
                                line-height: 1.6;
                                box-shadow: 0 8px 32px 0 rgba( 31, 38, 135, 0.37 );
                                backdrop-filter: blur(8px);
                                -webkit-backdrop-filter: blur(8px);
                                border: 1px solid rgba(255, 255, 255, 0.18);
                            '>
                                {summary}
                            </div>
                        """, unsafe_allow_html=True)
                    else:
                        st.error("⚠️ Falha ao gerar resumo com coimbrazin AI")
            else:
                st.error("😕 Não foi possível obter a transcrição do vídeo.")

        except Exception as e:
            st.error(f"💥 Ocorreu um erro: {e}")

if __name__ == "__main__":
    main()
