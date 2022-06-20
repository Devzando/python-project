var div = document.getElementsByClassName("botaoArquivo")[0];
var input = document.getElementById("inputArquivo");
let buttonSend = document.getElementById('send')
let form = document.getElementById('submit')

let controllerSend = 0
div.addEventListener("click", function(){
    input.click();
});

input.addEventListener("change", function(){
    var nome = "Não há arquivo selecionado. Selecionar arquivo...";
    if(input.files.length > 0) nome = input.files[0].name;
    div.innerHTML = nome;
    document.getElementById("setinha").style.transform = 'rotate(270deg)';
    controllerSend = 1
});

buttonSend.addEventListener('click', function(e) {
    if(controllerSend == 0) return e.preventDefault()
    controllerSend = 0

})

