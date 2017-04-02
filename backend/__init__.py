from Framework import PontoDeInicio

def application ( variaveis_do_ambiente, iniciar_resposta):
    try:
        resposta = PontoDeInicio(variaveis_do_ambiente)
        corpo_da_resposta = resposta.getCorpoDaResposta()
        status_da_resposta = resposta.getStatusDaResposta()
        cabecalho_da_resposta = resposta.getCabecalhoDaResposta()
    except:
        corpo_da_resposta = b'{ "status" : 500 , "message" : "Internal Server Error" }'
        status_da_resposta = "500 Internal Server Error"
        cabecalho_da_resposta = resposta.getCabecalho = [('Content-Type', 'application/json; charset=UTF-8'),('Content-Length', str(len(corpo_da_resposta)))]

    iniciar_resposta(status_da_resposta, cabecalho_da_resposta)
    return [corpo_da_resposta]
