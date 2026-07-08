# ⚽ Project Palanca – Sports Computer Vision
> **Mapeamento de Talento Através de Visão Computacional em Campos de Terra Batida**
> 
> *"O talento está no pé, o mérito está no dado."*

---

## 1. Visão Geral (The Pitch)
O **Projecto Kilamba** é um sistema automatizado de *Scouting* e Análise de Desempenho Desportivo baseado em Inteligência Artificial e Visão Computacional. 

O objetivo principal é democratizar o acesso ao futebol de elite em Angola, permitindo que jogadores talentosos de campeonatos de rua (inter-bairros) sejam avaliados por mérito puramente estatístico através de vídeos gravados por telemóveis comuns, quebrando o monopólio das influências e "cunhas".

---

## 2. Objetivos Principais (Milestones)

* **Automatização Total:** Eliminar a necessidade de registo manual de dados (fichas em papel ou digitação).
* **Acessibilidade Técnica:** O sistema deve ser capaz de processar vídeos com tremores, baixa resolução (720p/1080p de telemóveis) e variações de luz (campos abertos de terra batida).
* **Quantificação de Mérito:** Gerar um relatório final com métricas físicas e técnicas claras que possam ser comparadas num ranking baseado em dados reais.

---

## 3. Arquitetura do Software (The Pipeline)
O projeto está dividido em 4 módulos obrigatórios, desenvolvidos inteiramente em **Python**:

### Módulo 1: Pré-processamento de Vídeo (Input & Estabilização)
* **Função:** Receber o ficheiro de vídeo (`.mp4`, `.avi`) e aplicar filtros de imagem.
* **Tecnologia:** OpenCV.
* **Restrição:** O script deve compensar o movimento da câmara (tremor das mãos) usando algoritmos de fluxo ótico (*optical flow*) para suavizar os frames antes da inferência da IA.

### Módulo 2: Deteção e Rastreio Inteligente (Object Detection)
* **Função:** Localizar e seguir os elementos essenciais em cada frame.
* **Tecnologia:** YOLO (You Only Look Once).
* **Regras de Rastreio:**
  * Identificar a **Bola** (atribuir um ID fixo).
  * Identificar as **Pessoas** no campo e isolar o "Jogador Alvo".
  * Separar as equipas pela cor da camisola usando filtros de cor no espaço de cor HSV/RGB.

### Módulo 3: Motor de Métricas Lógicas (The Core Engine)
* **Função:** Transformar pixéis e coordenadas em dados de performance reais.
* **Matemática Aplicada:**
  * **Velocidade e Distância:** Calcular a variação de posição $\Delta s$ entre frames em relação ao tempo $\Delta t$.
  * **Matriz de Homografia:** Converter a perspetiva lateral e angular da câmara de telemóvel para um plano 2D visto de cima (visão aérea do campo).
  * **Análise de Proximidade:** Registar um passe ou remate automaticamente quando a distância entre a *bounding box* do jogador e a da bola for inferior a um limite limite crítico de pixéis.

### Módulo 4: Interface e Relatório (The Dashboard)
* **Função:** Apresentar os dados de forma visual e intuitiva para investidores, treinadores ou olheiros.
* **Tecnologia:** Streamlit (Python) ou React.
* **Output Obrigatório:** Mapa de calor (Heatmap) de posicionamento, Gráfico de velocidade ao longo do tempo, e Contador de Ações (Passes, Remates, Velocidade Máxima).

---

## 4. Restrições do Projeto (Constraints)
Para garantir o rigor no desenvolvimento e o entendimento profundo dos algoritmos subjacentes, aplicam-se as seguintes regras de engenharia:

* 🚫 **Proibido:** Usar plataformas prontas de IA sem código (*no-code*). Toda a integração de dados e manipulação de arrays matriciais deve ser programada manualmente.
* ⚡ **Gestão de Recursos:** O processamento de frames consome muita largura de banda de CPU/GPU. O código deve ser otimizado algoritmicamente para evitar *memory leaks* e não crashar computadores comuns de desenvolvimento.

---

## 5. Próximos Passos (Sprint 0)
Antes de iniciar a escrita dos scripts de IA, a fase de infraestrutura foca-se em:

1. **Recolha de Amostras:** Conseguir 3 vídeos curtos (10 a 20 segundos) de teste. Um gravado de perto, um gravado de lado (perspetiva de bancada/lateral) e um com tremores acentuados de câmara.
2. **Ambiente de Desenvolvimento:** Configuração do interpretador Python (v3.x), isolamento do projeto via ambiente virtual (`venv`), instalação de dependências core (`pip install opencv-python ultralytics`) e versionamento inicial via Git.
