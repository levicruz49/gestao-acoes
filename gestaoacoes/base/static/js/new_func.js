function pagar_conta(id){
    token = document.getElementsByName("csrfmiddlewaretoken")[0].value;

    $.ajax({
        type: 'POST',
        url: '/contas_pagar/pagou_conta/' + id + '/',
        data: {
            csrfmiddlewaretoken: token,
        },
        success: function(result){
            $("#mensagem").text(result.mensagem);
        }
    });
}