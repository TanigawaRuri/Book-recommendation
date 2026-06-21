async function loadRecommendations() {
    const response = await fetch(
        `http://localhost:8000/api/recommendation`
    );

    console.log("response : ", response.status)
    const data = await response.json();

    const userId = data.user_id;
    console.log("data : ", data)

    const container =
        document.getElementById("recommendation-container");

    container.innerHTML = "";

    data.recommendations.forEach(book => {
        container.innerHTML += `
            <div class="book-card">
                <h3>${book.title}</h3>
                <button onclick="purchaseBook(${book.id})">
                    purchase
                </button>
            </div>
        `;
    });
}

async function purchaseBook(bookId) {
    const response = await fetch("http://localhost:8000/api/event/purchase", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            book_id: bookId,
            event_type: "click"
        })
    });

    const data = await response.json();
    console.log(data);
    console.log("purchase logged:", data);
}

loadRecommendations();