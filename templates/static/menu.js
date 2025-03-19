let aleatorioInput = document.getElementsByName('Aleatório')[0]; // Primeiro elemento
aleatorioInput.addEventListener('change', selecionaTodos);
aleatorioInput.value = "nada"
function desOculta(elementoId){

    document.getElementById(elementoId).style.display =  'flex'

}


function selecionaTodos(){
    inputs = Array.from(document.getElementsByClassName('checkBoxMenuGeral'))
  
    inputs.forEach(input => {
       
        input.checked  = !input.checked

        
    });
    aleatorioInput.checked = !aleatorioInput.checked


}