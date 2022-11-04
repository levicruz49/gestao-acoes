from ecogestao.apps.funcionarios import facade


def funcionarios_pendentes(request):
    return {
        'qtd_acessos': facade.contar_func_pendentes(),
        'acessos': facade.listar_func_pendentes()
    }
