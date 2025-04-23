import google.generativeai as genai

def configure_gemini():
    genai.configure(api_key="AIzaSyALDB8gw3k0_AU7eKfuLVDtDSrlH_rHB6g")  # Substitua pela sua API KEY

def generate_summary(text):
    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content(f"Resuma o seguinte texto: {text}")
    return response.text.strip()

def translate_text(text, language):
    language_names = {
        'pt': 'Português',
        'en': 'Inglês',
        'fr': 'Francês',
        'ru': 'Russo'
    }

    target_language = language_names.get(language, language)  # Se for nome já por extenso, usa direto

    prompt = f"Traduza o seguinte texto para {target_language}:\n\n{text}"
    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content(prompt)
    return response.text.strip()
