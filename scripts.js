let lista = []

function Salvar() {
    let entrada1 = document.getElementById("nome").value
    let entrada2 = document.getElementById("Gmail").value
    let entrada3 = document.getElementById("senha").value

    lista = [entrada1, entrada2, entrada3]

    console.log(lista)
    alert("Dados salvos: " + lista)
}
