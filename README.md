# 🤖 Bot de Agendamento para Discord com Flask + Render

Este projeto é um **bot para Discord** desenvolvido em **Python** utilizando as bibliotecas [discord.py](https://discordpy.readthedocs.io/) e [Flask](https://flask.palletsprojects.com/).
Ele envia notificações automáticas em horários pré-definidos em um canal do servidor do Discord, mencionando um cargo específico.
Além disso, conta com um **servidor Flask** para manter o bot ativo em plataformas como o [Render](https://render.com/).

---

## 🚀 Funcionalidades

* Envio automático de mensagens em horários configurados (eventos, boss, PVP, etc).
* Menção automática de um **cargo específico**.
* Comando manual `!teste` para validar o envio de mensagens.
* Servidor Flask rodando em paralelo para manter o serviço online no Render.
* Logs de debug para verificar se as mensagens foram enviadas corretamente.

---

## ⚙️ Tecnologias utilizadas

* **Python 3.10+**
* [discord.py](https://discordpy.readthedocs.io/) – interação com o Discord.
* [Flask](https://flask.palletsprojects.com/) – web server para Render.
* [pytz](https://pypi.org/project/pytz/) – manipulação de fuso horário.
* [threading](https://docs.python.org/3/library/threading.html) – rodar Flask em paralelo com o bot.

---

## 📌 Pré-requisitos

Antes de rodar o projeto, você precisa:

1. Criar um bot no [Portal de Desenvolvedores do Discord](https://discord.com/developers/applications).
2. Ativar **Intents de membros e mensagens**.
3. Criar um **servidor no Discord** e anotar:

   * **GUILD\_ID** (ID do servidor)
   * **CHANNEL\_ID** (ID do canal de texto onde as mensagens serão enviadas)
   * **ROLE\_ID** (ID do cargo a ser mencionado)
4. Configurar variáveis de ambiente:

```bash
TOKEN=seu_token_do_bot
GUILD_ID=XXXXXXXXXXXXXXXXXXX
CHANNEL_ID=XXXXXXXXXXXXXXXXXXX
ROLE_ID=XXXXXXXXXXXXXXXXXXX
PORT=10000
```

---

## ▶️ Como rodar localmente

Clone o repositório e instale as dependências:

```bash
git clone https://github.com/seuusuario/seu-repositorio.git
cd seu-repositorio
pip install -r requirements.txt
```

Crie um arquivo `.env` com as variáveis de ambiente necessárias e depois rode:

```bash
python bot.py
```

---

## 🌐 Deploy no Render

1. Crie um novo serviço no [Render](https://render.com/).
2. Configure as variáveis de ambiente no painel do Render.
3. Defina o **Start Command** como:

```bash
python bot.py
```

O Flask será responsável por manter o serviço rodando, enquanto o bot atua em paralelo.

---

## 📜 Exemplo de agendamento

O bot possui eventos configurados no dicionário `eventos`:

```python
eventos = {
    "12:55": "EVENTO PVP",
    "18:55": "BOSS RYUKUDDOU",
    "19:55": "EVENTO PVP"
}
```

* Você pode adicionar ou remover horários conforme necessário.
* O fuso horário usado é **America/Sao\_Paulo**.

---

## 🎮 Comandos disponíveis

* `!teste [mensagem]` → Envia uma mensagem manual mencionando o cargo configurado.
  Exemplo:

  ```
  !teste Verificação do bot
  ```

---

## 📄 Licença

Este projeto é de uso livre para fins pessoais e educacionais.

---
