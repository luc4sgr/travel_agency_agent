# ✈️ Trip Planner Crew

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![Python](https://img.shields.io/badge/Python-3.10+-green)
![License](https://img.shields.io/badge/license-MIT-orange)

> Um sistema inteligente de planejamento de viagens utilizando arquitetura multiagente para criar roteiros personalizados de 7 dias com base em interesses, orçamento, clima e eventos culturais.

## 🚀 Visão Geral

Trip Planner Crew é uma solução de IA avançada que demonstra o poder da colaboração entre agentes autônomos para resolver problemas complexos de planejamento de viagem. Através da orquestração de múltiplos agentes especializados, o sistema cria experiências de viagem personalizadas e contextualmente relevantes.

## 🎯 Principais Recursos

- **Roteiros personalizados de 7 dias** adaptados aos seus interesses específicos
- **Recomendações sensíveis ao orçamento** para acomodações, restaurantes e atividades
- **Sugestões baseadas em clima e sazonalidade** para otimizar sua experiência
- **Descoberta de eventos culturais e locais** durante o período da viagem
- **Interface intuitiva** para definir preferências e visualizar resultados

## 🧠 Tecnologias e Arquitetura

### Stack Tecnológico

| Tecnologia | Função |
|------------|--------|
| `Python 3.10+` | Linguagem base do projeto |
| `CrewAI` | Framework para orquestração de agentes autônomos |
| `LangChain` | Integração com modelos de linguagem |
| `OpenAI GPT-3.5` | Geração de conteúdo e recomendações primárias |
| `Groq LLaMA 3` | Alternativa otimizada para custo/desempenho |
| `Serper.dev` | API de busca para recuperação de informações em tempo real |
| `Streamlit` | Interface do usuário interativa e responsiva |
| `pytest` | Framework de testes automatizados |

### Arquitetura MVC

```
trip_planner/
├── main.py                      # Ponto de entrada da aplicação
├── config/
│   └── env.py                   # Gerenciamento de variáveis de ambiente
├── controllers/
│   └── trip_controller.py       # Orquestração do fluxo de planejamento
├── models/
│   ├── agents.py                # Definição dos agentes especializados
│   ├── tasks.py                 # Tarefas atribuídas a cada agente
│   └── trip_data.py             # Estruturas de dados da viagem
├── views/
│   └── ui.py                    # Interface com Streamlit
├── tests/
│   └── test_trip_controller.py  # Testes unitários e de integração
├── .env                         # Variáveis de ambiente (não versionado)
├── requirements.txt             # Dependências do projeto
└── README.md                    # Esta documentação
```

## 🧩 Funcionamento do Sistema

### Agentes Especializados

O sistema utiliza uma equipe de agentes de IA com papéis específicos:

1. **Especialista em Destinos** - Analisa preferências e recomenda pontos de interesse
2. **Planejador de Atividades** - Organiza atrações em um cronograma otimizado
3. **Pesquisador Local** - Descobre eventos únicos e experiências autênticas
4. **Consultor de Orçamento** - Ajusta recomendações para adequar-se ao orçamento

### Fluxo de Trabalho

1. O usuário fornece destino, datas, interesses e orçamento
2. O controlador orquestra a colaboração entre agentes
3. Cada agente executa tarefas especializadas e compartilha resultados
4. O sistema integra as contribuições em um plano de viagem coeso
5. A interface apresenta o roteiro finalizado para o usuário

## ⚙️ Instalação e Uso

### Pré-requisitos

- Python 3.10 ou superior
- Chaves de API para serviços externos (OpenAI/Groq e Serper)

### Configuração

```bash
# Clonar o repositório
git clone https://github.com/seu-usuario/trip-planner-crew.git
cd trip-planner-crew

# Criar e ativar ambiente virtual
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
# ou
.venv\Scripts\activate     # Windows

# Instalar dependências
pip install -r requirements.txt
```

### Configuração de Ambiente

Crie um arquivo `.env` na raiz do projeto:

```
OPENAI_API_KEY=sua-chave-openai
GROQ_API_KEY=sua-chave-groq
SERPER_API_KEY=sua-chave-serper
```

### Executando a Aplicação

```bash
streamlit run main.py
```

Acesse a interface em: http://localhost:8501

### Testes

```bash
pytest tests/
```

## 🔍 Exemplo de Uso

```python
# Exemplo de utilização programática
from controllers.trip_controller import TripController

controller = TripController()
trip_plan = controller.run_trip_plan(
    origin="São Paulo",
    destination="Paris", 
    date_range="2025-06-10 to 2025-06-17", 
    interests="gastronomia, arte, história"
)

print(trip_plan)
```

## 🚀 Roadmap

- [ ] **Sistema de mocking** para testes sem consumo de API
- [ ] **Containerização** com Docker para deploy simplificado
- [ ] **Autenticação de usuários** com OAuth ou JWT
- [ ] **Painel analítico** para comparação entre destinos
- [ ] **Integrações externas** com Google Calendar e APIs de voos
- [ ] **Versão móvel** otimizada para dispositivos Android e iOS

## 🤝 Contribuições

Contribuições são bem-vindas! Por favor, siga estes passos:

1. Faça fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-funcionalidade`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova funcionalidade'`)
4. Push para a branch (`git push origin feature/nova-funcionalidade`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo LICENSE para detalhes.

## 📚 Citações e Agradecimentos

- [CrewAI](https://docs.crewai.com) - Framework para orquestração de agentes
- [LangChain](https://python.langchain.com/docs/get_started/introduction) - Ferramentas para aplicações com LLMs
- [Streamlit](https://streamlit.io/) - Framework para aplicações de dados

---

Desenvolvido com ❤️ por Lucas Granjense