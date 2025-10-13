import sys

_next_id = 1

def _generate_id():
    global _next_id
    id_ = _next_id
    _next_id += 1
    return id_

def validarData(dataStr):
    try:
        datetime.strptime(dataStr, "%Y-%m-%d")
        return True
    except:
        return False

def adicionarEvento(listaEventos, nome, data, local, categoria):
    if nome.strip() == "":
        print("Nome do evento não pode ser vazio")
        return None
    if not validarData(data):
        print("Data inválida — use AAAA-MM-DD")
        return None
    if local.strip() == "":
        print("Local não pode ser vazio")
        return None
    if categoria.strip() == "":
        print("Categoria não pode ser vazia")
        return None

    evento = {
        "id": _generate_id(),
        "nome": nome.strip(),
        "data": data,
        "local": local.strip(),
        "categoria": categoria.strip(),
        "participado": False
    }
    listaEventos.append(evento)
    return evento

def listarEventos(listaEventos):
    try:
        return sorted(listaEventos, key=lambda e: datetime.strptime(e["data"], "%Y-%m-%d"))
    except:
        return listaEventos

def procurarEventoPorNome(listaEventos, nome):
    nome_proc = nome.strip().lower()
    encontrados = [e for e in listaEventos if nome_proc in e["nome"].lower()]
    return encontrados

def deletarEvento(listaEventos, id_or_name):
    if isinstance(id_or_name, int):
        for i, e in enumerate(listaEventos):
            if e["id"] == id_or_name:
                del listaEventos[i]
                return True
        return False
    else:
        name = str(id_or_name).strip().lower()
        for i, e in enumerate(listaEventos):
            if e["nome"].lower() == name:
                del listaEventos[i]
                return True
        return False

def displayMenu():
    print("\n=== Planejador de Eventos do Campus ===")
    print("1. Adicionar um Evento")
    print("2. Ver Todos os Eventos")
    print("3. Filtrar por Categoria")
    print("4. Marcar Evento como Participado")
    print("5. Gerar Relatório")
    print("6. Deletar um Evento")
    print("7. Buscar por Nome")
    print("8. Sair")

def getEscolhaDoUsuario():
    try:
        escolha = int(input("\nEscolha uma opção: ").strip())
        return escolha
    except:
        return -1

def filtrarEventosPorCategoria(listaEventos, categoria):
    categ = categoria.strip().lower()
    return [e for e in listaEventos if e["categoria"].lower() == categ]

def marcarEventoAtendido(listaEventos, id_):
    for e in listaEventos:
        if e["id"] == id_:
            e["participado"] = True
            return True
    return False

def gerarRelatorio(listaEventos):
    total = len(listaEventos)
    por_categoria = {}
    participados = 0
    for e in listaEventos:
        if e.get("participado"):
            participados += 1
        cat = e.get("categoria", "(Sem categoria)")
        por_categoria[cat] = por_categoria.get(cat, 0) + 1

    if total > 0:
        perc_part = (participados / total) * 100
    else:
        perc_part = 0

    print("\n--- RELATÓRIO DE EVENTOS ---")
    print("Total de Eventos:", total)
    print("Por Categoria:", por_categoria)
    print("Participados: {:.0f}% ({}/{})".format(perc_part, participados, total))

def _mostrar_evento(evento):
    print("ID:", evento['id'], "|", evento['nome'], "|", evento['data'], "|", evento['local'], "|", evento['categoria'], "| Participado:", evento['participado'])

def _input_evento_e_adicionar(listaEventos):
    nome = input("Nome do evento: ").strip()
    data = input("Data (AAAA-MM-DD): ").strip()
    local = input("Local: ").strip()
    categoria = input("Categoria: ").strip()
    ev = adicionarEvento(listaEventos, nome, data, local, categoria)
    if ev:
        print("\nEvento adicionado com sucesso! (ID:", ev["id"], ")")