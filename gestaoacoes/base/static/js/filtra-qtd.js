function process_response(quantidade){
    qtd_select = document.getElementById('quantidade');
    qtd_select.innerHTML = "";

    quantidade.forEach(function(quantidade)){
        var option = document.createElement("option");
        option.text = quantidade.fields.qtd;
        qtd_select.add(option);

    });
}

function filtraQTD(){
    familia_id = document.getElementById('familias').value;
    $.ajax({
        type: 'GET',
        url: '/filtra-dados/',
        data: {
            outro_param: familia_id
        },

        success: function(result){
            process_response(result)
            $("#mensagem").text(result.mensagem);
        }
    });
}