## 🎬 Vid Summarizer 🎬

**Resumo automático de vídeos com transcrição em português usando MoviePy, Faster-Whisper e OpenAI.**

## 📌 Descrição

O Vid Summarizer é uma aplicação web que permite aos usuários enviar vídeos, extrair o áudio, transcrevê-lo e gerar um resumo conciso do conteúdo. Ideal para quem deseja obter rapidamente o conteúdo principal de vídeo-aulas, por exemplo.

## 🚀 Tecnologias Utilizadas

* Django, MoviePy, Faster-Whisper, OpenAI GPT-3.5 Turbo, Python 3.10+.

---

## 🛠️ Instalação

Siga os passos abaixo para configurar e executar o projeto localmente:

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/Aramisbr/vid-summarizer.git
   cd vid-summarizer
   ```

2. **Crie e ative o ambiente virtual:**

   No Windows:

   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

   No Linux/macOS:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Instale as dependências:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure as variáveis de ambiente:**

   Crie um arquivo `.env` na raiz do projeto e adicione sua chave da OpenAI:

   ```env
   SK_OPENAI=sua_chave_aqui
   ```

5. **Aplique as migrações do banco de dados:**

   ```bash
   python manage.py migrate
   ```

6. **Execute o servidor:**

   ```bash
   python manage.py runserver
   ```

7. **Acesse a aplicação:**

   Abra o navegador e vá para (http://127.0.0.1:8000)

---

## 📄 Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

--

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.
