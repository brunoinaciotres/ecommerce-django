const addCardModal = document.querySelector("#add-card-modal")
const backdropAddCardModal = document.querySelector("#backdrop-add-card-modal")
const radios = document.querySelectorAll('.radio-payment-method');
const cardCvcInput = document.querySelector("#card-cvc")
const cardNameInput = document.querySelector("#card-name")
const cardValInput = document.querySelector("#card-val")
const cardNumberInput = document.querySelector("#card-number")
const addPaymentBtn = document.querySelector("#add-payment-button")

document.addEventListener('keydown', function (event) {
    if (event.key === 'Escape' || event.key === 'Esc') {
        if (addCardModal.style.display == "none") {
            return
        }
        closeAddCardModal();
    }
});

backdropAddCardModal.addEventListener('click', () => {
    closeAddCardModal()
})

radios.forEach(radio => {
    radio.addEventListener('change', function () {
        radios.forEach(r => {
            document.querySelector(`label[for="${r.id}"]`).classList.remove('selected-radio');
        });
        const selectedLabel = document.querySelector(`label[for="${this.id}"]`);
        selectedLabel.classList.add('selected-radio');
    });
});

addPaymentBtn.addEventListener("click", () => {
    if (cardNumberInput.value.length == 0) {
        alert("Preencha todos os dados")
        return
    }

    let expiryDate =  document.getElementById('card-val').value.split("/")
    let expiryDateYear = expiryDate[1]
    let expiryDateMonth = expiryDate[0]
    let expiryDateDay = "01"
    let expiryDateFormatted = `20${expiryDateYear}-${expiryDateMonth}-${expiryDateDay}`
    
    cardValInput.dataset.expiryDateFormatted = expiryDateFormatted

    const cardData = {
        cardNumber: document.getElementById('card-number').value,
        cardName: document.getElementById('card-name').value,
        cvc: document.getElementById('card-cvc').value,
        expiryDate: expiryDateFormatted,
        paymentMethod: document.querySelector('input[name="payment"]:checked').value 
    };

    const event = new CustomEvent('cardAdded', { detail: cardData });
    document.dispatchEvent(event);

    closeAddCardModal()
})

cardNumberInput.addEventListener('input', (event) => {
    // Remove qualquer caractere que não seja dígito
    let valor = event.target.value.replace(/\D/g, '');

    // Adiciona os traços a cada 4 dígitos, sem deixar espaços ou traços adicionais
    valor = valor.match(/.{1,4}/g)?.join('-') || '';

    event.target.value = valor;
});


//-------------FUNCTIONS----------------

function closeAddCardModal() {
    addCardModal.style.display = "none"
}

function openCardModal() {
    addCardModal.style.display = " flex"
}


function generateFakeCardNumber() {
    // MasterCard geralmente começa com números entre 51 e 55 ou 2221 a 2720.
    const prefixosMasterCard = [
        ...Array.from({ length: 5 }, (_, i) => 51 + i), // 51 a 55
        ...Array.from({ length: 500 }, (_, i) => 2221 + i) // 2221 a 2720
    ];

    // Seleciona um prefixo aleatório de MasterCard
    const prefixo = prefixosMasterCard[Math.floor(Math.random() * prefixosMasterCard.length)];

    // Determina quantos dígitos faltam para completar 15 dígitos (sem o dígito verificador)
    const numDigitosRestantes = 15 - prefixo.toString().length;

    // Gera os próximos dígitos aleatórios para completar os 15 dígitos
    const numeroParcial = prefixo.toString() + Array.from({ length: numDigitosRestantes }, () => Math.floor(Math.random() * 10)).join('');

    // Calcula o dígito verificador usando o algoritmo de Luhn
    const digitoVerificador = calcularDigitoVerificador(numeroParcial);
    const numeroCartao = numeroParcial + digitoVerificador;

    numeroCartaoFormatted = numeroCartao.match(/.{1,4}/g)?.join('-') || '';

    return numeroCartaoFormatted;
}

function calcularDigitoVerificador(numero) {
    let soma = 0;
    let alternar = true;

    for (let i = numero.length - 1; i >= 0; i--) {
        let n = parseInt(numero[i], 10);

        if (alternar) {
            n *= 2;
            if (n > 9) n -= 9;
        }

        soma += n;
        alternar = !alternar;
    }

    // Calcula o dígito verificador
    return (10 - (soma % 10)) % 10;
}

function generateFakeCvc() {
    let fakeCvc = Math.floor(Math.random() * 900) + 100
    return fakeCvc
}

function generateFakeName() {
    const nomes = [
        "Lucas", "Maria", "Pedro", "Ana", "João",
        "Carla", "Rafael", "Fernanda", "Gustavo", "Juliana"
    ];

    const sobrenomes = [
        "Silva", "Santos", "Oliveira", "Pereira", "Souza",
        "Almeida", "Costa", "Rocha", "Martins", "Azevedo"
    ];

    const nome = nomes[Math.floor(Math.random() * nomes.length)];
    const sobrenome = sobrenomes[Math.floor(Math.random() * sobrenomes.length)];

    return `${nome} ${sobrenome}`;
}

function generateFakeVal() {
    // Gera um mês aleatório entre 1 e 12 e garante que tenha dois dígitos 
    const month = String(Math.floor(Math.random() * 12) + 1).padStart(2, '0');

    // Gera um ano entre 24 e 30 
    const year = String(Math.floor(Math.random() * 7) + 24);

    return `${month}/${year}`;
}

function fillCardData() {
    let cardNumber = generateFakeCardNumber()
    let cardCvc = generateFakeCvc()
    let cardName = generateFakeName()
    let cardVal = generateFakeVal()
    cardNumberInput.value = cardNumber
    cardCvcInput.value = cardCvc
    cardNameInput.value = cardName
    cardValInput.value = cardVal
}



