const addAdressModal = document.querySelector("#add-adress-modal")
const backdropAddAdressModal = document.querySelector("#backdrop-add-adress-modal")
const adressStreetInput = document.querySelector("#adress-street");
const adressNumberInput = document.querySelector("#adress-number");
const adressComplementInput = document.querySelector("#adress-complement");
const adressNeighborhoodInput = document.querySelector("#adress-neighborhood");
const adressStateInput = document.querySelector("#adress-state");
const adressCityInput = document.querySelector("#adress-city");
const addAdressBtn = document.querySelector("#add-adress-button")

document.addEventListener('keydown', function (event) {
    if (event.key === 'Escape' || event.key === 'Esc') {
        if (addAdressModal.style.display == "none") {
            return
        }
        closeAddAdressModal()
    }
});

backdropAddAdressModal.addEventListener("click", () => {
    closeAddAdressModal()
    }
)

addAdressBtn.addEventListener('click', () => {
    let adressText = `${adressStreetInput.value}, ${adressNumberInput.value}/${adressComplementInput.value} - ${adressNeighborhoodInput.value}, ${adressCityInput.value} - ${adressStateInput.value}`
    const event = new CustomEvent('adressAdded', { detail: adressText })
    document.dispatchEvent(event)
    closeAddAdressModal()

})


function openAdressModal() {
    addAdressModal.style.display = "flex"
}

function closeAddAdressModal() {
    addAdressModal.style.display = "none"
}

function fillAdressData() {
    adressStreetInput.value = "Avenida Esbertalina Barbosa Damiani"
    adressNeighborhoodInput.value = "Guriri Norte"
    adressCityInput.value = "São Mateus"
    adressStateInput.value = "ES"
    adressComplementInput.value = "100"
    adressNumberInput.value = "203"

}