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


// -----FUNCTIONS------

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

function updateCartItemsCountHeader(item){
    let totalItemsCount = item.total_items_count
    const cartItemCounterElement = document.querySelector("#how-many-cart-itens-value")
    cartItemCounterElement.innerText = totalItemsCount

}

// Increase and Decrease Product Amount Buttons 

async function increaseProductAmount(event){
    let orderItemElementId = event.target.id

    let dividedString = orderItemElementId.split("order-item-increase-");

    let productIntId = dividedString[1]
    let totalOrderItemPriceElement = document.querySelector(`#order-item-total-price-${productIntId}`)

    const itemIncreased = await addToCartFetch(productIntId)
    
    let orderItems = itemIncreased.order_items
    
    orderItems.forEach(item => {
        if (item.product_id == productIntId){
            let newCounterValue = item.product_amount
            let productPrice = totalOrderItemPriceElement.dataset.individualProductPrice;
            console.log(productPrice)
            changeProductAmountCounterValue(newCounterValue, productIntId)
            changeOrderItemTotalPrice(productPrice, item.product_amount, productIntId )
        }
    })


    
}

function decreaseProductAmount(event, newAmount){
    
}

function changeProductAmountCounterValue(newValue, productId,){
    console.log("OrderItemId = " + productId)
    const counter = document.querySelector(`#product-amount-counter-${productId}`)

    console.log(counter)
    counter.innerText = newValue
}

function changeOrderItemTotalPrice(productPrice, productAmount, productId){
    let productAmountNumber = Number(productAmount)
    let cleanedProductPriceNumber = Number(productPrice.replace(',', '.').trim())
    let newValue = productAmountNumber * cleanedProductPriceNumber
    let formattedValue = newValue.toLocaleString('pt-BR', {
        minimumFractionDigits: 2,
        maximumFractionDigits: 2
    }).replace(/\./g, '')

    const orderItemTotalPriceElement = document.querySelector(`#order-item-total-price-${productId}`)
    orderItemTotalPriceElement.innerText = formattedValue
   
    changeCartTotalPrice(cleanedProductPriceNumber)
    
}

function changeCartTotalPrice(valueToIncrement){
    const cartTotalPriceElement = document.querySelector("#cart-total-price")
    const cartTotalPriceValue = Number(cartTotalPriceElement.innerText.replace(',', '.').trim())
    console.log("total_price_curr" + cartTotalPriceElement)

    let sum = cartTotalPriceValue + valueToIncrement
    console.log("typeof sum = " + typeof sum)

    let formattedValue = sum.toLocaleString('pt-BR', {
        minimumFractionDigits: 2,
        maximumFractionDigits: 2
    }).replace(/\./g, '')
    cartTotalPriceElement.innerText = formattedValue

}

// Interact with cart - fetchs

async function addToCartFetch(productId) {
    const res = await fetch('/add_to_cart', {
        method: 'POST',
        mode: 'cors',
        body: JSON.stringify({
                "product_id" : productId
            })
        
    })
    const item = await res.json()
    updateCartItemsCountHeader(item)
    return item
}
