const inputFodastico = document.getElementById("input");
const botaoZika = document.getElementById("botaozinhofoda");
const body = document.getElementsByTagName("body")[0];

botaoZika.addEventListener("click", () => {
    const listonaThaisdoAmaral = document.createElement("ul");
    const itemDaLista = document.createElement("li");
    const RemovedorUltrassonico = document.createElement("button");
    RemovedorUltrassonico.innerHTML = "QUER REMOVER, PAPAI ?";

    body.appendChild(listonaThaisdoAmaral);
    listonaThaisdoAmaral.appendChild(itemDaLista);
    listonaThaisdoAmaral.appendChild(RemovedorUltrassonico);
    itemDaLista.innerHTML = input.value;

    RemovedorUltrassonico.addEventListener("click", () => {
        itemDaLista.remove();
        RemovedorUltrassonico.remove();
        listonaThaisdoAmaral.remove();
    });

    input.value = null;
});