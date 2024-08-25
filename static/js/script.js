$(document).ready(function(){
    $('#adiciona_dados').click(function(){
        $.ajax({
            url:'lista/produtos/',
            method: 'GET',
            success: function(data){
                const tabela = $('#tabela tbody');
                tabela.empty(); // limpa atabela antes de inserir novos dados

                data.forEach(function(produto){
                    tabela.append(`
                        <tr>
                            <td>${produto.nome}</td>
                            <td>${produto.descricao}</td>
                            <td>${produto.preco}</td>
                            <td>${produto.status}</td>
                            <td>${produto.categoria}</td>
                            <td>${produto.usuario}</td>
                        </tr>
                    `);
                });   
            },
            error: function(error){
                console.error('Erro ao carregar dados', error);
            }       
        });
    });
});