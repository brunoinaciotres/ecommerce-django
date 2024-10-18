const cardInputCheckout = document.querySelector("#card-input")
const adressInputCheckout = document.querySelector("#adress-input")
const editCardButton = document.querySelector("#edit-card")
const editAdressButton = document.querySelector("#edit-adress")
const buyButton = document.querySelector(".buy-button")
const buyBtnDisabledIcon = document.querySelector("#buy-button-disabled-icon")
const buyBtnAbledIcon = document.querySelector("#buy-button-abled-icon")
const addCardIcon = document.querySelector("#add-card-icon")
const addCardText = document.querySelector("#add-card-text")
const addAdressIcon = document.querySelector("#add-adress-icon")
const addAdressText = document.querySelector("#add-adress-text")

document.addEventListener("cardAdded", () => {
    const cardData = event.detail
    styleCardInputCheckout(cardData)
    toAbleBuyBtn()
})

document.addEventListener("adressAdded", () => {
    const adress = event.detail
    styleAdressInputCheckout(adress)
    toAbleBuyBtn()
})

editCardButton.addEventListener("click", () => {
    openCardModal()
})
editAdressButton.addEventListener("click", () => {
    openAdressModal()
})

function toAbleBuyBtn() {
    if (cardInputCheckout.value && adressInputCheckout.value) {
        buyButton.classList.remove("disabled")
        buyBtnDisabledIcon.style.display = 'none'
        buyBtnAbledIcon.classList.remove("d-none")
    }
}

function styleCardInputCheckout(cardData) {
    cardInputCheckout.value = cardData.cardNumber
    cardInputCheckout.style.pointerEvents = 'none'
    addCardIcon.style.display = 'none'
    addCardText.style.display = 'none'
    cardInputCheckout.style.padding = ".8rem 1rem"
    cardInputCheckout.style.backgroundColor = "#4f4f4f"
    editCardButton.style.display = "block"
}

function styleAdressInputCheckout(adress) {
    adressInputCheckout.value = adress
    adressInputCheckout.style.pointerEvents = 'none'
    addAdressIcon.style.display = 'none'
    addAdressText.style.display = 'none'
    adressInputCheckout.style.padding = ".8rem 1rem"
    adressInputCheckout.style.backgroundColor = "#4f4f4f"
    editAdressButton.style.display = "block"
}
