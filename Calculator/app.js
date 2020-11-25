function calculateLoan() {
    const amount = document.querySelector("#amount").value;
    const interest_rate = document.querySelector("#interest").value;
    const time = document.querySelector("#time").value;
    const interest = (amount * (interest_rate * 0.01)) / time;
    const payment = ((amount / time) + interest);

    document.querySelector("#payment").innerHTML = 'EMI: ₹' + payment;

}