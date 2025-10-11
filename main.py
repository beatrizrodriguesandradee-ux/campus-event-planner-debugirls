def main():
    listaEventos = []
    print("Bem-vindo ao Planejador de Eventos do Campus")

    while True:
        displayMenu()
        escolha = getEscolhaDoUsuario()

        if escolha == 1:
            _input_evento_e_adicionar(listaEventos)
        if escolha == 2:
            eventos = listarEventos(listaEventos)
            if not eventos:
                print("Nenhum evento cadastrado.")
            else:
                print("\n--- Eventos ---")
                for e in eventos:
                    _mostrar_evento(e)
        if escolha == 3:
            cat = input("Categoria para filtrar: ").strip()
            filtrados = filtrarEventosPorCategoria(listaEventos, cat)
            if not filtrados:
                print("Nenhum evento encontrado para essa categoria.")
            else:
                print("\nEventos na categoria", cat, ":")
                for e in listarEventos(filtrados):
                    _mostrar_evento(e)
        if escolha == 4:
            try:
                id_str = input("ID do evento a marcar como participado: ").strip()
                id_ = int(id_str)
                ok = marcarEventoAtendido(listaEventos, id_)
                if ok:
                    print("Evento marcado como participado.")
                else:
                    print("Evento não encontrado.")
            except:
                print("ID inválido. Informe um número inteiro.")
        if escolha == 5:
            gerarRelatorio(listaEventos)
        if escolha == 6:
            chave = input("Informe o ID ou nome do evento a deletar: ").strip()
            try:
                chave_int = int(chave)
                ok = deletarEvento(listaEventos, chave_int)
            except:
                ok = deletarEvento(listaEventos, chave)
            if ok:
                print("Evento deletado com sucesso.")
            else:
                print("Evento não encontrado.")
        if escolha == 7:
            termo = input("Termo para buscar no nome: ").strip()
            encontrados = procurarEventoPorNome(listaEventos, termo)
            if not encontrados:
                print("Nenhum evento encontrado com esse termo.")
            else:
                print("\nEventos encontrados para:", termo)
                for e in encontrados:
                    _mostrar_evento(e)
        if escolha == 8:
            print("Saindo. Até logo!")
            break
        if escolha < 1 or escolha > 8:
            print("Escolha inválida. Tente novamente.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nPrograma interrompido pelo usuário. Saindo...")
        sys.exit(0)