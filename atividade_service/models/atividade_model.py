atividades = [
    {
        'id_atividade': 1,
        'id_disciplina': 1,
        'enunciado': 'Crie um app de todo em Flask',
        'respostas': [
            {'id_aluno': 1, 'resposta': 'todo.py', 'nota': 9},
            {'id_aluno': 2, 'resposta': 'todo.zip.rar'},
            {'id_aluno': 4, 'resposta': 'todo.zip', 'nota': 10}
        ]
    },
    {
        'id_atividade': 2,
        'id_disciplina': 1,
        'enunciado': 'Crie um servidor que envia email em Flask',
        'respostas': [
            {'id_aluno': 4, 'resposta': 'email.zip', 'nota': 10}
        ]
    }
]

class AtividadeNotFound(Exception):
    pass

class InvalidAtividadeData(Exception):
    pass

def listar_atividades():
    return atividades

def obter_atividade(id_atividade):
    for atividade in atividades:
        if atividade['id_atividade'] == id_atividade:
            return atividade
    raise AtividadeNotFound

def criar_atividade(dados):
    if 'id_disciplina' not in dados or 'enunciado' not in dados or 'respostas' not in dados:
        raise InvalidAtividadeData('Campos id_disciplina, enunciado e respostas são obrigatórios.')
    nova_atividade = {
        'id_atividade': gerar_novo_id(),
        'id_disciplina': dados['id_disciplina'],
        'enunciado': dados['enunciado'],
        'respostas': dados.get('respostas', [])
    }
    atividades.append(nova_atividade)
    return nova_atividade

def atualizar_atividade(id_atividade, dados):
    for i, atividade in enumerate(atividades):
        if atividade['id_atividade'] == id_atividade:
            if 'id_disciplina' in dados:
                atividades[i]['id_disciplina'] = dados['id_disciplina']
            if 'enunciado' in dados:
                atividades[i]['enunciado'] = dados['enunciado']
            if 'respostas' in dados:
                atividades[i]['respostas'] = dados['respostas']
            return atividades[i]
    raise AtividadeNotFound

def excluir_atividade(id_atividade):
    for i, atividade in enumerate(atividades):
        if atividade['id_atividade'] == id_atividade:
            del atividades[i]
            return
    raise AtividadeNotFound

def gerar_novo_id():
    if atividades:
        return max(atividade['id_atividade'] for atividade in atividades) + 1
    else:
        return 1
