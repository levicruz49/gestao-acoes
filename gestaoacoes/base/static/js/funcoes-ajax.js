function utilizouHoraExtra(id){
    token = document.getElementsByName("csrfmiddlewaretoken")[0].value;

    $.ajax({
        type: 'POST',
        url: '/horas-extras/utilizou-hora-extra/' + id + '/',
        data: {
            csrfmiddlewaretoken: token,
        },
        success: function(result){
            $("#mensagem").text(result.mensagem);
            $("#horas_atualizadas").text(result.horas);
        }
    });
}
function process_response(id_funcionario){
    func_select = document.getElementById('id_funcionario');
    func_select.innerHTML = "";

    id_funcionario.forEach(function(id_funcionario){
        var option = document.createElement("option");
        option.text = id_funcionario.fields.nome;
        func_select.add(option);
    });
}

function filtraFuncionarios(){
    filial_id = document.getElementById('id_filial').value;
    $.ajax({
        type: 'GET',
        url: '/vendas/carrega_func/',
        data: {
            outro_param: filial_id
        },
        success: function(result){
            process_response(result);

        }
    });
}