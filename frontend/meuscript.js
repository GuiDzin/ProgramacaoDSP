$(function(){

    //Quando o documento estiver carregado
    $.ajax({
        url: 'http://localhost:5000/listar_pokemons',
        method: 'GET',
        dataType: 'json', //Recebe os dados no formato json
        success: listar, //Chama a função listar
        erro: function(){
            alert("Erro ao ler dados, verifique o Backend!")
        }
    }); 

    function listar(pokemon){
        //Percorre a lista retornada
        for(var i in pokemon){
            //Cria linhas com os dados
            lin = '<tr>' + 
                '<td>' + pokemon[i].nome +  '</td>' +
                '<td>' + pokemon[i].tipo +  '</td>' +
                '<td>' + pokemon[i].categoria +  '</td>' +
                '<td>' + pokemon[i].altura +  '</td>' +
                '<td>' + pokemon[i].peso +  '</td>'  +
                '</tr>';
    
                $('#corpoTabelaPokemon').append(lin);
            }
    }
});

